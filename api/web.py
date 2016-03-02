import json
import time

from PIL import Image
from api.action import util
from flask.helpers import send_file
from selenium import webdriver
from api.app import app
from cfg import RESOURCES_FOLDER_PATH, DEFAULT_IMAGE_PLACEHOLDER, SMART_LOAD_LOAD_SECS
from flask import request, jsonify
import os
from slugify import slugify


def is_0byte(file_path):
    return os.stat(file_path).st_size == 0


def is_all_white(file_path):
    img = Image.open(file_path)
    return sum(img.convert("L").getextrema()) in (0, 2)


def get_screenshot():
    url = request.args.get("url", None)
    width = int(request.args.get("width", 400))
    height = int(request.args.get("height", 400))
    scale = float(request.args.get("scale", 0.5))
    timeout = int(request.args.get("timeout", -1))
    is_smart_load = timeout == -1
    file_name = "%s.png" % (util.generate_uuid())
    file_path = os.path.join(RESOURCES_FOLDER_PATH, file_name)
    x_width = int(width / scale)
    x_height = int(height / scale)

    params = {
        'url': url,
        'width': width,
        'height': height,
        'scale': scale,
    }

    cache_filename = slugify(json.dumps(params))
    cache_filepath = os.path.join(RESOURCES_FOLDER_PATH, '%s.png' % (cache_filename))
    if os.path.exists(cache_filepath):
        return send_file(cache_filepath, mimetype='image/png')

    driver = webdriver.PhantomJS()
    driver.set_window_size(x_width, x_height)
    driver.set_page_load_timeout(0)

    try:
        driver.get(url)
    except:
        if is_smart_load:
            while True:
                time.sleep(0.5)
                driver.get_screenshot_as_file(file_path)
                if is_0byte(file_path) or is_all_white(file_path):
                    continue
                else:
                    time.sleep(SMART_LOAD_LOAD_SECS)
                    driver.get_screenshot_as_file(file_path)
                    break
        else:
            time.sleep(timeout)
            driver.get_screenshot_as_file(file_path)
    finally:
        driver.quit()

    if is_0byte(file_path):
        return send_file(DEFAULT_IMAGE_PLACEHOLDER, mimetype='image/png')

    if is_all_white(file_path):
        return send_file(DEFAULT_IMAGE_PLACEHOLDER, mimetype='image/png')

    # crop image
    img = Image.open(file_path)
    worked_image = img.crop((0, 0, x_width, x_height))
    worked_image = worked_image.resize((width, height), Image.ANTIALIAS)
    worked_image.save(cache_filepath)

    return send_file(cache_filepath, mimetype='image/png')


def ping():
    return jsonify({'status': 'ok'})


app.add_url_rule('/ping',
                 "ping", ping, methods=['GET'])

app.add_url_rule('/',
                 "index", get_screenshot, methods=['GET'])
