from tkinter import filedialog, Tk
import platform

root = Tk()
root.geometry("0x0")
root.overrideredirect(1)
root.withdraw()

def select_file():
    root.update()
    root.lift()
    root.focus_force()
    path = filedialog.askopenfilename()
    root.update()
    print(path)

if __name__ == "__main__":
    select_file()
