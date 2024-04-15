def read_col(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def total_rainfall_event(rainfall):
    rain_event = []
    prev_rain_count = 0
    prev_rain = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain)
            prev_rain_count = 0
            prev_rain = 0
        else:
            prev_rain_count += 1
            prev_rain += rain
            # 비가오는데 마지막날이다? 이벤트하나 추가해줌.
            if i == len(rainfall) - 1:
                rain_event.append(prev_rain)
    return max(rain_event)

def main():
    rainfall = read_col("weather(146)_2022-2022.csv", 9)
    print(f"강우이벤트 중 최대 강수량은 {total_rainfall_event(rainfall):.1f}mm 입니다. ")

if __name__ == "__main__":
    main()