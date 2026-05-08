from tkinter import StringVar
from tkinter import ttk
from services.game_service import game_service

# generoitu koodi alkaa
class RegisterView:
    def __init__(self, root, show_login):
        self._root = root
        self._show_login = show_login

        self._username_var = StringVar()
        self._password_var = StringVar()
        self._message_var = StringVar()

        self._build()
    
    def _build(self):
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
    
    def _register(self):
        """Registers a user.
        """

        try:
            game_service.register_user(self._username_var.get(), self._password_var.get())
            self._message_var.set("User registered successfully")
            self._root.after(1000, self._show_login)
        except Exception as error:
            self._message_var.set(str(error))
# generoitu koodi päättyy