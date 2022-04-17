FROM ubuntu:jammy-20220404

RUN apt update
RUN yes | apt upgrade
RUN yes | apt install python3.10
RUN yes | apt install python3-pip=22.0.2+dfsg-1
RUN yes | pip install pandas==1.4.2
RUN yes | pip install scikit-learn==1.0.2
RUN yes | pip install Flask==2.1.1
RUN yes | pip install flask-restful==0.3.9
#RUN yes | apt install libpython2.7-stdlib # for import json