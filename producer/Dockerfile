FROM python:3.11

ADD ./producer.py .

ADD ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./producer.py"]