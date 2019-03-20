FROM python:3

WORKDIR /app

COPY . .

CMD ["python", "./weird-weather/app.py"]