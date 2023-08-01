FROM python:3.10.6

RUN mkdir /levers

WORKDIR /levers

COPY ./app2/requirements.txt .

RUN pip install -r requirements.txt

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./worker-start-2.sh /worker-start-2.sh
RUN chmod +x /worker-start-2.sh

ENV PYTHONPATH=/levers