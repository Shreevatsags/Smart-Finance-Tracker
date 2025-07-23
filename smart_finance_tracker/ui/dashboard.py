import tkinter as tk
from tkinter import ttk
from data.db import add_transaction, get_all_transactions
from utils.visuals import generate_charts

class Dashboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f0f2f5")
        self.master = master
        self.configure(bg="#f0f2f5")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Smart Finance Tracker", font=("Helvetica", 20, "bold"), fg="#2c3e50", bg="#f0f2f5")
        self.label.pack(pady=20)

        form_frame = tk.Frame(self, bg="#f0f2f5")
        form_frame.pack(pady=10)

        labels = ["Date (YYYY-MM-DD)", "Amount", "Category", "Description"]
        self.entries = []
        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label, font=("Arial", 12), bg="#f0f2f5", fg="#34495e").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        button_frame = tk.Frame(self, bg="#f0f2f5")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Add Transaction", font=("Arial", 11, "bold"), bg="#27ae60", fg="white", command=self.add_transaction, width=20).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Show Transactions", font=("Arial", 11, "bold"), bg="#2980b9", fg="white", command=self.show_transactions, width=20).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Generate Charts", font=("Arial", 11, "bold"), bg="#8e44ad", fg="white", command=self.generate_charts, width=20).grid(row=0, column=2, padx=10)

        self.tree = ttk.Treeview(self, columns=("Date", "Amount", "Category", "Description"), show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(pady=20, padx=20, fill="both", expand=True)

    def add_transaction(self):
        date = self.entries[0].get()
        amount = float(self.entries[1].get())
        category = self.entries[2].get()
        description = self.entries[3].get()
        add_transaction(date, amount, category, description)
        self.clear_entries()
        self.show_transactions()

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def show_transactions(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for txn in get_all_transactions():
            self.tree.insert("", tk.END, values=txn)

    def generate_charts(self):
        generate_charts()
