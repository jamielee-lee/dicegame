FROM python:3
WORKDIR /dicegame
COPY . .
RUN pip install coverage
CMD [ "python", "./dicegame.py" ]