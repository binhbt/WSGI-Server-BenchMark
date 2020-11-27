FROM python:3.6.9

LABEL maintainer="LeoBui<treiro@gmail.com>"

COPY . /
RUN apt-get -y update
RUN apt-get -y install libev-dev
RUN pip install -r requirements.txt

ENTRYPOINT ["/runserver.sh"]
# EXPOSE 8000

# RUN runserver.sh
# CMD ["honcho", "start"]