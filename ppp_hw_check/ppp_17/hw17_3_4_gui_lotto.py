import tkinter as tk
from tkinter import simpledialog
from hw17_2_4_lotto import get_lotto, rank_check

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    buy = int(gui_input("로또 자동으로 몇장 구매하실건가요?"))
    bonus_num = 7
    winning_nums = [1, 6, 21, 24, 25, 33]

    for i in range(buy):
        lotto_nums = get_lotto()
        print(f"{i+1}: {lotto_nums} -> 결과는 {rank_check(winning_nums,bonus_num,lotto_nums)} 입니다.")

if __name__ == "__main__":
    main()