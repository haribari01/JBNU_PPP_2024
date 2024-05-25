import random
import tkinter as tk
from tkinter import simpledialog
from hw17_2_3_hangman import update_shown_answer

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    word_list = ['smartfarm', 'jeonbuk', 'football', 'chicken', 'seungwon' ]
    hidden_answer = random.choice(word_list)
    shown_answer = "_" * len(hidden_answer)
    trial = 7

    while True:
        x = gui_input(f"({shown_answer}, {len(hidden_answer)}글자입니다. 목숨 = {trial}) 답을 입력하시오 => ?")
        if x in hidden_answer:
            shown_answer = update_shown_answer(shown_answer, hidden_answer, x)
        else:
            trial -= 1
        if "_" not in shown_answer:
            print("정답입니다.")
            break

        if trial <= 0:
            print(f"틀렸습니다. 정답은 {hidden_answer} 입니다.")
            break

if __name__ == "__main__":
    main()