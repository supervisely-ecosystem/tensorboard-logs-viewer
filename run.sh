# !/bin/bash

python3 src/main.py && \
LOGDIR_PATH=`cat logdir_path.txt` && \
echo "Logs directory url: " $LOGDIR_PATH && \

tensorboard --logdir $LOGDIR_PATH --port 8000  --host 0.0.0.0 --reload_multifile=true --load_fast=false --path_prefix=$BASE_URL 
