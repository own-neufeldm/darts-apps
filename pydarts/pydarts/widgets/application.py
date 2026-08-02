from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import pydarts
from pydarts.widgets.main_window import MainWindow


class Application(QApplication):
    def __init__(self, args: list[str]) -> None:
        super().__init__(args)
        self.setApplicationName("pydarts")
        self.setApplicationDisplayName("PyDarts")
        try:
            self.setApplicationVersion(pydarts.__version__)
        except AttributeError:
            # workaround for portable exe
            pass
        self.setWindowIcon(QIcon(pydarts.package_dir.joinpath("icons/darts.ico").as_posix()))
        # set taskbar icon in Windows
        try:
            from ctypes import windll
            app_id = "shyguys.pydarts"
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        except ImportError:
            # not on Windows, fine
            pass
        self.main_window: MainWindow
        self._load_main_window()
        return None

    def _load_main_window(self) -> None:
        self.main_window = MainWindow()
        self.main_window.finished_exit.connect(self.quit)
        return None
