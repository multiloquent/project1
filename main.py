import tkinter as tk
from gui import Gui
from voter_id_handler import *


def main() -> None:
    """
    Main function of program.
    """
    start_record()
    root = tk.Tk()
    root.resizable(False, False)

    Gui(root)

    root.mainloop()


if __name__ == '__main__':
    main()
