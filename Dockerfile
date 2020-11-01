ARG TAG=latest
FROM ubuntu:$TAG

RUN apt-get update && apt-get install -y \
    git \
    wget \
    nano \
    python3 \
    python3-pip \
    libncurses5

ARG NRFTOOLS=nRF-command-line-tools/sw/Versions-10-x-x/10-10-0-v2/nRFCommandLineTools10100Linuxamd64tar.gz
RUN wget https://www.nordicsemi.com/-/media/Software-and-other-downloads/Desktop-software/$NRFTOOLS
RUN tar zxvf *.gz \
    && dpkg -i nRF-Command-Line-Tools*.deb \
    && dpkg -i JLink*.deb

RUN git clone https://github.com/ryanjh/pylink.git -b test_remote_server

RUN git clone https://github.com/ryanjh/pynrfjprog.git -b remote_server
