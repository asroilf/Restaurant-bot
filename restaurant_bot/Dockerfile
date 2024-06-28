FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app
RUN rasa train

EXPOSE 5005

CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*"]

