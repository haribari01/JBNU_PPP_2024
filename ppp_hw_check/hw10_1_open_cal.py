def total_calorie(fruits, fruits_cal_dic):
    total_cal = 0
    for fruit in fruits:
        if fruit in fruits_cal_dic:
            total_cal += fruits[fruit] * fruits_cal_dic[fruit]/100
        else:
            return False
    return total_cal

def read_cal_db(filename):
    database = {}
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(',')
            fruit_name = tokens[0]
            calorie = int(tokens[1])
            database[fruit_name] = calorie
    # print(database)
    return database

# -> utf-8도 파일 열림. utf-8-sig은 BOM을 추가해 호환성이 더 좋음.

def main():
    fruits_calorie_dic = read_cal_db("calorie_db.csv")

# 내꺼
    add_fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77, "사과": 57, "포도": 60,
                          "수박": 31, "참외": 47, "파인애플": 53, "복숭아": 49, "오렌지": 47,
                          "키위": 54, "석류": 77, "애플망고": 57, "귤": 39, "천혜향": 41,
                          "레드향": 48, "레몬": 36, "블루베리": 48, "자몽": 32, "복분자": 88,
                          "멜론": 21, "무화과": 57, "유자": 49, "망고스틴": 71, "자두": 26}

    fruits_calorie_dic.update(add_fruits_calorie_dic)
    # print(fruits_calorie_dic)
    # database = read_cal_db("calorie_db.csv")
    # database.update(add_fruits_calorie_dic)
    # print(f"{database}")
#-> csv 파일에 한라봉에 대한 정보가 없어서 직접 적은 딕셔너리를 추가했습니다.

    fruits_mon = {"딸기": 300, "귤": 150}
    print("월요일에 섭취한 총 칼로리는 ", total_calorie(fruits_mon, fruits_calorie_dic))

    fruits_wed = {"딸기": 200, "바나나": 300}
    print("수요일에 섭취한 총 칼로리는 ", total_calorie(fruits_wed, fruits_calorie_dic))
    # print(total_calorie(fruits_wed, database))

# Q: csv 파일에서 딸기,바나나는 100g 당 각각 36, 84kcal이고 제가 적은 딕셔너리에서는 100g당 34, 77kcal입니다.
#    update를 하면 같은 과일은 덮어쓰기가 되는데, 딸기,바나나 처럼 이미 데이터가 있는 과일은 csv 파일에 있는 값을 사용 하고 싶을때 코드를 어떻게 짜야하는지 궁금합니다.
#    for문에 if not을 사용해서 데이터가 없는 경우에만 딕셔너리 추가하는 fruits_calorie_dic[fruit] = calorie 코드를 사용하는 방식으로 시도해봤지만 실패했습니다.
    fruits_fri = {"한라봉": 200, "바나나": 300}
    print("금요일에 섭취한 총 칼로리는 ", total_calorie(fruits_fri, fruits_calorie_dic))

    # fruits_sun = {"감자":100}
    # print("일요일에 섭취한 총 칼로리는 ", total_calorie(fruits_sun, fruits_calorie_dic))
    # 값은 False.

if __name__ == "__main__":
    main()