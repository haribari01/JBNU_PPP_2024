# [구구단]
n = int(input("구구단 몇단?"))

for i in range(9):
    print(f"{n}*{i+1}={n*(i+1)}")

# [구구단(10단 이상부터 n번째까지 곱함.)]
n = int(input("구구단 몇단?"))

if 1 <= n and n <= 9:
    for i in range(9):
        print(f"{n}*{i+1}={n*(i+1)}")
else:
    for i in range(n):
        print(f"{n}*{i+1}={n*(i+1)}")
