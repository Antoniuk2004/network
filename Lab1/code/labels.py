from tkinter import ttk

import psutil


def initialize_labels(root):
    labels = []
    labels.append(ttk.Label(root, text=f"CPU Usage"))
    labels.append(ttk.Label(root, text=f"Memory Usage"))
    labels.append(ttk.Label(root, text=f"Disk Usage"))

    for label in labels:
        label.pack()

    return labels


def update_labels(labels):
    cpu_percent, memory_usage, disk_usage = get_data()
    labels[0].config(text=f"CPU Usage: {cpu_percent}%")
    labels[1].config(text=f"Memory Usage: {memory_usage}%")
    labels[2].config(text=f"Disk Usage: {disk_usage}%")


def get_data():
    cpu_percent = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_percent, memory_usage, disk_usage
