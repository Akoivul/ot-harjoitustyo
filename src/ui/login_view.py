from tkinter import StringVar
from tkinter import ttk
from services.game_service import game_service


class LoginView(ttk.Frame):
    """Login view.
    """

    def __init__(self, root, show_register, show_backlog):
        self._root = root

        self._show_register = show_register
        self._show_backlog = show_backlog

        self._username_var = StringVar()
        self._password_var = StringVar()
        self._message_var = StringVar()

        self._build()

    def _build(self):
        ttk.Label(self._root, text="Login", font=("Arial", 16, "bold")).pack()

        ttk.Label(self._root, text="Username").pack()
        ttk.Entry(self._root, textvariable=self._username_var).pack()

        ttk.Label(self._root, text="Password").pack()
        ttk.Entry(self._root, textvariable=self._password_var, show="*").pack()

        ttk.Button(self._root, text="Login", command=self._login).pack()
        ttk.Button(self._root, text="Register",
                   command=self._show_register).pack()

        ttk.Label(self._root, textvariable=self._message_var).pack()

    def _login(self):
        """Logs in a user.  
        """

        try:
            game_service.login(self._username_var.get(),
                               self._password_var.get())
            self._show_backlog()
        except Exception as error:
            self._message_var.set(str(error))
