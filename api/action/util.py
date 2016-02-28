import time
import datetime
import uuid

import os


def unserialize_json_datetime(json_str):
    return datetime.datetime.fromtimestamp(float(json_str))


def serialize_json_datetime(datetime_obj):
    if datetime_obj is not None:
        return time.mktime(datetime_obj.timetuple())
    return None

def generate_uuid():
    return str(uuid.uuid1())

def run_cmd_lis(cmd_lis):
    full_cmd = " && ".join(cmd_lis)
    os.system(full_cmd)
