import random

def update_shown_answer(shown_answer, hidden_answer, x):
    results = []

    for shown_text, hidden_text in zip(shown_answer, hidden_answer):
        if shown_text == "_":
            if x == hidden_text:
                results.append(x)
            else:
                results.append("_")
        else:
            results.append(shown_text)    #맞춘 단어 보여지게 출력.
            # results.append(shown_answer)    #이렇게 하면 j______e______o____ 이런식으로 나옴.
    return "".join(results)   #리스트 안에 값을 결합된 '문자열'로 반환해준다.


def main():
    word_list = ['smartfarm', 'jeonbuk', 'football', 'chicken', 'seungwon' ]
    # hidden_answer = random.choices(word_list)      #random.choices는 choice랑 다르게 여러개 가져오는거. 이때 len하면 값이 1만 나옴.
    # hidden_answer = random.choices(word_list)[0]   #인덱스 설정을 해줘야 첫번째 요소인 단어를 가져오고 len을 제대로 구할 수 있음.
    hidden_answer = random.choice(word_list)
    shown_answer = "_" * len(hidden_answer)
    # print(hidden_answer)
    # print(len(hidden_answer))
    # print(shown_answer)

    trial = 7

    while True:
        x = input(f"({shown_answer}, 목숨 = {trial}) 답을 입력하시오 => ?")
        if x in hidden_answer:
            shown_answer = update_shown_answer(shown_answer, hidden_answer, x)
        else:
            trial -= 1
        if "_" not in shown_answer:
            print("정답입니다.")
            break

        if trial <= 0:    # 0일때 종료해도 되는데 코드 안정성을 위해 0이하로 설정.
            print(f"틀렸습니다. 정답은 {hidden_answer} 입니다.")
            break

if __name__ == '__main__':
    main()