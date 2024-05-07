FROM python:3

ADD tictactoe.py .

CMD [ "python", "./tictactoe.py" ]