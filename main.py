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


async def logic_process(signals):
    from asyncio import wait_for
    from asyncio import TimeoutError
    from asyncio import sleep
    while True:
        try:
            event = await wait_for(signals.get(), 10)
            print(repr(event), flush=True)
            signals.task_done()
        except TimeoutError:
            print('no signals', flush=True)


async def ping():
    from asyncio import sleep
    while True:
        print('.', end='', flush=True)
        await sleep(1)


def application_live(loop, signals):
    from asyncio import set_event_loop
    set_event_loop(loop)
    pinging = loop.create_task(ping())
    processing = loop.create_task(logic_process(signals))
    try:
        loop.run_forever()
    finally:
        pinging.cancel()
        processing.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    from asyncio import new_event_loop, Queue
    loop = new_event_loop()
    signals = Queue(loop=loop)
    live = Thread(name='live', target=application_live, args=(loop, signals,))
    live.start()

    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    root = Path(__file__).absolute().parent

    application_state = ApplicationState(url='postgres://')
    application_state.connectDB.connect(lambda url: loop.call_soon_threadsafe(signals.put_nowait, ('connectDB', url)))

    application = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    context.setContextProperty('application_state', application_state)
    engine.load(QUrl.fromLocalFile(str(root/'markup'/'main.qml')))
    window = engine.rootObjects()[0]
    window.show()

    status = application.exec_()
    loop.call_soon_threadsafe(loop.stop)
    live.join()
    sys.exit(status)
