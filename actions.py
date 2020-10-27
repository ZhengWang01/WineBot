# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from src.information_retrieval_model import Wine_Information_Retrieval_Model as wir

import pandas as pd
import numpy as np
import pickle
from textwrap import wrap
import re

import matplotlib.pyplot as plt
from skimage import io

import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia

from gensim.models.doc2vec import Doc2Vec
from gensim.test.utils import get_tmpfile
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from scipy import sparse


class ActionGetWine(Action):
    def name(self):
        return "action_get_wine"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message.get("text")
        # dispatcher.utter_message(query)
        message = query
        recs = self.query_similar_wines(message, 5)
        print(recs)
        recom = self.view_recommendations(recs)
        # print(recom)
        recomstr = '\n'.join([str(i) for i in recom])
        dispatcher.utter_message(recomstr)

        # return []

    def __init__(self):
        self.dv = Doc2Vec.load("./ml_models/doc2vec_model")
        self.tf = pickle.load(open("./ml_models/tfidf_model.pkl", "rb"))
        self.svd = pickle.load(open("./ml_models/svd_model.pkl", "rb"))
        self.svd_feature_matrix = pickle.load(open("./ml_models/lsa_embeddings.pkl", "rb"))
        self.doctovec_feature_matrix = pickle.load(open("./ml_models/doctovec_embeddings.pkl", "rb"))
        self.df = df = pd.read_pickle("./wine_data.pkl")
        self.hal = sia()


    @staticmethod
    def stem_words(text):
        text = text.split()
        stemmer = SnowballStemmer('english')
        stemmed_words = [stemmer.stem(word) for word in text]
        text = " ".join(stemmed_words)
        return text


    @staticmethod
    def make_lower_case(text):
        return text.lower()


    @staticmethod
    def remove_stop_words(text):
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)
        return text


    @staticmethod
    def remove_punctuation(text):
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        text = " ".join(text)
        return text


    def get_message_sentiment(self, message):
        sentences = re.split('\.|\but',message)
        sentences = [x for x in sentences if x != ""]
        love_message = ""
        hate_message = ""
        for s in sentences:
            sentiment_scores = self.hal.polarity_scores(s)
            if sentiment_scores['neg'] > 0:
                hate_message = hate_message + s
            else:
                love_message = love_message + s
        return love_message, hate_message


    def clean_message(self, message):
        message = self.make_lower_case(message)
        message = self.remove_stop_words(message)
        message = self.remove_punctuation(message)
        message = self.stem_words(message)
        return message


    def get_message_tfidf_embedding_vector(self, message):
        message_array = self.tf.transform([message]).toarray()
        message_array = self.svd.transform(message_array)
        message_array = message_array[:,0:25].reshape(1, -1)
        return message_array


    def get_message_doctovec_embedding_vector(self, message):
        message_array = self.dv.infer_vector(doc_words=message.split(" "), epochs=200)
        message_array = message_array.reshape(1, -1)
        return message_array


    @staticmethod
    def get_similarity_scores(message_array, embeddings):
        cosine_sim_matrix = pd.DataFrame(cosine_similarity(X=embeddings,
                                                           Y=message_array,
                                                           dense_output=True))
        cosine_sim_matrix.set_index(embeddings.index, inplace=True)
        cosine_sim_matrix.columns = ["cosine_similarity"]
        return cosine_sim_matrix


    def get_ensemble_similarity_scores(self, message):
        message = self.clean_message(message)
        bow_message_array = self.get_message_tfidf_embedding_vector(message)
        semantic_message_array = self.get_message_doctovec_embedding_vector(message)

        bow_similarity = self.get_similarity_scores(bow_message_array, self.svd_feature_matrix)
        semantic_similarity = self.get_similarity_scores(semantic_message_array, self.doctovec_feature_matrix)

        ensemble_similarity = pd.merge(semantic_similarity, bow_similarity, left_index=True, right_index=True)
        ensemble_similarity.columns = ["semantic_similarity", "bow_similarity"]
        ensemble_similarity['ensemble_similarity'] = (ensemble_similarity["semantic_similarity"] + ensemble_similarity["bow_similarity"])/2
        ensemble_similarity.sort_values(by="ensemble_similarity", ascending=False, inplace=True)
        return ensemble_similarity


    def get_dissimilarity_scores(self, message):
        message = self.clean_message(message)
        bow_message_array = self.get_message_tfidf_embedding_vector(message)
        semantic_message_array = self.get_message_doctovec_embedding_vector(message)

        dissimilarity = self.get_similarity_scores(bow_message_array, self.svd_feature_matrix)
        dissimilarity.columns = ["dissimilarity"]
        dissimilarity.sort_values(by="dissimilarity", ascending=False, inplace=True)
        return dissimilarity


    def query_similar_wines(self, message, n):

        love_message, hate_message = self.get_message_sentiment(message)

        similar_wines = self.get_ensemble_similarity_scores(love_message)
        dissimilar_wines = self.get_dissimilarity_scores(hate_message)
        dissimilar_wines = dissimilar_wines.query('dissimilarity > .3')
        similar_wines = similar_wines.drop(dissimilar_wines.index)

        return similar_wines.head(n)

    def view_recommendations(self, recs):

        titles = []
        for i in range(len(recs)):
            single_title = recs.index.tolist()[i]
            titles.append(single_title)

        return titles

    