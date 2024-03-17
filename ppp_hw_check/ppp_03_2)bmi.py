import math

weight = int(input("몸무게를 입력하세요."))
height = int(input("키를 입력하세요."))
BMI = weight / math.pow((height/100),2)

print("{}kg, {}cm 일때 BMI는 {:.2f}입니다.".format(weight, height, BMI))