import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json data saved to: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r") as f:
        data = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary data saved to: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename=path)
    logger.info(f"Binary data loaded successfully from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    return round(os.path.getsize(path) / 1024)


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImage(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
