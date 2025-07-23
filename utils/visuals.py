import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_charts():
    conn = sqlite3.connect("transactions.db")
    df = pd.read_sql_query("SELECT * FROM transactions", conn)

    if df.empty:
        print("No data to display")
        return

    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    df.groupby("category")["amount"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.show()

    df.resample("M")["amount"].sum().plot(kind="bar")
    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()