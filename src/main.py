import os
import supervisely as sly
from dotenv import load_dotenv

metrics_dir = "/tmp"
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))
    metrics_dir = sly.app.get_data_dir()

team_id = sly.env.team_id()
remote_folder = sly.env.folder(raise_not_found=False)
remote_file = sly.env.file(raise_not_found=False)

api = sly.Api.from_env()

if remote_file is not None:
    name = sly.fs.get_file_name_with_ext(remote_file)
    if ".tfevents." not in name:
        raise KeyError(
            f'Extension ".tfevents." not found. File {remote_file} is not metrics for Tensorboard.'
        )
    local_file = os.path.join(metrics_dir, name)
    api.file.download(team_id, remote_file, local_file)
elif remote_folder is not None:
    if remote_folder == "/":
        raise KeyError("Permission denied. It is not safe to run app the root directory")
    print(f"Directory to download: {remote_folder}")
    sizeb = api.file.get_directory_size(team_id, remote_folder)
    progress = sly.Progress(
        f"Downloading metrics from {remote_folder}", total_cnt=sizeb, is_size=True
    )
    api.file.download_directory(team_id, remote_folder, metrics_dir, progress.iters_done_report)
