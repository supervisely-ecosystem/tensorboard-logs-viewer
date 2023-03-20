import os

import supervisely as sly
from dotenv import load_dotenv


if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

team_id = sly.env.team_id()

input_folder = sly.env.folder(raise_not_found=False)
input_file = sly.env.file(raise_not_found=False)


logdir_path = sly.app.get_synced_data_dir()

if not input_file is None:
    sly.logger.info(f"App is started from file context menu in TeamFiles: {input_file}")

    input_folder = os.path.dirname(input_file)
    ext = '.' + os.path.basename(input_file).split('.')[2]

    if ext != '.tfevents':
        sly.logger.warn(
            f"{os.path.basename(input_file)} is not a file with appropriate Tensorboard logs extension. Searching for files containing '.tfevents' in the parent folder instead: '{input_folder}'"
        )
    else:
        sly.logger.warn(
            f"{os.path.basename(input_file)} has an appropriate Tensorboard log extension. Searching for files containing '.tfevents' in the parent folder: {input_folder}"
        )

    api = sly.Api()
    api.file.download_directory(team_id, remote_path=input_folder, local_save_path=logdir_path)


else:
    sly.logger.info(f"App is started from folder context menu in TeamFiles: '{input_folder}'")

    api = sly.Api()
    api.file.download_directory(team_id, remote_path=input_folder, local_save_path=logdir_path)


with open("logdir_path.txt", "w") as text_file:
    text_file.write(logdir_path)

