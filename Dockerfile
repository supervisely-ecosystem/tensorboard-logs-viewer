FROM tensorboard/tensorboard:2.12.0

RUN pip install supervisely==6.70.13

COPY /src /repo/src
COPY /run.sh /repo/run.sh