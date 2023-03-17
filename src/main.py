import os, json, re

import supervisely as sly
from dotenv import load_dotenv


if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

team_id = sly.env.team_id()

input_folder = sly.env.folder(raise_not_found=False)
# input_file = sly.env.file(raise_not_found=False)
input_file = sly.env.file(raise_not_found=False)


default_path = sly.app.get_synced_data_dir()

if not input_file is None:
    sly.logger.info(f"App is started from file context menu in TeamFiles: {input_file}")

    input_folder = os.path.dirname(input_file)
    ext = '.' + os.path.basename(input_file).split('.')[2]

    if ext != '.tfevents':
        sly.logger.warn(
            f"{os.path.basename(input_file)} is not a file with appropriate Tensorboard log extension. Searching for files containing '.tfevents' in the parent folder instead: {default_path}"
        )
    else:
        sly.logger.warn(
            f"{os.path.basename(input_file)} has an appropriate Tensorboard log extension. Searching for files containing '.tfevents' in the parent folder: {default_path}"
        )

    api = sly.Api()
    api.file.download_directory(team_id, remote_path=input_folder, local_save_path=default_path)


else:
    sly.logger.info(f"App is started from folder context menu in TeamFiles: {input_folder}")
    # default_path = sly.app.get_synced_data_dir()

    api = sly.Api()
    api.file.download_directory(team_id, remote_path=input_folder, local_save_path=default_path)
    # default_url = os.path.join(default_path, "/logs")
    # default_path = default_path


sly.logger.info(f"Default path: {default_path}")
with open("default_path.txt", "w") as text_file:
    text_file.write(default_path)

