FROM python:3.6.5
ENV PYTHONBUFFERED 1

WORKDIR /usr/src/app
RUN mdkir -p /user/src/app && \
    pip install --no-cache-dir -U pip wheel setuptools

COPY src/requirements.txt /user/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src /usr/src/app
EXPOSE 5080
CMD ["gunicorn"]