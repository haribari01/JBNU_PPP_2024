import math

weight = int(input("몸무게를 입력하세요."))
height = int(input("키를 입력하세요."))
BMI = weight / math.pow((height/100),2)

if 23 <= BMI <25:
    print("{}kg, {}cm 일때 BMI는 {:.1f}이고 비만 전단계입니다.".format(weight,height,BMI))
elif 25 <= BMI <30:
    print("{}kg, {}cm 일때 BMI는 {:.1f}이고 1단계 비만입니다.".format(weight,height,BMI))
elif 30 <= BMI <35:
    print("{}kg, {}cm 일때 BMI는 {:.1f}이고 2단계 비만입니다.".format(weight, height,BMI))
elif 35 <= BMI:
    print("{}kg, {}cm 일때 BMI는 {:.1f}이고 3단계 비만입니다.".format(weight,height, BMI))
else :
    print("정상 또는 저체중입니다.")