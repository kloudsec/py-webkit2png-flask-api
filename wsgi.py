import sys, os

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)

from api.web import app
application = app