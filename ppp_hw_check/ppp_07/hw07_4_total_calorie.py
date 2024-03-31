def total_calorie(fruits, fruits_calorie_dic):
    total_cal = 0
    for fruit in fruits:
        if fruit in fruits_calorie_dic:
            total_cal += fruits[fruit] * fruits_calorie_dic[fruit]/100
        else:
            return False
    return total_cal
# for문으로 key값(과일이름) 할당하고 계산.

def main():
    fruits = {"딸기":300, "한라봉":150}
    # fruits = {"바나나":100, "유자":200, "복숭아":400} 일때 결과값 : 371.0
    # fruits = {"토마토":100} 일때 결과값 : {'토마토': 100}에 정보가 없는 입력값이 포함되어 있어 총 칼로리 계산이 불가능합니다.
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77, "사과": 57, "포도": 60,
                          "수박": 31, "참외": 47, "파인애플": 53, "복숭아": 49, "오렌지": 47,
                          "키위": 54, "석류": 77, "애플망고": 57, "귤": 39, "천혜향": 41,
                          "레드향": 48, "레몬": 36, "블루베리": 48, "자몽": 32, "복분자": 88,
                          "멜론": 21, "무화과": 57, "유자": 49, "망고스틴": 71, "자두": 26}
    total_cal = total_calorie(fruits, fruits_calorie_dic)
    if total_cal != False:
        print(f"당신이 먹은 과일의 총 칼로리는 {total_cal:.1f}입니다.")
    else:
        print(f"{fruits}에 정보가 없는 입력값이 포함되어 있어 총 칼로리 계산이 불가능합니다.")

if __name__ == "__main__":
    main()

# 딕셔너리 가독성 좋게 띄어쓰기 하는방법이 궁금합니다. 그냥 tap과 space bar로 줄 맞춰도 문제 없는건가요.
