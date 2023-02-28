"""This module contains the logic of challenge 1"""

import sqlite3

import pandas as pd
from flask import jsonify


def get_df_data():
    """Return DF with customer_ord_lines rows"""
    query = """
    SELECT order_number, status FROM customer_ord_lines
    """
    conn = sqlite3.connect("main.db")
    data_set = pd.read_sql(query, conn)
    conn.close()
    return data_set


def get_status(data_df: pd.DataFrame) -> str:
    """Return the status of the order"""
    status = ""
    if "PENDING" in data_df["status"].unique():
        status = "PENDING"
    elif "SHIPPED" in data_df["status"].unique():
        status = "SHIPPED"
    else:
        status = "CANCELLED"

    return status


def ord_status():
    """Return json with all order status"""
    response = []
    df_data = get_df_data()
    for order in df_data["order_number"].unique():
        sub_df = df_data[df_data["order_number"] == order]
        status = get_status(sub_df)
        response.append({"order_number": order, "status": status})

    return jsonify(response)
