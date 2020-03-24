FROM python:3.8
RUN groupadd -r user && useradd -r -g user user
RUN pip install Flask uWSGI requests
WORKDIR /app
COPY app /app
COPY entry-point.sh /
EXPOSE 9090 9191
USER user
CMD ["/entry-point.sh"]