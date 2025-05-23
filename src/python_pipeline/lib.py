from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from pandas.core.window.rolling import timedelta


class SheetNameError(Exception):
    pass


@dataclass
class Frames:
    """
    The payroll data, in convenient format.
    """

    disbursements: pd.DataFrame
    payslips: pd.DataFrame
    paycodes: pd.DataFrame


def read_xlsx(path: Path) -> Frames:
    """
    Read XLSX file into a convenient format.
    """
    file = pd.ExcelFile(path)
    frames = {}

    # The XSLX must have a single one of these sheets, else bail
    labels = ["Disbursements", "Payslips", "PayCodes"]
    for label in labels:
        matching = [sheet for sheet in file.sheet_names if sheet == label]
        if len(matching) == 1:
            pass
        else:
            raise SheetNameError(f"{label} sheet missing or duplicate.")

        dataframe: pd.DataFrame = file.parse(label)  # pyright: ignore [reportAssignmentType]
        dataframe.columns = dataframe.columns.str.strip()
        frames[label.lower()] = dataframe

    return Frames(**frames)


def select_ordinary(frames: Frames) -> Frames:
    """
    Keep ordinary time earnings, discard others.
    """
    payslips = pd.merge(
        frames.payslips,
        frames.paycodes,
        how="inner",
        left_on="code",
        right_on="pay_code",
    )

    frames.payslips = payslips.loc[payslips.ote_treatment == "OTE"].drop(
        labels=frames.paycodes.columns, axis=1
    )
    return frames


def payable_super(payslips: pd.DataFrame, perc: float = 9.5) -> pd.DataFrame:
    """
    Add a column to payslips with payable super.
    """
    payslips["super"] = payslips["amount"] / perc
    groupby = ["payslip_id", "end", "employee_code"]
    payable = payslips.groupby(groupby).sum().super.reset_index()
    return payable


def calculate_disbursement(
    frame: pd.DataFrame, datecol: str, plus_days: int = 28
) -> pd.DataFrame:
    """
    Having a date, find its quarter date, then add more days to it.
    """
    frame["disbursement_due"] = frame[datecol].dt.to_period(
        "Q"
    ).dt.end_time + timedelta(days=plus_days)
    return frame


def disbursements_due(super: pd.DataFrame, sum_col: str) -> pd.Series:
    """
    Sum `sum_col` by `disbursement_due` and `employee_code`.
    """
    groupby = ["employee_code", "disbursement_due"]
    return super.groupby(groupby).loc[:, sum_col].sum()
