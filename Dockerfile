FROM tensorboard/tensorboard:2.12.0


WORKDIR /sly-app-data

COPY /src /repo/src
COPY /run.sh /repo/run.sh