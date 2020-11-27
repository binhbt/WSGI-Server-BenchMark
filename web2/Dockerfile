FROM python:3.6.9

LABEL maintainer="LeoBui<treiro@gmail.com>"

COPY . /
RUN apt-get -y update
RUN apt-get -y install libev-dev
RUN pip install -r requirements.txt

# RUN runserver.sh
CMD ["honcho", "start"]