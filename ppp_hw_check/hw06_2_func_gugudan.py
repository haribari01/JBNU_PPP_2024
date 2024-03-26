def gugudan(dan):
    for i in range(1, 9 + 1):
        print(f"{dan}*{i}={dan * i:2d}")
def main():
    dan = int(input("구구단 몇단?"))
    gugudan(dan)

if __name__ == '__main__':
    main()