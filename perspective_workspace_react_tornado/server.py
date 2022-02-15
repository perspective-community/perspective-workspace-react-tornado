import logging
import os
import os.path
import sys

from perspective import PerspectiveTornadoHandler
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler

from .tables import get_table_manager


# This is a helper wrapper around StaticFileHandler
# to not cache files, so we can pickup our JS
# changes as they happen
class DebugStaticFileHandler(StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


def build_application():
    # Grab perspective manager
    table_manager = get_table_manager()

    # setup 2 handlers, one for the perspective manager's websocket
    # and one for the static assets (react project)
    handlers = [
        (
            r"/websocket",
            PerspectiveTornadoHandler,
            {"manager": table_manager, "check_origin": True},
        ),
        (
            r"/(.*)",
            # User the debug handler if we're watching for file changes
            DebugStaticFileHandler if "--watch" in sys.argv else StaticFileHandler,
            {
                "path": os.path.join(os.path.dirname(__file__), "static"),
                "default_filename": "index.html",
            },
        ),
    ]

    # instantiate the application, turning debug on if necessary
    application = Application(
        handlers, serve_traceback=True, debug="--watch" in sys.argv
    )
    return application


def main():
    # build the application
    app = build_application()

    # listen and log the port
    app.listen(8080)
    logging.warn("Listening on http://localhost:8080")

    # launch
    IOLoop.instance().start()
