def read_col(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def top_rank(values, limit):
    # 방법1
    return sorted(values)[-limit:][::-1]
    # 방법2
    # return sorted(values, reverse=True)[:limit]

def main():
    tmax = read_col("weather(146)_2022-2022.csv", 3)
    print(f"가장 더운날 top3 {top_rank(tmax,3)}입니다.")

if __name__ == "__main__":
    main()
