import os


MAX_FILES_IN_FOLDER = 100
CWD = os.path.dirname(os.path.realpath(__file__))
RESOURCES_FOLDER_PATH = os.path.join(CWD, "resources")
ASSETS_FOLDER_PATH = os.path.join(CWD, "assets")
DEFAULT_IMAGE_PLACEHOLDER = os.path.join(ASSETS_FOLDER_PATH, "default_placeholder.png")
USE_XVFB = True
WEBKIT2PNG_PATH = "/workspace/python-webkit2png/webkit2png"
SMART_LOAD_LOAD_SECS = 2
