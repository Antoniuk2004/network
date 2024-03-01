from tkinter import ttk

from interface_manager import calc_number_of_interfaces, get_list_of_interfaces


def initialize_treeview(root):
    tree = ttk.Treeview(root, columns=("Column 1", "Column 2", "Column 3", "Column 4"),
                        show="headings")
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Interface")
    tree.heading("#3", text="Bytes Sent")
    tree.heading("#4", text="Bytes Received")
    return tree


def initialize_treeview_values(tree):
    num = calc_number_of_interfaces()
    step = 1

    for j in range(num):
        values = [f"Value{i}" for i in range(step, step + 3)]
        tree.insert("", "end", text="Parent", values=values)
        step += 3

    tree.pack(expand=True)


def update_treeview(tree):
    list_of_interfaces = get_list_of_interfaces()
    for index, interface in enumerate(list_of_interfaces):
        new_values = []
        new_values.append(interface.get_index())
        new_values.append(interface.get_name())
        new_values.append(interface.get_bytes_sent())
        new_values.append(interface.get_bytes_received())

        tree.item(tree.get_children()[index], values=new_values)
