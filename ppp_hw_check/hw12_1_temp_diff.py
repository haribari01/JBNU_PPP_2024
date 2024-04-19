from hw11_5_year_rainfall import read_col, read_col_int

def get_data_ifs(values, conditions, criteria):
    return [value for value, year in zip(values, conditions) if year == criteria]

def main():
    filename = "weather(146)_2001-2022.csv"
    tmax = read_col(filename, 3)
    tmin = read_col(filename, 5)
    years = read_col_int(filename, 0)
    months = read_col_int(filename, 1)
    days = read_col_int(filename, 2)

    for year in range(2001, 2023):
        temp_diff = get_data_ifs([tx - tn for tx, tn in zip(tmax, tmin)], years, year)
        max_diff = max(temp_diff)
        max_index = temp_diff.index(max_diff)
        # print(max_index)
        print(f"{year}년 최대 일교차는 {max_diff:.1f}℃이며, 그 날짜는 {months[max_index]:02d}/{days[max_index]:02d}입니다.")

# index - 중복값이 있는경우 enumerate 사용 *시험 끝나고 해보기*

if __name__ == "__main__":
    main()