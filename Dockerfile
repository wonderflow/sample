FROM mcr.microsoft.com/cbl-mariner/base/python:3

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