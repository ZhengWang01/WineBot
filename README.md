# WineBot
Your personal assistant in finding the optimum wine.
Please try it ou here [www.winebot.xyz](http://winebot.xyz/guest/conversations/production/b72f6317e7de4a2496285e4484c39056)

## What is WineBot?
Winebot is a wine recommendation chatbot. It is a combination of a recommender and a chatbot, where the recommender is built by using Doc2Vec and Latent Semantic Analysis(LSA) and the chatbot is built by utilizing the [Rasa](https://rasa.com/) Open Source Chatbot.

## Table of Contents
  * [Installation](#installation)
  * [Usage](#usage)
  * [Results](#results)



## Installation

clone into directory:
```
git clone https://github.com/ZhengWang01/WineBot.git
cd WineBot
```

Run the below command within the project directory (this will install the dependencies):
```
docker-compose up --build
```
Check whether the services are up and running using below command:
```
docker ps -a
```

## Usage
```
├── WineBot
│   ├── actions            # custom actions files for the rasa chatbot
│   │   ├── actions.py
│   │   ├── doc2vec_model
│   │   ├── doc2vec_embeddings.pkl
│   │   ├── lsa_embeddings.pkl
│   │   ├── svd_model.pkl
│   │   ├── tfidf_model.pkl
│   ├── data   
│   │   ├── nlu.md
│   │   ├── stories.md
│   │   ├── utils.py       
│   ├── Dockerfile
│   ├── config.yml
│   ├── credentials.yml
│   ├── docker-compose.yml
│   ├── domain.yml
│   ├── endpoints.yml
│   ├── run_model.ipynb    # WineBot demo
│   ├── train_model.ipynb  # WineBot model training
```

## Results

The deliverable of the project is a Web App that allows user to tell the chatbot what they need, and get the recommendation on which wine they should buy.

<p float="left">
  <img src="WineBotDemo.gif" width="800" />
</p>


