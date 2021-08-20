FROM python:latest

COPY ./requirements.txt /requirements.txt
COPY ./bot.py /bot.py
COPY ./.env /.env

RUN python -m pip install -r /requirements.txt

CMD ["python", "/bot.py"]
