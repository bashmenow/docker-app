FROM python:3.8

WORKDIR /app
COPY app /app
COPY requirements.txt /app/
COPY entry-point.sh /

RUN groupadd -r user \
        && useradd -r -g user user \
        && pip install -r requirements.txt

EXPOSE 9090
USER user
CMD ["/entry-point.sh"]
