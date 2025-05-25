import logging
from pathlib import Path
from time import gmtime

from python_pipeline.lib import find_variance, read_xlsx


class App:
    """
    Main process for python_pipeline
    """

    def __init__(self) -> None:
        self.logger = logging.getLogger("python_pipeline")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s.%(name)s.%(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S UTC",
        )
        formatter.converter = gmtime
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info("App initialised.")

    def run(self, raw_path: str) -> None:
        """
        Process one file.
        """
        path = Path(raw_path)
        self.logger.info(f"Reading {path}")
        frames = read_xlsx(path)
        self.logger.info(f"Calculating variance")
        result = find_variance(frames)
        out_path = f"{path.stem}.variance.xlsx"
        self.logger.info(f"Writing {out_path}")
        result.to_excel(out_path, sheet_name="variance", float_format="%.2f")
        self.logger.info("Finished.")
