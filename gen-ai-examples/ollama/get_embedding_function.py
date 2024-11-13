from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function(base_url: str, model: str):
    """
    embeddings = OllamaEmbeddings(
        base_url="http://node103.ord.adhoc.dw.cnvr.net:11434",
        model="llama2"
    )
    """
    embeddings = OllamaEmbeddings(
        base_url=base_url,
        model=model
    )

    """
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us_east_1"
    )
    """
    return embeddings
