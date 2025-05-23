from dataclasses import asdict

import pandas as pd
import pytest
from python_pipeline.lib import SheetNameError, read_xlsx, select_ordinary


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
