import math

r = int(input("반지름을 입력하세요."))
circle_area = math.pi * r ** 2

print("반지름이 {}일때 원의 넓이는 {:.2f}입니다.".format(r, circle_area))
