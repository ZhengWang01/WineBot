  
# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./
COPY actions/svd_model.pkl ./
COPY actions/doc2vec_model ./
COPY actions/lsa_embeddings.pkl ./
COPY actions/doctovec_embeddings.pkl ./
COPY actions/tfidf_model.pkl ./
COPY actions/wine_data.pkl ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1000