x = int(input("x 값을 입력하세요."))
y = int(input("y 값을 입력하세요."))

if x > 0 :
    if y > 0 :
        print("입력한 좌표 ({},{})는 제 1사분면입니다.".format(x,y))
    elif y < 0 :
        print("입력한 좌표 ({},{})는 제 4사분면입니다.".format(x,y))
    else :
        print("입력한 좌표 ({},{})는 x축 위에 있습니다.".format(x,y))
elif x < 0 :
    if y > 0 :
        print("입력한 좌표 ({},{})는 제 2사분면입니다.".format(x,y))
    elif y < 0:
        print("입력한 좌표 ({},{})는 제 3사분면입니다.".format(x,y))
    else :
        print("입력한 좌표 ({},{})는 x축 위에 있습니다.".format(x,y))
else :
    if y != 0 :
        print("입력한 좌표 ({},{})는 y축 위에 있습니다.".format(x,y))
    else :
        print("입력한 좌표 ({},{})는 원점입니다.".format(x,y))