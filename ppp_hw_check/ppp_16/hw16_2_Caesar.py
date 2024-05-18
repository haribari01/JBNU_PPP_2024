def caesar_encode(text:str, shift:int) -> str:
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    caesar_text = ""

    #[try 함수 ver.] = 인덱스 오류가 한번 발생할때 까지는 정상적으로 작동. but 인덱스 오류가 두번이상 발생하면 오류가 나는부분을 decode 하면 다 Z로 표시됨.
    #           인덱스오류만 해결하고 다시 try문으로 돌아가는 방법을 고민해봤는데 실패. IndexError만 해결하고 다시 try문으로 돌아가는건 불가능한가?
    # for i in text:
    #     try:
    #         caesar_text += alphabet_list[(ord(i)-ord('A')+shift)]
    #
    #     except IndexError:
    #         caesar_text += alphabet_list[(ord(i) - ord('A') // 26 + shift - 1]
    #
    # return caesar_text

    #[% ver.]
    for i in text:
        caesar_text += alphabet_list[(ord(i)-ord('A')+shift)%26] # index가 0~25사이만 나옴. IndexError를 쓸 필요가 없다.
    return caesar_text

def caesar_decode(text:str, shift:int) -> str:
    return caesar_encode(text, -shift)

def main():
    string = input("암호화 하고 싶은 '대문자'를 입력하세요.")
    # num = 3
    num = int(input("몇칸을 밀어서 암호화 할까요?"))  #3칸 외에도 밀고 싶은만큼 설정가능.
    encode = caesar_encode(string, num)
    print(f"암호화된 문장은{encode}입니다.")
    print(f"해독하면 {caesar_decode(encode,num)}입니다.")

if __name__ == "__main__":
    main()