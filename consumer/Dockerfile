FROM python:3.11

ADD ./consumer.py .

ADD ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "./consumer.py"]
