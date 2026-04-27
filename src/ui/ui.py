import tkinter as tk
from tkinter import ttk, StringVar
from services.game_service import game_service


class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
# generoitu koodi alkaa
        self._show_login()

    def _clear_view(self):
        for widget in self._root.winfo_children():
            widget.destroy()

    def _show_login(self):
        self._clear_view()

        self._username_var = StringVar()
        self._password_var = StringVar()
        self._message_var = StringVar()

        ttk.Label(self._root, text="Login", font=("Arial", 16, "bold")).pack()

        ttk.Label(self._root, text="Username").pack()
        ttk.Entry(self._root, textvariable=self._username_var).pack()

        ttk.Label(self._root, text="Password").pack()
        ttk.Entry(self._root, textvariable=self._password_var, show="*").pack()

        ttk.Button(self._root, text="Login", command=self._login).pack()
        ttk.Button(self._root, text="Register",
                   command=self._show_register).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

    def _show_register(self):
        self._clear_view()

        self._username_var = StringVar()
        self._password_var = StringVar()
        self._message_var = StringVar()

        ttk.Label(self._root, text="Register",
                  font=("Arial", 16, "bold")).pack()

        ttk.Label(self._root, text="Username").pack()
        ttk.Entry(self._root, textvariable=self._username_var).pack()

        ttk.Label(self._root, text="Password").pack()
        ttk.Entry(self._root, textvariable=self._password_var, show="*").pack()

        ttk.Button(self._root, text="Register", command=self._register).pack()
        ttk.Button(self._root, text="Back to Login",
                   command=self._show_login).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

    def _show_backlog(self):
        self._clear_view()

        self._game_name_var = StringVar()
        self._game_status_var = StringVar()
        self._message_var = StringVar()

        self._status_names = game_service.get_status_names()

        self._root.bind_class("TCombobox", "<MouseWheel>", lambda e: "break")
        self._root.bind_class("TCombobox", "<Button-4>", lambda e: "break")
        self._root.bind_class("TCombobox", "<Button-5>", lambda e: "break")

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
        self._edit_status_button = ttk.Button(self._root, text="Edit status names", command=self._show_edit_status_names)
        self._edit_status_button.pack()
        ttk.Button(self._root, text="Sign out",
                   command=self._show_login).pack()
        ttk.Label(self._root, textvariable=self._message_var).pack()

        ttk.Separator(self._root, orient="horizontal").pack(fill="x", pady=5)

        board = ttk.Frame(self._root)
        board.pack(fill="both", expand=True)

        for i in range(3):
            board.columnconfigure(i, weight=1, uniform="col")
        board.rowconfigure(0, weight=1)

        self._canvases = []
        self._frames = []

        for column in range(3):
            canvas = tk.Canvas(board, highlightthickness=0)
            scrollbar = ttk.Scrollbar(board, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)

            frame = ttk.Frame(canvas)
            canvas.create_window((0, 0), window=frame, anchor="nw")

            frame.bind(
                "<Configure>",
                lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
            )

            canvas.grid(row=0, column=column, sticky="nsew", padx=(5, 0))
            scrollbar.grid(row=0, column=column, sticky="nse")

            self._canvases.append(canvas)
            self._frames.append(frame)

        self._backlog_frame = self._frames[0]
        self._progress_frame = self._frames[1]
        self._done_frame = self._frames[2]

        self._update_games()
    
    def _show_edit_status_names(self):
        self._status_dialog = tk.Toplevel(self._root)
        self._status_dialog.title("Edit Status Names")
        self._status_dialog.resizable(False, False)
        self._status_dialog.error_var = StringVar()

        x = self._edit_status_button.winfo_rootx()
        y = self._edit_status_button.winfo_rooty() + self._edit_status_button.winfo_height()
        self._status_dialog.geometry(f"+{x}+{y}")

        self._status_entries = []

        for i, name in enumerate(game_service.get_status_names()):
            ttk.Label(self._status_dialog, text=f"Column {i + 1}:").grid(
                row=i, column=0, padx=10, pady=5, sticky="e")
            var = StringVar(value=name)
            entry = ttk.Entry(self._status_dialog, textvariable=var, width=20)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self._status_entries.append(var)

        ttk.Label(self._status_dialog, textvariable=self._status_dialog.error_var).grid(
            row=len(self._status_entries), column=0, columnspan=2)

        ttk.Button(self._status_dialog, text="Save", command=self._set_new_status_names).grid(
            row=len(self._status_entries) + 1, column=0, columnspan=2, pady=10)
    
    def _set_new_status_names(self):
        new_names = [v.get().strip() for v in self._status_entries]
        try:
            game_service.set_new_status_names(new_names)
            self._status_dialog.destroy()
            self._show_backlog()
        except Exception as error:
            self._status_dialog.error_var.set(str(error))

    def _add_game(self):
        game_name = self._game_name_var.get()
        game_status = self._game_status_var.get()

        try:
            game_service.add_game_to_backlog(game_name, game_status)
            self._game_name_var.set("")
            self._game_status_var.set("")
            self._update_games()
        except Exception as error:
            self._message_var.set(str(error))

    def _change_status(self, name, new_status):
        game_service.change_game_status(name, new_status)
        self._update_games()

    def _delete_game(self, name):
        game_service.delete_game_from_backlog(name)
        self._update_games()

    def _update_games(self):
        for frame in [
            self._backlog_frame,
            self._progress_frame,
            self._done_frame
        ]:
            for widget in frame.winfo_children():
                widget.destroy()

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
            row.pack(anchor="w", fill="x", pady=5)

            combo = ttk.Combobox(
                row,
                textvariable=status_var,
                values=self._status_names,
                state="readonly",
                width=15
            )
            combo.pack(side="left")

            ttk.Button(
                row,
                text="Delete",
                command=lambda g=game: self._delete_game(g.name)
            ).pack(side="left", padx=10)

            combo.bind(
                "<<ComboboxSelected>>",
                lambda e, g=game, var=status_var: self._change_status(
                    g.name, var.get())
            )

    def _login(self):
        username = self._username_var.get()
        password = self._password_var.get()

        try:
            game_service.login(username, password)
            self._show_backlog()
        except Exception as error:
            self._message_var.set(str(error))

    def _register(self):
        username = self._username_var.get()
        password = self._password_var.get()

        try:
            game_service.register_user(username, password)
            self._message_var.set("User registered successfully")
            self._root.after(1000, self._show_login)
        except Exception as error:
            self._message_var.set(str(error))
# generoitu koodi päättyy
