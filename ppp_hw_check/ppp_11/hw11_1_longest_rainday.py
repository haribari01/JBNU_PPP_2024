def read_col(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def longest_rainday(rainfall):
    rain_event = []
    prev_rain_count = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
            # 비가오는데 마지막날이다? 이벤트하나 추가해줌.
            if i == len(rainfall) - 1:
                rain_event.append(prev_rain_count)
    return max(rain_event)

def main():
    rainfall = read_col("weather(146)_2022-2022.csv", 9)
    print(f"최장연속강우일수는 {longest_rainday(rainfall)}일 입니다.")

if __name__ == "__main__":
    main()
