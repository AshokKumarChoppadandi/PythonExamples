#!/bin/sh
#set -e

python /chatbot-example/chatbot-ollama-llama2.py --inputDir $INPUT_DATA_DIR --vectorStore $VECTOR_STORE_PATH -s $OLLAMA_SERVICE_URL -m $MODEL

tail -f /dev/null