# 실습1번

import numpy as np

celsius = np.array([20.0, 25.0, 30.0, 35.0])

fahrenheit = celsius * 1.8 + 32

print("섭씨 온도:", celsius)
print("화씨 온도:", fahrenheit)

# =================================================================
# 실습2번

import numpy as np

arr = np.linspace(0, 100, 5)

step = arr[1] - arr[0]

print("균등 분할 배열:", arr)
print("각 값의 간격:", step)

# =================================================================
# 실습3번

import numpy as np

time_axis = np.arange(0, 10, 2)

time_axis_dense = np.arange(0, 10, 1)

print("2초 간격 시간축 배열:", time_axis)
print("2초 간격 시점 개수:", len(time_axis))

print("\n1초 간격 시간축 배열:", time_axis_dense)
print("1초 간격 시점 개수:", len(time_axis_dense))

# =================================================================
# 실습4번

import numpy as np

data = np.array([[10, 20, 30], 
                 [40, 50, 60]])

dim = data.ndim
shape = data.shape
size = data.size

print("차원:", dim)
print("형태:", shape)
print("개수:", size)

# ====================================================================
# 실습5번

import numpy as np

data = np.array([12.8, 25.3, 30.9, 42.1])
print("현재 자료형:", data.dtype)

int_data = data.astype(int)
print("변환된 정수 배열:", int_data)

# ========================================================================