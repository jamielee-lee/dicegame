FROM python:3
WORKDIR /tictactoe
COPY tictactoe.py .
CMD [ "python", "./tictactoe.py" ]