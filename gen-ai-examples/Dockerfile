FROM python:3.11.9

LABEL author="Ashok Kumar Choppadandi <ashokkumar98778@gmail.com>" \
        maintainer="Ashok Kumar Choppadandi <ashokkumar98778@gmail.com>" \
        description="Python 3.11.9 docker image for running the Chatbot"

USER root

RUN mkdir -p chatbot-example/files

WORKDIR /chatbot-example

COPY ./files/*.pdf /chatbot-example/files/

COPY ollama/*.py /chatbot-example/
COPY ./requirements.txt /chatbot-example/

RUN pip install -r /chatbot-example/requirements.txt

ENV INPUT_DATA_DIR files
ENV VECTOR_STORE_PATH vector_store
ENV OLLAMA_SERVICE_URL localhost
ENV MODEL llama2

COPY docker-entrypoint.sh /chatbot-example/docker-entrypoint.sh

RUN chmod +x /chatbot-example/docker-entrypoint.sh

ENTRYPOINT ["/chatbot-example/docker-entrypoint.sh"]
CMD ["sh"]