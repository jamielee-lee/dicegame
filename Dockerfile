FROM python:3
WORKDIR /dicegame
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "./dicegame.py" ]