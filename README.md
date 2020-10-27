# WineBot
Your personal assistant in finding the optimum wine.

## What is WineBot?
Winebot is a wine recommendation chatbot. It is a combination of a recommender and a chatbot, where the recommender is built by using Doc2Vec and Latent Semantic Analysis(LSA) and the chatbot is built by utilizing the [Rasa](https://rasa.com/) Open Source Chatbot.

## Table of Contents
  * [Setup](#Setup)
    + [Setup with Docker](#Setup-with-Docker)
    + [Setup with Python virtual environment](#Setup-with-Python-virtual-environment)
  * [Run the Project](#Run-the-Project)
  * [Explore the Project](#Explore-the-Project)
  * [Usage](#usage)
  * [Results](#results)



## Setup

Clone this repo with

```
git clone https://github.com/ZhengWang01/WineBot.git
```

### Setup with Docker
**The recommended way to run this project is by installing Docker and building and running an image**.  This process manages libraries, the python runtime environment, and dependences; it also manages environment variables nicely. This maximizes stability and portability.

- First, visit https://www.docker.com to install the Docker platform (e.g. Docker Desktop) on your machine.

- To build and run your container, run the following in your command shell.

```
cd <project_path>
docker-compose up --build
```

- Check whether the services are up and running using below command:
```
docker ps -a
```
### Setup with Python virtual environment
Run the following command
```
cd <project_path>
python -m venv <environment_name>
source <environment_name>/bin/activate
pip install --upgrade pip
cd actions
pip install -r requirements-actions.txt 
```
## Run the Project
Talk to Winebot here [www.winebot.xyz](http://www.winebot.xyz/guest/conversations/production/b72f6317e7de4a2496285e4484c39056)

## Explore the Project
The project is deployed on [Rasa X](https://rasa.com/docs/rasa-x/), where you can build, improve, and deploy AI Assistants that are powered by the Rasa framework. Try and explore it here [www.winebot.xyz/login](http://winebot.xyz/login), with the passcode ```rasarasa```


## Usage
```
├── WineBot
│   ├── actions            # Custom actions files for the rasa chatbot
│   │   ├── actions.py
│   │   ├── doc2vec_model  # The models from training the data 
│   │   ├── doc2vec_embeddings.pkl
│   │   ├── lsa_embeddings.pkl
│   │   ├── svd_model.pkl
│   │   ├── tfidf_model.pkl
│   ├── data   
│   │   ├── nlu.md         # NLU training data stores structured information about user messages
│   │   ├── stories.md     # Stories are a type of training data used to train the assistant's dialogue management model      
│   ├── Dockerfile
│   ├── config.yml         # The configuration file defines the components and policies that the model will use to make predictions based on user input
│   ├── credentials.yml    # To connect to most channels, you will need to add some credentials (e.g. an API token)
│   ├── docker-compose.yml 
│   ├── domain.yml         # The domain defines the universe in which the assistant operates. It specifies the intents, entities, slots, responses, forms, and actions the bot should know about 
│   ├── endpoints.yml      # Contains the different endpoints your bot can use.
│   ├── run_model.ipynb    # WineBot demo
│   ├── train_model.ipynb  # WineBot model training
```

## Results

The deliverable of the project is a Web App that allows user to tell the chatbot what they need, and get the recommendation on which wine they should buy.

<p float="left">
  <img src="WineBotDemo.gif" width="800" />
</p>


