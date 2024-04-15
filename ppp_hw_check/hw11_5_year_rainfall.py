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

def get_data_ifs(values, conditions, criteria):
    # 방법1
    # dataset = []
    # for rain, year in zip(values, conditions):
    #     if year == criteria:
    #         dataset.append(rain)
    # return dataset

    # 방법2
    return [rain for rain, year in zip(values, conditions) if year == criteria]

def main():
    # 방법1 (리스트 두개 값 비교해서 원하는거 뽑아냄)
    rainfall = read_col("weather(146)_2001-2022.csv", 9)
    year = read_col_int("weather(146)_2001-2022.csv", 0)
    rainfall_2021 = get_data_ifs(rainfall, year, 2021)
    rainfall_2022 = get_data_ifs(rainfall, year, 2022)
    print(f"2021년 총 강수량은 {sum(rainfall_2021):.1f}mm입니다.")
    print(f"2022년 총 강수량은 {sum(rainfall_2022):.1f}mm입니다.")

if __name__ == "__main__":
    main()