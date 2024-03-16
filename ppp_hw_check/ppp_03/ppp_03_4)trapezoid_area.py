top = int(input("윗변의 길이를 입력하세요."))
base = int(input("밑변의 길이를 입력하세요."))
height = int(input("높이를 입력하세요."))

trapezoid_area = (top + base) * height / 2

print("윗변{},밑변{},높이{}일때 사다리꼴의 면적은{}입니다.".format(top, base, height, trapezoid_area))

