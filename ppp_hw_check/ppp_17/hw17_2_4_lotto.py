import random
def get_lotto():
    result = []

    while True:
        num = random.randint(1, 45) #로또는 1~45 고정 -> 매개변수 받지않고 설정.
        if num not in result:
            result.append(num)
        if len(result) == 6:
            return sorted(result)

def rank_check(winning_nums, bonus_num, lotto_nums):
    count = 0
    for num in lotto_nums:
        if num in winning_nums:
            count += 1

    if count == 6:
        return "1등"
    elif count == 5 and bonus_num in lotto_nums:
        return "2등"
    elif count == 5:
        return "3등"
    elif count == 4:
        return "4등"
    elif count == 3:
        return "5등"
    else:
        return "낙첨"

def main():
    buy = int(input("로또 자동으로 몇장 구매하실건가요?"))
    bonus_num = 7
    winning_nums = [1, 6, 21, 24, 25, 33]

    for i in range(buy):
        lotto_nums = get_lotto()
        print(f"{i+1}: {lotto_nums} -> 결과는 {rank_check(winning_nums,bonus_num,lotto_nums)} 입니다.")

if __name__ == '__main__':
    main()