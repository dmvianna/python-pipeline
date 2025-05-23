# conftest.py
# pytest makes fixtures magically available as arguments to functions
# in other modules.

import sys
from pathlib import Path

import pytest

root = Path(__file__).parent.parent
sys.path.append(repr(root))


@pytest.fixture
def example() -> Path:
    """
    Example file.
    """
    return Path("tests/fixtures/Sample Super Data.xlsx")
