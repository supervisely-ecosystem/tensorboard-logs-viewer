# !/bin/bash

# set_shell_env() {
#     output=$(python3 src/export_env.py)
#     eval $output
# }
# set_shell_env

# echo prID is: $PROJECT_ID && \
# echo prName is: $PROJECT_NAME && \

# python3 typer_commands.py download ${PROJECT_ID} src/download/ && \

# echo "$(pwd)" && \
# echo Root:
# echo "$(ls)" && \
# echo "$(cd src/ && ls)" && \
# echo "$(cd src/download/ds1/img && ls)" && \

# nohup tensorboard &> output & sleep 5 &
# python script.py &

echo "$(pwd)"
echo "$(ls)"

# echo $CONTEXT_SLYFOLDER
# echo $CONTEXT_SLYFILE
# echo $FILE
# echo $FOLDER
# echo $SLYFOLDER
# echo $SLYFILE

python3 src/main.py && \
LOGDIR_PATH=`cat logdir_path.txt` && \
echo "Logs directory url: " $LOGDIR_PATH && \

tensorboard --logdir $LOGDIR_PATH --port 8000  --host 0.0.0.0 --reload_multifile=true --load_fast=false --path_prefix=$BASE_URL 

# python3 src/customers_main.py src/download/ds1/img src/artefacts/ && \

# python3 typer_commands.py upload-directory ${TEAM_ID} src/artefacts/ /uploaddir/${TASK_ID}-${PROJECT_NAME}-${PROJECT_ID}/ && \
# python3 typer_commands.py set-task-output-dir ${TASK_ID} /uploaddir/${TASK_ID}-${PROJECT_NAME}-${PROJECT_ID}/
