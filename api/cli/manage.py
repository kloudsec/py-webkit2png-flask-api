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
    from api.web import app
    d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
    host = '0.0.0.0'
    port = 8080
    server = wsgiserver.CherryPyWSGIServer((host, port), d, numthreads=10, timeout=30, request_queue_size=100)

    if __name__ == '__main__':
        try:
            print "Server started on http://%s:%d" % (host, port)
            server.start()
        except KeyboardInterrupt:
            server.stop()


if __name__ == '__main__':
    manager.main()
