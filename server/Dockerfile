FROM ubuntu:20.04
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y stockfish
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
