# import ppp_02_bmi

# print(ppp_02_bmi.weight)
# print(ppp_02_bmi.height)
''' weight = 60, height = 170 인 파일(ppp_02_bmi)을 만들고 weight,height 두 값 모두 불러오는거 성공'''

# weight = int(input(ppp_02_bmi.weight))
# height = int(input(ppp_02_bmi.height))
# print("{}kg, {}cm.".format(weight, height))

""" Q: 불러온 값을 input에 넣으면 weight값만 나오는데 height값이 안나오는 이유를 모르겠습니다."""
import math

weight = 60
height = 170
BMI = weight / math.pow((height/100), 2)
print("{}kg, {}cm 일때 BMI는 {:.2f}입니다.".format(weight, height, BMI))
