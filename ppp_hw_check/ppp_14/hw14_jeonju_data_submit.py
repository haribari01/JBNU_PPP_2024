import hw_submission
import requests
def download(filename, URL):
    with open(filename, "w", encoding="utf-8-sig") as f:
        res = requests.get(URL)
        f.write(res.text.replace("\r", ""))

# 9번째 줄부터 읽기 시작 & 데이터가 없는 경우 None으로 표시
def read_col(filename, col_idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            # if tokens[col_idx] != '':
            # ->이렇게 하면 오류남. => 인덱스가 실제로 존재하는지 tokens의 길이를 통해 확인해야함.
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
            if tokens[col_idx] != '':
            # date는 0번째라 그냥 이거 써도됨. 만약 공백 뒤에 date 값이 있다면 아래 코드사용.
            # if len(tokens) > col_idx and tokens[col_idx] != '':
                dataset.append(tokens[col_idx])
            else:
                dataset.append(None)
    return dataset

def main():
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename = "jeonju_all.csv"
    download(filename, URL)

    # date = read_col_str(filename, 0)
    # tmax = read_col(filename, 4)
    # tmin = read_col(filename, 3)

# ->  None이 있으면 max 계산 오류남. 따라서 None이 아닐때만 리스트에 값 추가

    # tmax_valid = [temp for temp in tmax if temp is not None]
    # max_temp = max(tmax_valid)
    # max_index = tmax.index(max_temp)
    # temp_diff = [tx-tn for tx, tn in zip(tmax, tmin) if tx is not None and tn is not None]
    # max_diff = max(temp_diff)
    # max_diff_index = temp_diff.index(max_diff)

    # print(tmax)
    # print(f"최고 기온은 {max_temp:.1f}℃이며, 그 날짜는 {date[max_index]}입니다.")
    # print(f"최대 일교차는 {max_diff:.1f}℃이며, 그 날짜는 {date[max_diff_index]}입니다.")
    # -> 최고 기온은 38.9℃이며, 그 날짜는 2018 - 08 - 13입니다.
    # -> 최대 일교차는 24.8℃이며, 그 날짜는 1939 - 04 - 10입니다.

    hw_submission.submit("김하종", 38.9, "2018-08-13", 24.8, "1939-04-10")

if __name__ == "__main__":
    main()
