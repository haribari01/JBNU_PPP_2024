import tkinter as tk
from tkinter import simpledialog
from hw16_2_Caesar import caesar_encode, caesar_decode

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    string = gui_input("암호화 하고 싶은 '대문자'를 입력하세요.")
    num = int(gui_input("몇칸을 밀어서 암호화 할까요?"))
    encode = caesar_encode(string,num)
    print(f"암호화된 문장은{encode}입니다.")
    print(f"해독하면 {caesar_decode(encode, num)}입니다.")

if __name__ == "__main__":
    main()