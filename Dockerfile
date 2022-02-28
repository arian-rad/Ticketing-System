FROM python:alpine
# set a system user with limited privilages
RUN addgroup code && adduser -S -G code code

# install postgresql dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# expose port
EXPOSE 8000

# create and change the working directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/