import os
import requests

url = "http://api.taegon.kr/stations/146/?sy=2022&ey=2022&format=csv"

filename = "weather_146_2020.csv"
# filename만 2020으로 바꿔서 불러왔는데 값이 2022파일과 동일합니다. 잘못불러온건지 2020파일값이 2022파일과 동일한것인지 모르겠습니다.

if not os.path.exists(filename):
    with open(filename, "w") as f:
        res =requests.get(url)
        f.write(res.text)

with open(filename, "r") as f:
    lines = f.readlines()

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