FROM python:3

WORKDIR /app

RUN apt-get update -y
RUN apt-get upgrade -y
RUN pip install requests
RUN pip install certifi

COPY . .

CMD ["python3", "./weird-weather/app.py"]