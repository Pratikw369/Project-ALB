import os
import json

# Locate project root (this file is at root)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Path to the config file
CONFIG_FILE = os.path.join(PROJECT_ROOT, "config.json")

# Load once
with open(CONFIG_FILE) as f:
    _CONFIG = json.load(f)

def get_path(key: str) -> str:
    """
    Returns the absolute path for a given key from paths.json.
    """
    if key not in _CONFIG:
        raise KeyError(f"Key '{key}' not found in config file.")
    
    return os.path.join(PROJECT_ROOT, _CONFIG[key])
