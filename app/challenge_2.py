"""This module contains logic of the challenge 2"""
import sqlite3
from datetime import datetime as dt

import pandas as pd


def get_df_data():
    """Return DF with customer_ord_lines rows"""
    query = """
    SELECT ord_id, ord_dt, qt_ordd FROM customer_orders
    """
    conn = sqlite3.connect("main.db")
    data_set = pd.read_sql(
        query,
        conn,
    )
    conn.close()
    data_set["ord_dt"] = pd.to_datetime(data_set["ord_dt"], format="%m/%d/%y")
    return data_set


def get_season(date: dt) -> str:
    """Return the season of a specific date"""
    year_str = str(date.year)
    season = ""
    date_format = "%Y/%m/%d"
    spring = (
        dt.strptime(year_str + "/3/19", date_format),
        dt.strptime(year_str + "/6/19", date_format),
    )
    summer = (
        dt.strptime(year_str + "/6/20", date_format),
        dt.strptime(year_str + "/9/21", date_format),
    )
    fall = (
        dt.strptime(year_str + "/9/22", date_format),
        dt.strptime(year_str + "/12/20", date_format),
    )

    if date >= spring[0] and date <= spring[1]:
        season = "SPRING"
    elif date >= summer[0] and date <= summer[1]:
        season = "SUMMER"
    elif date >= fall[0] and date <= fall[1]:
        season = "FALL"
    else:
        season = "WINTER"

    return season


def ord_season():
    """Return what season were orders created"""
    df_data = get_df_data()
    df_data["season"] = df_data["ord_dt"].apply(get_season)

    return df_data[["ord_id", "season"]].to_json(orient="records")
