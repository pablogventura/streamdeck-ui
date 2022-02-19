import sys
from unittest.mock import MagicMock

import pytest
from hypothesis_auto import auto_pytest_magic

from streamdeck_ui import api, gui

pytestmark = pytest.mark.skipif(sys.platform == "linux", reason="tests for mac only due to travis issues")

gui.selected_button = MagicMock()

auto_pytest_magic(gui.update_button_text, ui=MagicMock())
auto_pytest_magic(gui.update_button_command, ui=MagicMock())
auto_pytest_magic(gui.update_button_keys, ui=MagicMock())
auto_pytest_magic(gui.update_button_write, ui=MagicMock())
auto_pytest_magic(gui.update_change_brightness, ui=MagicMock())
auto_pytest_magic(gui.change_page, ui=MagicMock())
auto_pytest_magic(gui.set_brightness, ui=MagicMock(), auto_allow_exceptions_=(KeyError,))
auto_pytest_magic(gui.queue_update_button_text, ui=MagicMock())


def test_start():
    api.decks = {None: MagicMock()}
    gui.start(_exit=True)
