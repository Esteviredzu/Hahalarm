"""Запуск программы - будильник"""

import tkinter as tk
from hahalarm import hahalarm

root = tk.Tk()
app = hahalarm.Alarm(root)

app.run()
