from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse
import time
import os
import tkinter as tk
from tkinter import filedialog, Tk
import configparser
from utils import mv

class EventHandler(FileSystemEventHandler): # should be out of this file
    def __init__(self, root):
        self.root = root

    def on_created(self, e):
        # check path
        new_file_path = e.src_path
        print(f"new file create:{new_file_path}")
        # open dialog and pass new_file_path
        dst = filedialog.askdirectory()
        mv(new_file_path, dst)
        # 失敗したら通知する

if __name__ == "__main__":
    config_ini = configparser.ConfigParser()
    config_ini.read("./config/config.ini")

    DIR = config_ini["TARGET"]["DIR"]
    print(f"observing {DIR}")
    
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
