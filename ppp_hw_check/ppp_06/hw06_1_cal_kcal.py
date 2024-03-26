def cal_kcal(eat_fruits, eat_grams):
    cal = {
        "한라봉": 50, "딸기": 34, "바나나": 77, "사과": 57, "포도": 60,
        "수박": 31, "참외": 47, "파인애플": 53, "복숭아": 49, "오렌지": 47,
        "키위": 54, "석류": 77, "애플망고": 57, "귤": 39, "천혜향": 41,
        "레드향": 48, "레몬": 36, "블루베리": 48, "자몽": 32, "복분자": 88,
        "멜론": 21, "무화과": 57, "유자": 49, "망고스틴": 71, "자두": 26
    }
    total_cal = 0
    for eat_fruit, eat_gram in zip(eat_fruits, eat_grams):
            if eat_fruit in cal:
                total_cal += cal[eat_fruit] * int(eat_gram) /100
            else:
                print(f"{eat_fruits}에 정보가 없는 입력값이 포함되어 있어 총 칼로리 계산이 불가능합니다.")
                return None
    return total_cal
def main():
    """먹은 과일과 먹은 양을 ','로 구분해 입력 받음."""
    eat_fruits = input("당신이 먹은 과일을 입력하세요.").split(',')
    eat_grams = input("당신이 먹은 과일의 양을 입력하세요.").split(',')
    total_cal = cal_kcal(eat_fruits, eat_grams)
    if total_cal != None:
        print(f"당신이 먹은 과일의 총 칼로리는 {total_cal}입니다.")

if __name__ == "__main__":
    main()
