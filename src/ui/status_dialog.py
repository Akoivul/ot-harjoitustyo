import tkinter as tk
from tkinter import ttk
from services.game_service import game_service

# generoitu koodi alkaa


class StatusDialog:
    def __init__(self, root, refresh_callback):
        self._root = tk.Toplevel(root)
        self._refresh_callback = refresh_callback

        self.error_var = tk.StringVar()
        self._entries = []

        self._build()

    def _build(self):
        self._root.title("Edit Status Names")
        self._root.resizable(False, False)

        self._root.transient(self._root.master)
        self._root.grab_set()

        for i, name in enumerate(game_service.get_status_names()):
            ttk.Label(
                self._root, text=f"Column {i + 1}:").grid(row=i, column=0)

            var = tk.StringVar(value=name)

            ttk.Entry(self._root, textvariable=var).grid(row=i, column=1)

            self._entries.append(var)

        row = len(self._entries)

        ttk.Label(self._root, textvariable=self.error_var).grid(
            row=row, column=0, columnspan=2)

        ttk.Button(self._root, text="Save", command=self._save).grid(
            row=row + 1, column=0, columnspan=2)

        self._root.protocol("WM_DELETE_WINDOW", self._close)

    def _save(self):
        try:
            game_service.set_new_status_names(
                [v.get().strip() for v in self._entries])
            self._refresh_callback()
            self._root.destroy()

        except Exception as e:
            self.error_var.set(str(e))

    def _close(self):
        self._root.grab_release()
        self._root.destroy()
# generoitu koodi päättyy
