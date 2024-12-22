FROM python:3.11

ADD ./producer.py .
ADD ./generate_coordinate.py .

ADD ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "./producer.py"]