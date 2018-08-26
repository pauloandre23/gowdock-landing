FROM gcr.io/google_appengine/python

RUN virtualenv -p python3 /env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Add application code.
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD . /app
CMD gunicorn -b :8080 gowdock_landing.wsgi
#EXPOSE 8080:8080