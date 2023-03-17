FROM tensorflow/tensorflow

USER root

WORKDIR /sly-app-data

COPY /src /repo/src
COPY /run.sh /repo/run.sh