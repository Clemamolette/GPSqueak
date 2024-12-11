FROM python:3.9


RUN mkdir /app

WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]