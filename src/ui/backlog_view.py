import tkinter as tk
from tkinter import StringVar
from tkinter import ttk

from services.game_service import game_service
from ui.status_dialog import StatusDialog

# generoitu koodi alkaa


class BacklogView:
    def __init__(self, root, show_login):
        self._root = root
        self._show_login = show_login

        self._game_name_var = StringVar()
        self._game_status_var = StringVar()
        self._message_var = StringVar()

        self._status_names = game_service.get_status_names()

        self._bind_combobox_scroll()
        self._build()
        self._update_games()

    def _build(self):
        ttk.Label(self._root, text=f"Logged in: {game_service.get_logged_in_user()}", font=(
            "Arial", 12)).pack(anchor="nw", padx=10, pady=5)
        ttk.Label(self._root, text="Game Backlog",
                  font=("Arial", 16, "bold")).pack()

        ttk.Label(self._root, text="Game").pack()
        ttk.Entry(self._root, textvariable=self._game_name_var).pack()

        ttk.Label(self._root, text="Status").pack()
        ttk.Combobox(
            self._root,
            textvariable=self._game_status_var,
            values=self._status_names,
            state="readonly"
        ).pack()

        ttk.Button(self._root, text="Add", command=self._add_game).pack()

        self._edit_status_button = ttk.Button(
            self._root, text="Edit status names", command=self._show_edit_status_names)
        self._edit_status_button.pack()

        ttk.Button(self._root, text="Sign out",
                   command=self._show_login).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

        ttk.Separator(self._root, orient="horizontal").pack(fill="x", pady=5)

        self._create_board()

    def _bind_combobox_scroll(self):
        self._root.bind_class("TCombobox", "<MouseWheel>", lambda e: "break")
        self._root.bind_class("TCombobox", "<Button-4>", lambda e: "break")
        self._root.bind_class("TCombobox", "<Button-5>", lambda e: "break")

    def _create_board(self):
        board = ttk.Frame(self._root)
        board.pack(fill="both", expand=True)

        for i in range(3):
            board.columnconfigure(i, weight=1, uniform="col")

        board.rowconfigure(0, weight=1)

        self._frames = []

        for col in range(3):
            canvas = tk.Canvas(board, highlightthickness=0)
            scrollbar = ttk.Scrollbar(
                board, orient="vertical", command=canvas.yview)

            canvas.configure(yscrollcommand=scrollbar.set)

            frame = ttk.Frame(canvas)
            canvas.create_window((0, 0), window=frame, anchor="nw")

            frame.bind("<Configure>", lambda e,
                       c=canvas: c.configure(scrollregion=c.bbox("all")))

            canvas.grid(row=0, column=col, sticky="nsew", padx=(5, 0))
            scrollbar.grid(row=0, column=col, sticky="nse")

            self._frames.append(frame)

        self._backlog_frame = self._frames[0]
        self._progress_frame = self._frames[1]
        self._done_frame = self._frames[2]

    def _add_game(self):
        try:
            game_service.add_game_to_backlog(
                self._game_name_var.get(),
                self._game_status_var.get()
            )

            self._game_name_var.set("")
            self._game_status_var.set("")
            self._message_var.set("")

            self._update_games()

        except Exception as error:
            self._message_var.set(str(error))

    def _change_status(self, name, status):
        game_service.change_game_status(name, status)
        self._update_games()

    def _delete_game(self, name):
        game_service.delete_game_from_backlog(name)
        self._update_games()

    def _update_games(self):
        for frame in [self._backlog_frame, self._progress_frame, self._done_frame]:
            for w in frame.winfo_children():
                w.destroy()

        games = game_service.get_all_games()

        for game in games:
            if game.status == self._status_names[0]:
                parent = self._backlog_frame
            elif game.status == self._status_names[1]:
                parent = self._progress_frame
            else:
                parent = self._done_frame

            card = ttk.Frame(parent, padding=10, relief="ridge")
            card.pack(fill="x", pady=5)

            ttk.Label(card, text=game.name, font=(
                "Arial", 11, "bold")).pack(anchor="w")

            status_var = StringVar(value=game.status)

            row = ttk.Frame(card)
            row.pack(fill="x", pady=5)

            combo = ttk.Combobox(
                row,
                textvariable=status_var,
                values=self._status_names,
                state="readonly",
                width=15
            )
            combo.pack(side="left")

            ttk.Button(row, text="Delete",
                       command=lambda g=game: self._delete_game(g.name)).pack(side="left", padx=10)

            combo.bind(
                "<<ComboboxSelected>>",
                lambda e, g=game, v=status_var: self._change_status(
                    g.name, v.get())
            )

    def _show_edit_status_names(self):
        StatusDialog(self._root, self._refresh_status_names)

    def _refresh_status_names(self):
        self._status_names = game_service.get_status_names()
        self._update_games()

    def _show_login(self):
        from ui.ui import UI
        UI(self._root).show_login()
# generoitu koodi päättyy
