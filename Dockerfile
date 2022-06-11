FROM ubuntu:22.04
RUN apt update && apt -y upgrade
RUN apt install git python3 python3-pip

RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

RUN WORKDIR /root
RUN git clone https://github.com/Voldemort175/RESTapi.git
RUN WORKDIR /RESTapi

EXPOSE 8080
CMD ["uvicorn", "main:app","--reload"]