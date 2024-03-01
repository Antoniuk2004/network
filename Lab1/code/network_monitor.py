import tkinter as tk

from helpers import update_values
from labels import initialize_labels
from treeview import initialize_treeview, initialize_treeview_values

if __name__ == "__main__":
    root = tk.Tk()
    root.title("System Monitor")
    root.resizable(width=False, height=False)
    tree = initialize_treeview(root)
    initialize_treeview_values(tree)

    labels = initialize_labels(root)

    update_values(tree, labels)

    root.mainloop()
