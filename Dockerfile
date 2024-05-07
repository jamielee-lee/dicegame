FROM python:3
WORKDIR /dicegame
COPY . .
CMD [ "python", "./dicegame.py" ]