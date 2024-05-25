import winsound
import time

def countdown(count):
    print("Start")
    while True:
        print(f"{count}")
        time.sleep(1)
        count -= 1
        if count <= 0:
            print("Bomb!!")
            frequency = 1000  # 주파수 설정
            duration = 1500  # 지속시간 설정 (1000 = 1초)
            winsound.Beep(frequency, duration)  # 카운트다운이 끝났을 때 삐 소리 출력
            break

def main():
    count = int(input("몇 초를 카운트다운 할까요? "))
    countdown(count)

if __name__ == '__main__':
    main()