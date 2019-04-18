# nso-container

FROM ubuntu:bionic

WORKDIR /
COPY nso-4.7.linux.x86_64.installer.bin .

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential wget net-tools iputils-ping iproute2 openssh-client software-properties-common tree vim python libxml2-utils default-jre-headless \
    && rm -rf /var/lib/apt/lists/* \
    # Install NSO
    && sh nso-4.7.linux.x86_64.installer.bin /opt/ncs \
    && rm nso-4.7.linux.x86_64.installer.bin \
    && printf "\nsource /opt/ncs/ncsrc\n" >> ~/.bashrc
