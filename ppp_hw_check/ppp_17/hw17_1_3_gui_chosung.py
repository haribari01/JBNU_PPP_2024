import tkinter as tk
import random
from tkinter import simpledialog
from hw16_3_chosung_game import get_chosung

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    word_list = ['프원실', '연오의파이썬', '전북대', '스마트팜', '대동제', '싸이', '후생관', '브디런', '축산학', '토양학']
    hidden_answer = random.choice(word_list)
    problem = get_chosung(hidden_answer)
    answer = gui_input(f"주어진 초성은 '{''.join(problem)}'입니다. 답은 => ?")
    if answer == hidden_answer:
        print("정답입니다.")
    else:
        print(f"틀렸습니다. 정답은 {hidden_answer}입니다.")

if __name__ == "__main__":
    main()