def main():
    dataset = []
    while True:
        try:
            print("숫자를 입력해 주세요. (-1을 입력하면 종료됩니다.)")
            number = int(input())
            if number == -1:
                break
            if number > 0:
                dataset.append(number)
                # print(dataset)
        except ValueError:
            pass

    if len(dataset) != 0:
        print(f"입력된 값은 {dataset}입니다. 총 {len(dataset)}개의 자연수가 입력되었고, 평균은 {sum(dataset) / len(dataset)}입니다.")
    else:
        print("입력된 자연수가 없습니다.")

if __name__ == "__main__":
    main()

# 과제 제출이후 추가로 질문할 것이 있어서 발송을 취소했는데, 수신자의 메일이 네이버메일이 아닌경우 취소가 안된다고 합니다. 
# 발송이 취소된 줄 알고 수정한 메일을 보냈는데... 의도치 않게 메일이 2개가 됐습니다. 죄송합니다.
# 과제15는 동일한데 혹시 질문을 못 보셨을 수 있어 아래에 주석으로 글 남깁니다.
# Q : 과제 14에서 일교차 리스트를 만들때 빈칸이 아닐때만 추가하도록 코드를 짰는데, 
#     인덱스를 일교차 리스트로 설정해서 빈칸행 개수만큼 날짜가 당겨진 것을 뒤늦게 알게 됐습니다.
#     과제 제출을 Github 커밋 시간으로 판별한다고 해서 아직 수정하지 않았는데, 수정해도 괜찮은가요?
