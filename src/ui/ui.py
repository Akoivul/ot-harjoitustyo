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

        ttk.Label(self._root, text="Login").pack()

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

        ttk.Label(self._root, text="Register").pack()

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

        ttk.Label(self._root, text="Game Backlog").pack()

        ttk.Label(self._root, text="Game").pack()
        ttk.Entry(self._root, textvariable=self._game_name_var).pack()

        ttk.Label(self._root, text="Status").pack()
        ttk.Entry(self._root, textvariable=self._game_status_var).pack()

        ttk.Button(self._root, text="Add", command=self._add_game).pack()
        ttk.Button(self._root, text="Sign out",
                   command=self._show_login).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

        self._tree = ttk.Treeview(self._root, columns=(
            "name", "status"), show="headings")
        self._tree.heading("name", text="Game")
        self._tree.heading("status", text="Status")
        self._tree.column("name", width=200)
        self._tree.column("status", width=100)
        self._tree.pack()

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

    def _update_games(self):
        for item in self._tree.get_children():
            self._tree.delete(item)

        games = game_service.get_all_games()

        for game in games:
            self._tree.insert("", "end", values=(game.name, game.status))

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
