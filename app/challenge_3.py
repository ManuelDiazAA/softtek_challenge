"""This module contains the logic of challenge 1"""
import sqlite3

import pandas as pd
from flask import jsonify


def get_df_data():
    """Return DF with customer_ord_lines rows"""
    query = """
    SELECT date, was_rainy FROM weather
    """
    conn = sqlite3.connect("main.db")
    data_set = pd.read_sql(query, conn)
    conn.close()
    data_set["date_dt"] = pd.to_datetime(data_set["date"], format="%m/%d/%y")
    data_set = data_set.sort_values(["date_dt"])
    return data_set


def weather_change():
    """Return dates when starts rain"""
    response = []
    df_data = get_df_data()
    status = "FALSE"
    response = []
    for _, row in df_data.iterrows():
        if row["was_rainy"] == "TRUE" and status == "FALSE":
            response.append({"date": row["date"], "was_rainy": row["was_rainy"]})

        status = row["was_rainy"]

    return jsonify(response)
