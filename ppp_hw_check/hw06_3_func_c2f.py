def c2f(t_c):
    return (t_c * 9/5 + 32)
def main():
    t_c = int(input("섭씨온도를 입력하세요."))
    print("섭씨 {}℃는 화씨 {}℉입니다.".format(t_c, c2f(t_c)))

if __name__ == '__main__':
    main()