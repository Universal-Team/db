FROM devkitpro/devkitarm

MAINTAINER Pk11 <epicpkmn11@outlook.com>

RUN echo deb http://deb.debian.org/debian stable main contrib non-free >> /etc/apt/sources.list && \
    sudo apt-get update && \
    sudo apt-get install python3-pip -y && \
    pip3 install markdownify==0.9.0 numpy==1.21.0 Pillow==9.0.0 python-dateutil==2.8.1 PyYAML==5.4.1 qrcode==6.1 requests==2.25.1 Unidecode==1.3.4
