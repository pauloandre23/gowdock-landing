FROM gcr.io/google_appengine/python

RUN virtualenv -p python3 /env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Add application code.
ADD . /app
RUN pip install -r /app/requirements.txt

CMD gunicorn -b :8080 gowdock_landing.wsgi
