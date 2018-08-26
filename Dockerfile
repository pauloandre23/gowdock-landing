FROM gcr.io/google_appengine/python

# Add application code.
ADD . /app
RUN pip install -r /app/requirements.txt

CMD export DJANGO_PASSWORD=$(cat /etc/secrets/djangouserpw); gunicorn -b :$PORT mysite.wsgi
