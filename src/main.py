import os, json, re

import supervisely as sly
from dotenv import load_dotenv


def strip_with_replacement(text, replacement):
    return re.sub(r'\s+', replacement, text)

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


api: sly.Api = sly.Api.from_env()


folder = sly.env.folder()
env_file = sly.env.file()




