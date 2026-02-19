# from langchain_community.embeddings.ollama import OllamaEmbeddings

from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_ollama import OllamaEmbeddings  

def get_embedding_function():
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    return embedding

# def get_embedding_function():
# #     embedding = BedrockEmbeddings(
# #          credentials_profile_name="default", region_name="us-east-1"
# #     )
#     embedding = OllamaEmbeddings(model="nomic-embed-text")
#     return embedding