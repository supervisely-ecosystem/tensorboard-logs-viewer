FROM tensorflow/tensorflow:2.12.0

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install supervisely==6.70.13

COPY /src /repo/src
COPY /run.sh /repo/run.sh