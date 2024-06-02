import tkinter as tk

def caesar_encode(text:str, shift:int) -> str:
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    caesar_text = ""

    for i in text:
        caesar_text += alphabet_list[(ord(i)-ord('A')+shift)%26]
    return caesar_text

def click(ent_input, ent_shift, ent_output):
    input_text = ent_input.get()
    shift = int(ent_shift.get())
    encode_text = caesar_encode(input_text, shift)
    ent_output.delete(0, tk.END)   # 기존내용 지우기 (0부터 마지막 텍스트까지): input 값 달라질경우 기존 output 값 지우고
    ent_output.insert(0, encode_text)   # 0위치에 새로운 output 출력

def main():
    window = tk.Tk()
    window.title("Caesar")
    window.resizable(width=False, height=True)  # False 는 크기조절 불가 / True 는 크기조절 가능
    window.geometry("900x100")   # 가로 * 세로

    frm_entry = tk.Frame(master=window)
    frm_entry.grid(row=0, column=0, padx=40, pady=10)  #padx 수평 여백/ pady 수직 여백

    lbl_input = tk.Label(master=frm_entry, text="암호화하고 싶은 대문자", font=("Arial", 12))
    lbl_input.grid(row=0, column=0, sticky="w")
    ent_input = tk.Entry(master=frm_entry, width=20, font=("Arial", 16)) # width로 입력칸 가로 조절 / 폰트크기로 입력칸 세로 크기 조절
    ent_input.grid(row=0, column=1, sticky="w")

    lbl_shift = tk.Label(master=frm_entry, text="몇칸", font=("Arial", 12))
    lbl_shift.grid(row=1, column=0, sticky="w")
    ent_shift = tk.Entry(master=frm_entry, width=10, font=("Arial", 16))
    ent_shift.grid(row=1, column=1, sticky="w")

    btn_convert = tk.Button(window, text="\N{RIGHTWARDS BLACK ARROW}",
                            command=lambda: click(ent_input, ent_shift, ent_output)) # 버튼 클릭했을때 실행할 함수 지정
    btn_convert.grid(row=0, column=2, padx=20)

    lbl_output = tk.Label(master=window, text="암호", font=("Arial", 12))
    lbl_output.grid(row=0, column=3, sticky="w")
    ent_output = tk.Entry(master=window, width=20, font=("Arial", 16))                      #window에 배치
    # ent_output = tk.Entry(master=frm_entry, width=20, font=("Arial", 16))          #frm_entry에 배치  ->  위치가 달라짐
    ent_output.grid(row=0, column=4, sticky="w")

    window.mainloop()

if __name__ == "__main__":
    main()
