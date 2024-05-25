import tkinter as tk
from tkinter import simpledialog
from hw17_2_1_countdown import countdown

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    count = int(gui_input("몇 초를 카운트다운 할까요? "))
    countdown(count)

if __name__ == "__main__":
    main()