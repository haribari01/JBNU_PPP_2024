import math

def distance_two_points(base,height):
    distance = math.sqrt(base ** 2 + height ** 2)
    return distance

x1 = int(input("x1 값을 입력하세요"))
y1 = int(input("y1 값을 입력하세요"))
x2 = int(input("x2 값을 입력하세요"))
y2 = int(input("y2 값을 입력하세요"))
base = x2 - x1
height = y2 - y1

print(" 두 점 ({},{})와 ({},{}) 사이의 거리는 {}입니다. ".format(x1,y1,x2,y2,distance_two_points(base,height)))

