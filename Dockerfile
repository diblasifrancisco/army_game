FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /army_game
WORKDIR /army_game
COPY requirements.txt /army_game/
RUN pip install -r requirements.txt
COPY . /army_game/
