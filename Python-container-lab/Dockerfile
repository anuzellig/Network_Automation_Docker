# TASK 1: Base your image on the ubuntu:bionic image
FROM ubuntu:bionic

# I've provided the commands to install all the binaries here
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-distutils python3-dev build-essential curl wget net-tools iputils-ping iproute2 openssh-client telnet software-properties-common tree vim \
    && curl -s https://bootstrap.pypa.io/get-pip.py | python3 \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir /home/python

# TASK 2: Make the /home/python directory we just created the new default directory for commands

# TASK 3: Copy requirements.txt into the container, and issue 'pip3 install -r requirements.txt'

# TASK 4: Copy the python script into the container

# Question: Why are we breaking tasks 2 and 3 into seperate commands rather than a single command? What are the pros and cons of this approach? 