import logging
from pathlib import Path
from time import gmtime


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

    def run(self, path: Path) -> None:
        """
        Process one file.
        """
        self.logger.info(f"Processing {path}")
        # do stuff
        # finished doing stuff
        self.logger.info("Finished.")
