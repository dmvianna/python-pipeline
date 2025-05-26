from dataclasses import asdict

import pandas as pd
import pytest
from python_pipeline.lib import (
    SheetNameError,
    calculate_disbursement,
    payable_super,
    read_xlsx,
    select_ordinary,
)


class TestRead:
    def test_read_xlsx(self, example):
        """
        Read a file that has the expected sheet names.
        """
        frames = read_xlsx(example)
        for value in asdict(frames).values():
            assert isinstance(value, pd.DataFrame)

    def test_read_empty_xlsx(self, empty):
        """
        Fail a file with missing sheets.
        """
        with pytest.raises(SheetNameError):
            frames = read_xlsx(empty)
            print(frames)


class TestTransform:
    def test_select_ordinary(self, frames):
        """
        Select only ordinary payments.
        """
        ordinary = select_ordinary(frames)
        print(ordinary)
        assert ordinary.payslips.shape[0] == 1

    def test_disbursement_deadline(self):
        """
        Create column with last date of quarter + 28 days.
        """
        payslips = pd.DataFrame.from_dict(
            {
                "payslip_id": [0],
                "employee_code": [0],
                "amount": [0],
                "end": [pd.Timestamp("1/14/2018")],
            }
        )

        super = payable_super(payslips)
        deadlines = calculate_disbursement(super, "end")

        assert deadlines.loc[0, "disbursement_due"] == pd.Timestamp(
            "2018-04-28 23:59:59.999999999"
        )
