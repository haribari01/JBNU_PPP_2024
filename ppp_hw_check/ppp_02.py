"""[프원실] 과제 02"""

def c_to_f(celsius):
    return int(celsius * 9/5 + 32)
""" -> 계산 결과가 정수값인데 86.0℉로 나와서 int 함수 사용"""

c_temp_1 = 30
c_temp_2 = 0

f_temp_1 = c_to_f(c_temp_1)
f_temp_2 = c_to_f(c_temp_2)

print("1-1) 섭씨 {}℃는 화씨 {}℉입니다.".format(c_temp_1, f_temp_1))
print("1-2) 섭씨 {}℃는 화씨 {}℉입니다.".format(c_temp_2, f_temp_2))

print("---------------------------")

import random

def cal_BMI(weight, height):
    BMI = weight / (height ** 2)
    return BMI

weight = round(random.uniform(38, 101), 2)
height = round(random.uniform(1.38, 2.01), 2)

''' -> round 함수 안쓰면 BMI 값 오차 발생 '''

''' -> 병역판정검사 통계 기준 체중 38~101kg / 신장 1.38~2.01m (138~201cm) 로 범위 설정
https://kosis.kr/statHtml/statHtml.do?orgId=144&tblId=TX_14401_A007'''

BMI = cal_BMI(weight, height)

print("2) 몸무게{}kg, 키{}m 일때 BMI는{:.2f}입니다.".format(weight, height, BMI))

if BMI < 18.5:
    print("-> 저체중입니다.")
elif 18.5 <= BMI < 25:
    print("-> 정상입니다.")
elif 25 <= BMI < 30:
    print("-> 과체중입니다.")
elif 30 <= BMI < 35:
    print("-> 비만입니다.")
elif 35 <= BMI < 40:
    print("-> 고도비만입니다.")
else:
    print("-> 초고도비만입니다.")
""" -> 세계보건기구 기준 BMI 분류표. 하지만 BMI만으로 비만 판별 불가"""
print("---------------------------")

import math

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area
''' -> math.pi/np.pi/scipy.pi 결과값 같음'''

radius = 4

area = circle_area(radius)

print("3) 원의 면적은 {}π ≈ 약 {:.2f}입니다.".format(radius ** 2, area))
""" 소수점 아래2자리까지 반올림 해서 표시 """
print("---------------------------")

def trapezoid_area(base, top, height):
    area = (base+top) * height/2
    return area

base = 5
top = 3
height = 4

area = int(trapezoid_area(base, top, height))

print("4) 사다리꼴의 면적은 {}입니다.".format(area))



