from hw11_5_year_rainfall import read_col, read_col_int

# GDD = (평균온도 - 기준온도) 누적값.
def gdd_season(tavg, months, years, criteria):
    total_gdd = 0
    for temp, month, year in zip(tavg, months, years):
        if year == criteria and month in [5, 6, 7, 8, 9]:
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            total_gdd += eff_temp
    return total_gdd

def main():
    filename = "weather(146)_2001-2022.csv"
    tavg = read_col(filename, 4)
    years = read_col_int(filename, 0)
    months = read_col_int(filename, 1)

    for year in range(2001, 2023):
        gdd = gdd_season(tavg, months, years, year)
        print(f"{year}년 5~9월까지 GDD는 {gdd:.1f}입니다.")

if __name__ == "__main__":
    main()

#5~9월 적산온도
#2001년  2873.8
#2003년  2653.1