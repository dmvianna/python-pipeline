"""python-pipeline -- Check payroll compliance

Usage:
  python-pipeline <path>
  python-pipeline (-h | --help)
  python-pipeline --version

Options:
  -h --help                    Show this screen
  --version                    Show version
  <path>                       Path to XLSX file
"""

from docopt import docopt

from python_pipeline.app import App


def main() -> None:
    args = docopt(__doc__, version="python-pipeline 1.0")

    a = App()

    try:
        a.run(args["<path>"])

    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
