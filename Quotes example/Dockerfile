FROM ubuntu:bionic

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install fortune-mod fortunes cowsay

ENTRYPOINT /usr/games/fortune computers | /usr/games/cowsay
