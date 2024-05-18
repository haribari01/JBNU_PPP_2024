import random
def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []

    for i in text:
        chosung.append(CHOSUNG_LIST[(ord(i) - ord('가'))//588])
    return chosung

def main():
    word_list = ['프원실', '연오의파이썬', '전북대', '스마트팜', '대동제', '싸이', '후생관', '브디런', '축산학', '토양학']
    hidden_answer = random.choice(word_list)
    problem = get_chosung(hidden_answer)
    print(f"문제입니다. 주어진 초성은 '{''.join(problem)}'입니다.")
    answer = input("답은 => ?")
    if answer == hidden_answer:
        print("정답입니다.")
    else:
        print(f"틀렸습니다. 정답은 {hidden_answer}입니다.")

if __name__ == '__main__':
    main()