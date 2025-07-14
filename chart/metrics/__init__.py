"""Chart metrics package."""

from . import angular  # noqa: F401 - register metric classes
from . import aspects  # noqa: F401 - register metric classes
from . import rulership  # noqa: F401 - register metric classes
from . import dignities  # noqa: F401 - register metric classes
from . import strength  # noqa: F401 - register metric classes
from .base import compute_all

__all__ = ["compute_all"]
