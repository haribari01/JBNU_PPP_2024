import tkinter as tk
from tkinter import simpledialog
from hw16_1_ASCII_upper import toggle_text

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    string = gui_input("문자를 입력하세요")
    if string:
        print(f"{toggle_text(string)}")
    else:
        print("입력값이 없습니다.")

if __name__ == "__main__":
    main()