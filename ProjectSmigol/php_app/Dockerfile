FROM httpd

RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*

ADD . /app