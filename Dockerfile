FROM python:3.5

ENV PYTHONBUFFERED 1

WORKDIR /usr/src/app

RUN mkdir -p /user/src/app && \
    pip install --no-cache-dir -U pip wheel setuptools && \
    pip install Flask && \
    pip install Flask-RESTful

COPY requirements.txt /user/src/app/
COPY src /usr/src/app
EXPOSE 8081

CMD ["python", "./src/app.py"]