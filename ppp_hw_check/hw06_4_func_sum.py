def sum_n(n):
    total = 0
    for i in range(n+1):
        total += i
    print(f"1부터 {n}까지의 합은 {total}입니다.")
def main():
    n = int(input("숫자를 입력하세요."))
    sum_n(n)

if __name__ == '__main__':
    main()