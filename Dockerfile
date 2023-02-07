FROM python:3.9-slim-buster

WORKDIR /app

COPY supervisor.conf /etc/supervisor/conf.d/
COPY requirements.txt .

# installing dependencies and pip packages
RUN apt update && apt install -y \
    supervisor vim gcc libmariadb-dev-compat libmariadb-dev \
    && pip3 install -r requirements.txt \
    && mkdir -p /var/log/storefront

COPY . .

EXPOSE 8000
ENTRYPOINT [ "/usr/bin/supervisord" ]
