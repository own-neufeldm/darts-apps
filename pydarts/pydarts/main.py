import sys

from PySide6.QtCore import QCommandLineOption, QCommandLineParser

import pydarts
from pydarts.widgets.application import Application


def parse(app: Application) -> None:
    parser = QCommandLineParser()
    parser.addHelpOption()
    version_option = QCommandLineOption(
        ["v", "version"],
        "Show version and exit.",
    )
    parser.addOption(version_option)
    debug_option = QCommandLineOption(
        ["d", "debug"],
        "Write debug messages to stdout.",
    )
    parser.addOption(debug_option)
    parser.process(app)
    pydarts.configure_logging(parser.isSet(debug_option))
    if parser.isSet(version_option):
        print(pydarts.__version__)
        sys.exit()
    return None


def main() -> None:
    app = Application(sys.argv)
    parse(app)
    app.exec()
    return None


if __name__ == "__main__":
    main()
