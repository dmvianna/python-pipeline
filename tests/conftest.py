# conftest.py
# pytest makes fixtures magically available as arguments to functions
# in other modules.
import sys
from pathlib import Path

import pandas as pd
import pytest
from python_pipeline.lib import Frames

root = Path(__file__).parent.parent
sys.path.append(repr(root))


@pytest.fixture
def example() -> Path:
    """
    Example file.
    """
    return Path("tests/fixtures/Sample Super Data.xlsx")


@pytest.fixture
def empty() -> Path:
    """
    Empty file.
    """
    return Path("tests/fixtures/empty.xlsx")


@pytest.fixture
def frames() -> Frames:
    """
    Minimal Frames.
    """
    disbursements = {}
    payslips = {
        "payslip_id": [1, 2],
        "end": ["1/14/2018", "1/14/2018"],
        "employee_code": [1, 1],
        "code": [1, 2],
        "amount": [10, 20],
    }
    paycodes = {"pay_code": [1, 2], "ote_treatment": ["OTE", "Not OTE"]}

    frame_dict = {
        k: pd.DataFrame.from_dict(sheet)
        for k, sheet in {
            "disbursements": disbursements,
            "payslips": payslips,
            "paycodes": paycodes,
        }.items()
    }
    return Frames(**frame_dict)
