import os
import requests

url = "http://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

filename = "weather_146_2020.csv"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        res =requests.get(url)
        f.write(res.text)

with open(filename, "r") as f:
    lines = f.readlines()
# 연평균기온을 구하고 파일을 불러온 후 다음 5mm이상 강우일수를 구할때 오류가 납니다. 그래서 파일을 지웠다가 결과를 보고 다시 지웠다가 결과를 보는식으로
# 과제를 진행했는데 index부분에서 오류가 나는것 같습니다.
# 과제에 있는 3가지 문제의 결과를 파일에 저장한 후 새로운 결과값을 추가하고 저장하고 싶으면 파일을 지웠다가 다시 받는 방법말고 어떤방법으로 진행해야할까요?

tavg_list = []
rainfall_list = []
for line in lines[1:]:
    tokens = line.strip().split(",")
    tavg = float(tokens[4])
    rainfall = float(tokens[9])
    tavg_list.append(tavg)
    rainfall_list.append(rainfall)

average_tavg = sum(tavg_list) / len(tavg_list)
rain_day = sum(1 if rainfall >= 5 else 0 for rainfall in rainfall_list)
total_rainfall = sum(rainfall_list)

result = (
    f"\n연 평균 기온: {average_tavg:.1f}°C\n"
    f"5mm이상 강우일수 : {rain_day}일 \n"
    f"총 강우량: {total_rainfall:.1f} mm\n"
)

with open(filename, "a") as f:
    f.write(result)
