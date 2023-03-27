# !/bin/bash

python3 src/main.py && \
echo "Directory with tensorboard metrics: /tmp" && \
tensorboard --logdir "/tmp" --port 8000  --host 0.0.0.0 --reload_multifile=true --load_fast=false --path_prefix=$BASE_URL 
