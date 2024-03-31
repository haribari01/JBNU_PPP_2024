# [list 함수]
def get_range_list(n):
    return list(range(1,n+1))

def main():
    n = int(input("1부터 몇까지?"))
    print(f"1부터 {n}까지 리스트로 표현하면 {get_range_list(n)}")

if __name__ == "__main__":
    main()

# [append 활용]
def get_range_list(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list

def main():
    n = int(input("1부터 몇까지?"))
    print(f"1부터 {n}까지 리스트로 표현하면 {get_range_list(n)}")

if __name__ == "__main__":
    main()
