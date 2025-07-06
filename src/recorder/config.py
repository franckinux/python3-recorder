import logging
from pathlib import Path
import tomllib

from recorder.typem import GeneralConfig

general = None

loggers = {}

_module = []


def read(config_filename: str):
    config_file = Path(config_filename)
    with open(config_file, "rb") as f:
        raw_config = tomllib.load(f)

    global general
    general = GeneralConfig(**raw_config["general"])

    global loggers
    loggers = raw_config["logger"]
