# WineBot
Your personal assistant in finding the optimum wine.

# Table of Contents
This is a wine recommendation chatbot for specific business use that translate taxonomy data into an interactive dialog.
1. [Motivations](README.md#motivations)
2. [Overview of the Project](README.md#overview-of-the-project)
3. [Repo Structure](README.md#repo-structure)
4. [Setup](README.md#setup)
5. [Requirements](README.md#requirements)
6. [Run A Train and Test](README.md#run-a-train-and-test)
10. [Details of the Implementation](README.md#details-of-the-implementation)


To check-out the repo:

```
git clone https://github.com/ZhengWang01/WineBot.git
```

## Motivations

According to an on-line survey, 44% of U.S. consumers prefer chat-bots to humans when it comes to customer relations. More than 80% of company is utilizing chatbot in 2020. Chatbot offer a multitude of benefits for both the customer and company. It increases customers satisfaction and generated more revenue for companies.

## Overview of the Project

In this project, I utilized the [Rasa](https://rasa.com/) open source chatbot. I trained Latent Sentiment Analysis models that takes the preprocessed customer query, and give corresponding recommendation based on what the customer need.

The deliverable of the project is a Web App that allows user to tell the chatbot what they need, and get the recommendation on which wine they should buy.

<p float="left">
  <img src="WineBotDemo.gif" width="800" />
</p>

## Repo Structure

Below is the structure of this repo.

    ├── README.md
    ├── data
    │   └── nlu.md
    │   └── stories.md
    │   └── wine_data.pkl
    ├── models
    │   └── doc2vec_model
    │   └── doc2vec_embeddings.pkl
    │   └── lsa_embeddings.pkl
    │   └── svd_model.pkl
    │   └── tfidf_model.pkl
    ├── src
    │   └── __init__.py
    │   └── information_retrieval_model.py
    ├── tests
    │   └── conversation_tests.md
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── WineBotDemo.gif
    ├── __init__.py
    ├── actions.py
    ├── config.yml
    ├── credentials.yml
    ├── domain.yml
    ├── endpoints.yml
    ├── index.html
    ├── requirements.txt
    ├── run_mode.ipynb
    └── train_model.ipynb

## Setup

clone the project:
```
git clone https://github.com/ZhengWang01/WineBot.git
```
Get into the main folder:
```
cd WineBot
```

Creating a virtual environment for the project
On macOS and Linux:

```
python3 -m venv env
```
On Windows:
```
py -m venv env
```
Activating a virtual environment
On macOS and Linux:
```
source env/bin/activate
```
On Windows:

```
.\env\Scripts\activate
```
## Requirements

```
pip3 install -r requirements.txt
```


## Run A Train and Test

The example code of how to train and check the results can be found in the Jupyter notebooks train_model.ipynb and run_model.ipynb.

Choice #1. To run the Rasa Chatbot in terminal, run:

```
rasa run actions & rasa shell
```

Choice #2. To run the Rasa Chatbot in browser, run:
```
rasa run -m models --enable-api --cors "*" --debug
```
In another terminal in the save directory and virtual environment, run:
```
rasa run actions
```
click on the index.html


## Details of the Implementation

