from dataclasses import asdict

import pandas as pd
import pytest
from python_pipeline.lib import SheetNameError, read_xlsx


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
