from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse
import time
import os
import threading 
from gui_dialog import select_dir
import flet as ft
from multiprocessing import Process
import tkinter as tk
from tkinter import filedialog, Tk

def _open(root):
    path = filedialog.askdirectory()
    print(path)

class EventHandler(FileSystemEventHandler): # should be out of this file
    def __init__(self, root):
        self.root = root

    def on_created(self, e):
        # check path
        new_file_path = e.src_path
        print(f"new file create:{new_file_path}")
        # open dialog and pass new_file_path
        path = filedialog.askdirectory()
        print(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir")
    args = parser.parse_args()
    DIR = args.dir

    root = tk.Tk()   
    root.geometry("0x0")
    root.withdraw()

    observer = Observer()
    observer.schedule(EventHandler(root), path=DIR, recursive=True)
    observer.start()

    try:
        root.mainloop()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
