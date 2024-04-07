def main():
    with open("number1.txt") as f:
        nums = []
        for line in f:
            tokens = line.strip().split()
            for token in tokens:
                nums.append(int(token))

    #print(nums)
    print("총 숫자의 개수는", len(nums))
    if len(nums) != 0:
        average = sum(nums) / len(nums)
        print(f"주어진 숫자의 평균은 {average}")
    else:
        print("주어진 숫자 없음")
    print("주어진 숫자의 최댓값은", max(nums))
    print("주어진 숫자의 최솟값은", min(nums))
    #홀수개
    if len(nums) % 2 != 0:
        print("중앙값은", sorted(nums)[len(nums) // 2])
    #짝수개
    else:
        mid = len(nums) // 2
        print("중앙값은", (sorted(nums)[mid-1] + sorted(nums)[mid])/2)

if __name__ == "__main__":
    main()