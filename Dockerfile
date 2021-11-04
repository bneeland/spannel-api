FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
# CMD gunicorn web.wsgi:application --bind 0.0.0.0:$PORT
# CMD gunicorn api.wsgi:application --bind 0.0.0.0:$PORT
