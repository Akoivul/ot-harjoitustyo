from tkinter import Tk, ttk
from services.game_service import game_service

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Game Backlog")
        button = ttk.Button(master=self._root, text="Exit", command=self._root.destroy)

        label.pack()
        button.pack()