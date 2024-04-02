# [방법 1]
# def text2list(input_text):
#     tokens = input_text.split()
#     numbers = []
#     for token in tokens:
#         numbers.append(int(token))
#     return numbers

 # [방법 2] 지능형 리스트
def text2list(input_text):
    nums = [int(x) for x in input_text.split()]
    return nums

def average(nums):
    if len(nums) != 0:
        return sum(nums) / len(nums)
    else:
        return None

# 중앙값 : 크기 순서대로 놓았을 때 중앙에 있는 값.
def median(nums):
    return sorted(nums)[len(nums) // 2]
# 단, 갯수가 짝수일때는 중앙에 위치한 두 값 중 큰 값을 채택한다.
# ->2로 나눈 몫값을 인덱스로 쓰면 홀수/짝수 일때 식이 같아짐.

def minmax(nums):
    return min(nums), max(nums)


def main():
    input_text = "5 10 3 4 7"
    # input_text = "1 4 3 2 6 5"
    # input_text = "1 4 2 3"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print(f"평균값은 {average(nums):.1f}")
    print(f"중앙값은 {median(nums)}")
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")
if __name__ == "__main__":
    main()
