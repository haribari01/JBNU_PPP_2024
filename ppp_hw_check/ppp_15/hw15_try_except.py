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
