FROM python:3.10.6

RUN mkdir /levers

WORKDIR /levers

COPY ./app1/requirements.txt .

RUN pip install -r requirements.txt

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

#COPY ./app1/app /levers

ENV PYTHONPATH=/levers