import math

weight = 60
height = 170
BMI = weight / math.pow((height/100), 2)
print("{}kg, {}cm 일때 BMI는 {:.2f}입니다.".format(weight, height, BMI))
