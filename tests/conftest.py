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


@pytest.fixture
def example_frames() -> Frames:
    """
    Frames using case where the correct response is known.
    """
    disbursements = {
        "sgc_amount": [500, 500, 500],
        "payment_made": map(pd.Timestamp, ["2025-2-17", "2025-3-30", "2025-4-30"]),
        "pay_period_from": ["", "", ""],
        "pay_period_to": ["", "", ""],
        "employee_code": [0, 0, 0],
    }
    payslips = {
        "payslip_id": [1, 1, 1, 2, 2, 3, 3],
        "end": map(
            pd.Timestamp,
            [
                "2025-01-01",
                "2025-01-01",
                "2025-01-01",
                "2025-02-01",
                "2025-02-01",
                "2025-03-01",
                "2025-03-01",
            ],
        ),
        "employee_code": [0, 0, 0, 0, 0, 0, 0],
        "code": ["Salary", "Overtime", "Super", "Salary", "Super", "Salary", "Super"],
        "amount": [5000, 1500, 475, 5000, 475, 5000, 475],
    }
    paycodes = {
        "pay_code": ["Salary", "Overtime", "Super"],
        "ote_treatment": ["OTE", "Not OTE", "Not OTE"],
    }

    frame_dict = {
        k: pd.DataFrame.from_dict(sheet)
        for k, sheet in {
            "disbursements": disbursements,
            "payslips": payslips,
            "paycodes": paycodes,
        }.items()
    }
    return Frames(**frame_dict)
