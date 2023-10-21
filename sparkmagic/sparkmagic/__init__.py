__version__ = "0.21.2"

from sparkmagic.serverextension.handlers import (
    load_jupyter_server_extension,
)  # noqa: #501


def _jupyter_server_extension_paths():
    return [{"module": "sparkmagic"}]


def _jupyter_nbextension_paths():
    return []
