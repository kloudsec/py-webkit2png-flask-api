from api.action import util
from cfg import RESOURCES_FOLDER_PATH
from cherrypy import wsgiserver
from manager import Manager


manager = Manager()


@manager.command
def init():
    util.run_cmd_lis([
        "mkdir -p %s" % (RESOURCES_FOLDER_PATH),
    ])


@manager.command
def build():
    util.run_cmd_lis([
        'docker build -t nubelacorp/py-webkit2png-flask-api .',
    ])


@manager.command
def run():
    from api.web import app
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


@manager.command
def run_docker():
    util.run_cmd_lis([
        'docker run -p 8080:8080 -it nubelacorp/py-webkit2png-flask-api',
    ])


@manager.command
def run_standalone():
    util.run_cmd_lis([
        'gunicorn -c resources/gunicorn-conf.py backend_wsgi',
    ])

if __name__ == '__main__':
    manager.main()
