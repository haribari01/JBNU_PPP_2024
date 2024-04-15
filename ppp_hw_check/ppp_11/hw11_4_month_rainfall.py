def read_col(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def read_col_int(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_idx]))
    return dataset

def sumifs(rainfall, months, conditions):
    total = 0
    for rain, month in zip(rainfall, months):
        if month in conditions:
            total += rain
    return total

def main():
    rainfall = read_col("weather(146)_2022-2022.csv", 9)
    months = read_col_int("weather(146)_2022-2022.csv", 1)
    print(f"여름철(6-8월) 총 강수량은 {sumifs(rainfall, months, [6, 7, 8]):.1f}mm 입니다.")

if __name__ == "__main__":
    main()
