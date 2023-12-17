from utils import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse
import time
import os
import threading 
#from gui_dialog import open_dialog
import flet as ft

def open_dialog(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e.path)

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Choose Directory",
                    icon = ft.icons.UPLOAD_FILE,
                    on_click = lambda _:pick_files_dialog.get_directory_path()
                ),
                selected_files,
            ]
        )
    )

class EventHandler(FileSystemEventHandler): # should be out of this file
    def on_any_event(self, e):
        pass

    def on_modified(self, e):
        pass

    def on_created(self, e):
        # check path
        new_file_path = e.src_path
        print(f"new file createdw:{new_file_path}")
        # open dialog and pass new_file_path
        os.system("flet run gui_dialog.py")

    def on_moved(self, e):
        pass

    def on_deleted(self, e):
        pass

def watch(path):
    observer = Observer()
    observer.schedule(EventHandler(), path=DIR, recursive=True)
    observer.start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir")
    args = parser.parse_args()
    DIR = args.dir
    
    watch_thread = threading.Thread(target=watch, args=(DIR,))
    watch_thread.start()
