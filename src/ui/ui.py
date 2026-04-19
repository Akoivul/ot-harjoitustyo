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

        ttk.Label(self._root, text="Register", font=("Arial", 16, "bold")).pack()

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

        ttk.Label(self._root, text="Game Backlog", font=("Arial", 16, "bold")).pack()

        ttk.Label(self._root, text="Game").pack()
        ttk.Entry(self._root, textvariable=self._game_name_var).pack()

        ttk.Label(self._root, text="Status").pack()
        ttk.Combobox(
            self._root,
            textvariable=self._game_status_var,
            values=["Backlog", "In Progress", "Completed"],
            state = "readonly"
        ).pack()

        ttk.Button(self._root, text="Add", command=self._add_game).pack()
        ttk.Button(self._root, text="Sign out", command=self._show_login).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

        board = ttk.Frame(self._root)
        board.pack(fill="both", expand=True)

        self._backlog_frame = ttk.Frame(board)
        self._progress_frame = ttk.Frame(board)
        self._done_frame = ttk.Frame(board)

        self._backlog_frame.pack(side="left", fill="both", expand=True, padx=10)
        self._progress_frame.pack(side="left", fill="both", expand=True, padx=10)
        self._done_frame.pack(side="left", fill="both", expand=True, padx=10)

        ttk.Label(self._backlog_frame, text="Backlog",
              font=("Arial", 12, "bold")).pack(pady=5)

        ttk.Label(self._progress_frame, text="In Progress",
                font=("Arial", 12, "bold")).pack(pady=5)

        ttk.Label(self._done_frame, text="Completed",
                font=("Arial", 12, "bold")).pack(pady=5)

        self._update_games()

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
            if game.status == "Backlog":
                parent = self._backlog_frame
            elif game.status == "In Progress":
                parent = self._progress_frame
            else:
                parent = self._done_frame

            card = ttk.Frame(parent, padding=10, relief="ridge")
            card.pack(fill="x", pady=5)

            ttk.Label(card, text=game.name, font=("Arial", 11, "bold")).pack(anchor="w")

            status_var = StringVar(value=game.status)

            combo = ttk.Combobox(
                card,
                textvariable=status_var,
                values=["Backlog", "In Progress", "Completed"],
                state="readonly"
            )
            combo.pack(anchor="w")

            combo.bind(
                "<<ComboboxSelected>>",
                lambda e, g=game, var=status_var: self._change_status(g.name, var.get())
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
