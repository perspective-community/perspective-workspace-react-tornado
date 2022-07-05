import os
import os.path

from perspective import PerspectiveManager, PerspectiveTornadoHandler
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler


class DebugStaticFileHandler(StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


def get_tables():
    return {}


def get_table_manager():
    manager = PerspectiveManager()
    for name, table in get_tables().items():
        manager.host_table(name, table)
    return manager


def build_application():
    table_manager = get_table_manager()

    handlers = [
        (
            r"/websocket",
            PerspectiveTornadoHandler,
            {"manager": table_manager, "check_origin": True},
        ),
        (
            r"/(.*)",
            DebugStaticFileHandler,
            {
                "path": os.path.join(os.path.dirname(__file__), "static"),
                "default_filename": "index.html",
            },
        ),
    ]
    application = Application(handlers, serve_traceback=True)
    return application


def main():
    app = build_application()
    app.listen(8080)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
