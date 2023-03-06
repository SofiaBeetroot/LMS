FROM python:3.8

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt
RUN rm -rf /code/account/migrations/*.py
RUN rm -rf /code/article/migrations/*.*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
