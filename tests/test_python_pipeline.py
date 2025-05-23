from dataclasses import asdict

import pandas as pd
from python_pipeline.lib import read_xlsx


class TestRead:
    def test_read_xlsx(self, example):
        """
        Read a file that has the expected sheet names.
        """
        frames = read_xlsx(example)
        for value in asdict(frames).values():
            assert isinstance(value, pd.DataFrame)
