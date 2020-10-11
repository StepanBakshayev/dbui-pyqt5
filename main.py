from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject, QUrl
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine

from threading import Thread
from pathlib import Path
import sys


class ApplicationState(QObject):
    urlChanged = pyqtSignal()

    @pyqtProperty(str, notify=urlChanged)
    def url(self):
        return self.url_

    @url.setter
    def url(self, url):
        if self.url_ != url:
            self.url_ = url
            self.urlChanged.emit()

    connectDB = pyqtSignal(str)

    def __init__(self, url='', parent=None):
        super().__init__(parent)

        self.url_ = url


async def login_process():
    from asyncio import sleep
    import sys
    while True:
        print('.', end='')
        sys.stdout.flush()
        await sleep(1)


def application_live():
    from asyncio import new_event_loop
    loop = new_event_loop()
    loop.run_until_complete(login_process())


if __name__ == '__main__':
    live = Thread(name='live', target=application_live)
    live.start()

    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    root = Path(__file__).absolute().parent

    application_state = ApplicationState(url='postgres://')
    application_state.connectDB.connect(lambda url: print('connecting...', url))

    application = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    context.setContextProperty('application_state', application_state)
    engine.load(QUrl.fromLocalFile(str(root/'markup'/'main.qml')))
    window = engine.rootObjects()[0]
    window.show()

    sys.exit(application.exec_())
