"""Anki add-on exposing CM/CB/CS notes."""

from __future__ import annotations

import os
from typing import Optional

from aqt import mw
from aqt.qt import QAction
from aqt.utils import qconnect, showText, showWarning


def _notes_path() -> str:
    """Return the path to the bundled notes file."""
    return os.path.join(os.path.dirname(__file__), "data", "cm_cb_and_cs_notes.txt")


def _load_notes() -> Optional[str]:
    """Read the notes file, returning None if it can not be loaded."""
    try:
        with open(_notes_path(), "r", encoding="utf-8") as handle:
            return handle.read()
    except OSError as err:
        showWarning(f"Unable to load CM/CB/CS notes: {err}")
        return None


def show_cm_cb_cs_notes() -> None:
    """Display the bundled notes in Anki's text viewer."""
    notes = _load_notes()
    if notes is None:
        return

    showText(
        notes,
        title="CM/CB/CS Reference Notes",
        plain_text=True,
    )


def _setup_menu_entry() -> None:
    action = QAction("CM/CB/CS Notes", mw)
    qconnect(action.triggered, show_cm_cb_cs_notes)
    mw.form.menuTools.addAction(action)


_setup_menu_entry()
