import multiprocessing

import os



bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() + 1
preload = True

CWD = os.path.dirname(os.path.realpath(__file__))
errorlog = os.path.join(CWD, "gunicorn_error.log")
