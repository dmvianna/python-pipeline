"""python_pipeline -- Check payroll compliance

Usage:
  python_pipeline <path> ...
  python_pipeline (-h | --help)
  python_pipeline --version

Options:
  -h --help                    Show this screen
  --version                    Show version
  <path>                       Path to XLSX file
"""

from docopt import docopt

from python_pipeline.app import App

if __name__ == "__main__":
    args = docopt(__doc__, version="python_pipeline 1.0")

    print(args)
    a = App()

    try:
        a.run(args["<path>"])

    except Exception as e:
        raise e
