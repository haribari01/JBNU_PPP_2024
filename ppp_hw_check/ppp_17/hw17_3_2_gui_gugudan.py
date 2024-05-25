import tkinter as tk
from tkinter import simpledialog
from hw17_2_2_gugudan import gugudan_test

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='Test', prompt=text)

def main():
    quiz_num = 5   #간단하게 5문제만 세팅.
    score = 0

    for i in range(quiz_num):
        x, y, correct_answer = gugudan_test()
        answer = int(gui_input(f" {x} * {y} = ? "))
        if answer == correct_answer:
            print("정답입니다.")
            score += 1
        else:
            print("오답입니다.")
    print(f"{score}개 맞췄고, 점수는 {(score / quiz_num) * 100:.0f}점 입니다.")

if __name__ == "__main__":
    main()