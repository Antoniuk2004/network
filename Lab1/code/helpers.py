from labels import update_labels
from treeview import update_treeview


def update_values(tree, labels):
    update_treeview(tree)
    update_labels(labels)

    tree.after(1000, update_values, tree, labels)
