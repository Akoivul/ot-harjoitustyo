from tkinter import Tk
from ui.ui import UI


def main():
    root = Tk()
    root.title("Game Backlog")
    root.geometry("700x500")
    ui = UI(root)
    ui.start()
    root.mainloop()


if __name__ == "__main__":
    main()
