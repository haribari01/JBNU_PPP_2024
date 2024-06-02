import tkinter as tk
import random

def Rock_Scissors_Paper(text):
    dataset = ["가위", "바위", "보"]
    computer = random.choice(dataset)
    # print(computer)
    # print(text)
    if text == computer:
        return "비겼습니다."
    elif text == "가위" and computer == "보" or text == "바위" and computer == "가위" or text == "보" and computer == "바위":
        return "이겼습니다."
    else:
        return "졌습니다."

def click(ent_input, ent_output):
    input_text = ent_input.get()
    result = Rock_Scissors_Paper(input_text)
    ent_output.delete(0, tk.END)
    ent_output.insert(0, result)

    if result == "이겼습니다.":            #결과에 따라 다른색으로 출력
        ent_output.config(fg="blue")
    elif result == "졌습니다.":
        ent_output.config(fg="red")
    else:
        ent_output.config(fg="black")

def main():
    window = tk.Tk()
    window.title("가위바위보")
    window.resizable(width=False, height=False)
    window.geometry("800x100")

    frm_entry = tk.Frame(master=window)
    frm_entry.grid(row=0, column=0, padx=40, pady=10)

    lbl = tk.Label(master=frm_entry, text="[가위,바위,보] 중에서 하나를 입력하세요.", font=("Arial", 12))
    lbl.grid(row=0, column=0, sticky="w")
    ent_input = tk.Entry(master=frm_entry, width=20, font=("Arial", 16))
    ent_input.grid(row=1, column=0, sticky="w")

    btn_convert = tk.Button(window, text="\N{RIGHTWARDS BLACK ARROW}", font=("Arial", 14),
                            command=lambda: click(ent_input, ent_output))
    btn_convert.grid(row=0, column=1, padx=20)

    lbl_output = tk.Label(master=window, text="결과", font=("Arial", 12))
    lbl_output.grid(row=0, column=2, sticky="w")
    ent_output = tk.Entry(master=window, width=20, font=("Arial", 16))
    ent_output.grid(row=0, column=3, sticky="w")

    window.mainloop()

if __name__ == "__main__":
    main()