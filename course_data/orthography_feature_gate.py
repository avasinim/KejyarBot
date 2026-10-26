"""Explicit opt-in gate for the draft orthography course.

The draft course stays unavailable unless the environment setting is exactly
"true" (case-insensitive, whitespace ignored). This module has no bot side
effects and does not change the legacy course.
"""
from __future__ import annotations

import os
from collections.abc import Mapping

ENV_KEY = "KEJYAR_ENABLE_ORTHOGRAPHY_FOUNDATIONS"


def is_orthography_course_enabled(environ: Mapping[str, str] | None = None) -> bool:
    """Return True only when the dedicated draft-course flag is explicitly enabled."""
    source = os.environ if environ is None else environ
    return source.get(ENV_KEY, "").strip().lower() == "true"
