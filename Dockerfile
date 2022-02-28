FROM devkitpro/devkitarm

MAINTAINER Pk11 <epicpkmn11@outlook.com>

RUN echo deb http://deb.debian.org/debian stable main contrib non-free >> /etc/apt/sources.list && \
    sudo apt-get update && \
    sudo apt-get install python3-pip -y && \
    pip3 install -r source/requirements.txt
