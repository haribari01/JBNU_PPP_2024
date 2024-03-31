# 윤년: 4의 배수면서 100의 배수가 아닌 수
def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

def main():
    y = int(input("연도를 입력하세요."))
    if is_leap_year(y) == True:
        print(f"{y}년은 윤년입니다.")
    else:
        print(f"{y}년은 윤년이 아닙니다.")

if __name__ == "__main__":
    main()