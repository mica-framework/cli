FROM debian:stretch-slim
LABEL maintainer="zinklandi@gmail.com"

# first update and install the dependencies
RUN apt-get update -y && apt-get upgrade -y && \
  apt-get install -y python3 python3-pip

# Now get the files
RUN mkdir -p /app && mkdir -p /app/server && \
  mkdir -p /app/client && mkdir -p /app/config && \
  mkdir -p /app/installer && mkdir -p /app/manager/
COPY ./mica-cli.py /app/mica-cli.py
COPY ./requirements.txt /app/requirements.txt
COPY ./questions.* /app/
COPY ./config.yml /app/config.yml
COPY ./config/*.py /app/config/
COPY ./server/*.py /app/server/
COPY ./installer/*.py /app/installer/
COPY ./client/*.py /app/client/
COPY ./manager/*.py /app/manager/

# now install all dependencies of the client
WORKDIR /app
RUN pip3 install -r requirements.txt

# Define Entrypoint
CMD [ "python3", "mica-cli.py" ]