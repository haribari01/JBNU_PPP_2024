# [문자열 대문자 <-> 소문자 변환]
# def toggle_text(text:str) -> str:
#     change_text = ""
#     for i in text:
#         if i.islower():
#             change_text += i.upper()
#         elif i.isupper():
#             change_text += i.lower()
#         else:
#             change_text += i
#     return change_text

#[ASCII코드 이용한 ver.]
def toggle_text(text:str) -> str:
    change_text = ""
    for i in text:
        ASCII = ord(i)
        if 65 <= ASCII <= 90:  #ASCII 코드에서 A=65 ~Z=90 /a=97 ~ z=122
            change_text += chr(ASCII+32)   # 알파벳 대문자와 소문자의 ASCII 값차이는 32
        elif 97 <= ASCII <= 122:
            change_text += chr(ASCII-32)
        else:
            change_text += i
    return change_text

def main():
    print("문자를 입력하세요.")
    string = input("")
    if string:
        print(f"{toggle_text(string)}")
    else:
        print("입력값이 없습니다.")

if __name__ == "__main__":
    main()
