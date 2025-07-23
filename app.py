import tkinter as tk
from ui.dashboard import Dashboard

def main():
    root = tk.Tk()
    root.title("Smart Finance Tracker")
    root.geometry("900x600")
    app = Dashboard(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
