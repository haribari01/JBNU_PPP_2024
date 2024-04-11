def read_col(filename, col_idx):
    results = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            results.append(value)
    return results

def average(tavg):
    if len(tavg) != 0:
        return sum(tavg) / len(tavg)
    else:
        return None
def rain_day(rainfall):
    count = 0
    for i in range(len(rainfall)):
        if rainfall[i] >= 5 :
            count += 1
    return count
# ->rainfall 은 리스트
def total_rainfall(rainfall):
    return sum(rainfall)

def main():
    tavg = read_col("weather(146)_2022-2022.csv", 4)
    rainfall = read_col("weather(146)_2022-2022.csv", 9)
    print(f"연평균 기온은 {average(tavg):.1f}입니다.")
    print(f"5mm이상 강우일수는 {rain_day(rainfall)}일 입니다.")
    print(f"총 강우량은 {total_rainfall(rainfall):.1f}입니다.")

if __name__ == "__main__":
    main()
