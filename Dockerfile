# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.13-alpine

# Copy local code to the container image.
ENV APP_HOME=/app
ENV ROOT_PATH=/
WORKDIR $APP_HOME
# Install production dependencies.
RUN pip install Flask gunicorn
ENV PORT=8080
COPY . .

# Run the web service on container startup. Here we use the gunicorn webserver
CMD ["sh", "-c", "exec gunicorn --bind :$PORT app:app"]