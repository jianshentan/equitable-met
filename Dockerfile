FROM python:3.4-slim
MAINTAINER JS Tan "jianshentan@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential && \
    # install sass
    apt-get install -y ruby-full rubygems && \
    gem install bundler && \
    gem install sass

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

EXPOSE 8080 80 443
ENTRYPOINT ["python"]
CMD ["application.py"]
