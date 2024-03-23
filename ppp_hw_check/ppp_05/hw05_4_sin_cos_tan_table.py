# [삼각함수 표 만들기]
import math
for i in range(91):
    radians = math.radians(i)
    sin = math.sin(radians)
    cos = math.cos(radians)
    tan = math.tan(radians)
    print(f"각도:{i}°,라디안:{radians:.4f},sin:{sin:.4f},cos:{cos:.4f},tan:{tan:.4f}")

# [15도 단위로 삼각함수 표 만들기]
import math
for i in range(0,91,15):
    radians = math.radians(i)
    sin = math.sin(radians)
    cos = math.cos(radians)
    tan = math.tan(radians)
    print(f"각도:{i}°,라디안:{radians:.4f},sin:{sin:.4f},cos:{cos:.4f},tan:{tan:.4f}")