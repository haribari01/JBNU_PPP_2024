from hw11_5_year_rainfall import read_col, read_col_int

# GDD = (평균온도 - 기준온도) 누적값.
def gdd_index(tavg, months, years, criteria):
    total_gdd = 0
    for i in range(len(tavg)):
        if years[i] == criteria and months[i] >= 4:
            temp = tavg[i]
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            total_gdd += eff_temp
            if total_gdd >= 200:
                return i

def main():
    filename = "weather(146)_2001-2022.csv"
    tavg = read_col(filename, 4)
    years = read_col_int(filename, 0)
    months = read_col_int(filename, 1)
    days = read_col_int(filename, 2)

    for year in range(2001, 2023):
        gdd_index_200 = gdd_index(tavg, months, years, year)
        #print(f"{year}년 {months[gdd_index_200]:02d}월 {days[gdd_index_200]:02d}일에 누적 GDD가 200을 넘었습니다.")
        print(f"{years[gdd_index_200]}년 {months[gdd_index_200]:02d}월 {days[gdd_index_200]:02d}일에 누적 GDD가 200을 넘었습니다.")

if __name__ == "__main__":
    main()

# GDD가 200이 넘는 날짜
#2001년 4월 25일
#2003년 4월 26일