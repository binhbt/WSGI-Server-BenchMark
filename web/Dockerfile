FROM python:3.6.9

LABEL maintainer="LeoBui<treiro@gmail.com>"

COPY . /
RUN apt-get -y update
RUN apt-get -y install libev-dev
RUN pip3 install -r requirements.txt

# ENTRYPOINT ["/runserver.sh"]
EXPOSE 8000

# ENV C_FORCE_ROOT="true"

CMD ["honcho", "start"]