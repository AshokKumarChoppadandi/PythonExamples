import argparse
import os
import shutil
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain.vectorstores.chroma import Chroma
import datetime

CHROMA_PATH = ""
DATA_PATH = ""


def main():
    global CHROMA_PATH, DATA_PATH

    # Check if the database should be cleared (using the --clear flag)
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    parser.add_argument("-i", "--inputDir", required=True, type=str, help="Input directory path for PDFs or Text files")
    parser.add_argument("-v", "--vectorStore", required=True, type=str, help="Vector Store directory path to store "
                                                                             "Embeddings")
    parser.add_argument("-s", "--ollamaServiceUrl", required=True, type=str, help="Ollama Service URL")
    parser.add_argument("-m", "--model", required=True, type=str, help="LLM to use")

    args = parser.parse_args()

    if args.reset:
        print("Clearing Database")
        clear_database()

    if args.inputDir:
        DATA_PATH = args.inputDir

    if args.vectorStore:
        CHROMA_PATH = args.vectorStore

    ollama_service_url = args.ollamaServiceUrl
    model = args.model

    # Create (or update) the data store
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks, ollama_service_url, model)


def clear_database():
    if os.path.exists(CHROMA_PATH):
        print("Resetting the database.")
        shutil.rmtree(CHROMA_PATH)


def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    print(f"Loading documents from '{DATA_PATH}' are completed")
    return document_loader.load()


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False
    )
    print("Splitting documents in to chunks")
    return text_splitter.split_documents(documents)


def add_to_chroma(chunks: list[Document], ollama_service_url: str, model: str):
    # Load the existing Database
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function(base_url=ollama_service_url, model=model)
    )

    # Calculate Page IDs
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    # IDs are always included by default
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that doesn't exist in the DB
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"Added new documents: {len(new_chunks)}")
        new_chunks_ids = [chunk.metadata["id"] for chunk in new_chunks]
        print("New chunks with new IDs are added")
        db.add_documents(new_chunks, ids=new_chunks_ids)
        print("New chunks with new IDs are persisted")
        db.persist()

    else:
        print("No New documents to add")


def calculate_chunk_ids(chunks):
    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source: Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data
        chunk.metadata["id"] = chunk_id

    return chunks


if __name__ == '__main__':
    print(f"start_time = {datetime.datetime.now()}")
    main()
    print("Completed!")
    print(f"end_time = {datetime.datetime.now()}")
