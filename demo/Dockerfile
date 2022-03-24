# pull official base image
FROM python:3.7.3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run development server
CMD python manage.py runserver 0.0.0.0:$PORT