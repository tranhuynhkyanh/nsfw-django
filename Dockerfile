FROM python:3.9

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

RUN apt-get update && apt-get install -y supervisor

CMD gunicorn core.wsgi:application --bind 0.0.0.0:8000
