FROM ubuntu:14.04

#-- packages --#
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update
RUN apt-get update &&\
    apt-get -y upgrade &&\
    apt-get --no-install-recommends -y install python-qt4 libqt4-webkit xvfb python-pip python-dev git-core libqt4-dev libxtst-dev xvfb libicu52 wget libjpeg-dev zlib1g-dev gcc

#-- setup structure --#
RUN mkdir -p /workspace

#-- install phantomjs --#
WORKDIR /usr/bin
RUN wget https://github.com/Pyppe/phantomjs2.0-ubuntu14.04x64/raw/master/bin/phantomjs
RUN chmod 0755 phantomjs

#-- setup gom-backend--#
COPY . /workspace/py-webkit2png-flask-api
WORKDIR /workspace/py-webkit2png-flask-api
RUN pip install -r requirements.txt
RUN ./manage init

CMD /workspace/py-webkit2png-flask-api/manage run