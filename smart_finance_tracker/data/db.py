import sqlite3

conn = sqlite3.connect("transactions.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS transactions (
    date TEXT,
    amount REAL,
    category TEXT,
    description TEXT
)''')
conn.commit()

def add_transaction(date, amount, category, description):
    c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?)", (date, amount, category, description))
    conn.commit()

def get_all_transactions():
    c.execute("SELECT * FROM transactions")
    return c.fetchall()
