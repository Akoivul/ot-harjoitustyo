import tkinter as tk
from tkinter import ttk, StringVar
from services.game_service import game_service
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.backlog_view import BacklogView


class UI:
    """Class that handles the graphical user interface.
    """

    def __init__(self, root):
        """Constructor that initializes UI.

        Args:
            root: Tkinter root window.
        """
        self._root = root

    def start(self):
        """Starts the application with the login view.
        """
# generoitu koodi alkaa
        self._show_login()

    def _clear_view(self):
        """Remove all widgets from the root window.
        """
        for widget in self._root.winfo_children():
            widget.destroy()

    def _show_login(self):
        """Show the login view.
        """
        self._clear_view()

        LoginView(self._root, self._show_register, self._show_backlog)

    def _show_register(self):
        """Show the registration view.
        """
        self._clear_view()

        RegisterView(self._root, self._show_login)

    def _show_backlog(self):
        """Show the backlog view."""
        self._clear_view()

        BacklogView(self._root, self._show_login)
# generoitu koodi päättyy
