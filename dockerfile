# dockerfiles/prod/django/Dockerfile

# pull official base image
FROM python:3.9-slim


# set work directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt


# Set up Gunicorn
COPY . /app

# Install Nginx
RUN apt-get update && apt-get install -y nginx



# Configure Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# exposing nginx port
EXPOSE 80


# copy entrypoint
COPY entrypoint.sh .

# make our entrypoint.sh executable
RUN chmod +x ./entrypoint.sh

# execute our entrypoint.sh file
CMD ["./entrypoint.sh"]