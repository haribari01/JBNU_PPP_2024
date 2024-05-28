import os
import requests
import matplotlib.pyplot as plt
def download(filename, URL):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig") as f:
            res = requests.get(URL)
            f.write(res.text.replace("\r", ""))

def read_col_float(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            if len(tokens) > col_idx and tokens[col_idx] != '':
                dataset.append(float(tokens[col_idx]))
            else:
                dataset.append(None)
    return dataset

def read_col_str(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            if len(tokens) > col_idx and tokens[col_idx] != '':
                dataset.append(str(tokens[col_idx]))
            else:
                dataset.append(None)
    return dataset

def summer_tmax(dates, temps):
    dataset = []
    for date, temp in zip(dates, temps):                                                # yyyy-mm-dd 형태
        if date is not None and temp is not None and date[5:7] in ['06', '07', '08']:   # date[5:7}은 month 문자열 추출
            dataset.append(temp)
    return dataset

def winter_tmin(dates, temps):
    dataset = []
    for date, temp in zip(dates, temps):
        if date is not None and temp is not None and date[5:7] in ['12', '01', '02']:
            dataset.append(temp)
    return dataset

def main():
    start_year = 1980
    end_year = 2023
    # start_month = 01
    # end_month = 12
    # start_day = 01
    # end_day = 31
    # -> start_month 와 start_day에 01을 넣어줘야하는데 01로 적으면 SyntaxError 나옴.
    # -> 그래서 그냥 1로 진행해봤는데 숫자값이 아닌 한글만 나옴.  => 나중에 시간 나면 해보기.

    URL = (f"https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt={start_year}0101&endDt={end_year}1231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay={start_year}0101&startYear={start_year}&endDay={end_year}1231&endYear={end_year}&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=")
    filename = "weather(146)_1980-2023.csv"
    download(filename, URL)
    date = read_col_str(filename, 0)
    tmax = read_col_float(filename, 4)
    tmin = read_col_float(filename, 3)
    # tavg = read_col_float(filename, 2)

    summer = summer_tmax(date, tmax)
    winter = winter_tmin(date, tmin)
    # print(summer)
    # print(len(summer))
    # print(winter)
    # print(len(winter))

    plt.rcParams['font.family'] = ['NanumGothic']
    plt.rcParams['axes.unicode_minus'] = False   #마이너스(-) 기호표시 ->폰트나 길이 달라지는거 방지.
    plt.hist(summer, bins=20, color="red", label="1980-2023 여름철 최고기온 분포")
    plt.hist(winter, bins=20, color="b", label="1980-2023 겨울철 최저기온 분포")
    plt.xlabel("기온(℃)")
    plt.ylabel("빈도")    # 90도 회전시키고 싶은데 -> 나중에 해보기
    plt.legend()   #-> 범례설정
    plt.show()

if __name__ == "__main__":
    main()
