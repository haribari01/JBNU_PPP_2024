def average(nums):
    if len(nums) != 0:
        return sum(nums) / len(nums)
    else:
        return 0
# average 함수 작동 안함.
# 리스트 안에 숫자가 없는 경우 분모가 0이됨.

def main():
    nums = [3, 5, 7, 2, 6, 9, 4]
    # nums = []
    # nums = [2,4,6,8]
    print(f"평균은 {average(nums):.2f}입니다.")

if __name__ == "__main__":
    main()