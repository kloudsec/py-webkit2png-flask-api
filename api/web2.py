import datetime

from api.app import app
from api.action import util
from cfg import RESOURCES_FOLDER_PATH, DEFAULT_IMAGE_PLACEHOLDER, USE_XVFB, WEBKIT2PNG_PATH
from flask import request, send_file
import os


def get_screenshot():
    width = request.args.get("w", 400)
    height = request.args.get("h", 400)
    scale = request.args.get("scale", 0.5)
    url = request.args.get("url", None)

    if url is None:
        return send_file(DEFAULT_IMAGE_PLACEHOLDER, mimetype='image/png')

    filename = util.generate_uuid()
    params = {
        'width': width,
        'height': height,
        'scale': scale,
        'scaled_width': int(width * scale),
        'scaled_height': int(height * scale),
        'url': url,
        'filename': filename,
        'output_folder': RESOURCES_FOLDER_PATH,
        'output_file': os.path.join(RESOURCES_FOLDER_PATH, '%s.png' % filename),
        'webkit_2_png_path': WEBKIT2PNG_PATH,
    }

    print params

    if USE_XVFB:
        util.run_cmd_lis([
            'xvfb-run --server-args="-screen 0, 1024x768x24" python %(webkit_2_png_path)s/scripts.py -x %(width)d %(height)d --aspect-ratio=crop --scale=%(scaled_width)d %(scaled_height)d -o %(output_file)s %(url)s' % (params),
        ])
    else:
        util.run_cmd_lis([
            "webkit2png -W %(width)d --clipheight=%(scaled_height)d -s %(scale)f %(url)s -D %(output_folder)s -o %(filename)d" % (params),
        ])

    file_name = os.path.join(RESOURCES_FOLDER_PATH, "%s-clipped.png" % params['filename']) if not USE_XVFB else params['output_file']
    if os.path.exists(file_name):
        return send_file(file_name, mimetype='image/png')

    return send_file(DEFAULT_IMAGE_PLACEHOLDER, mimetype='image/png')


app.add_url_rule('/',
                 "index", get_screenshot, methods=['GET'])
