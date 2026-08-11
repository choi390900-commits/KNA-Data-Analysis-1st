# 실습1번

import numpy as np

rpm = np.array([70, 72, 71, 95, 73, 68])

first_val = rpm[0]
last_val = rpm[-1]

front_section = rpm[1:4]
step_two = rpm[::2]

print("첫 시점 값:", first_val)
print("마지막 시점 값:", last_val)
print("앞 구간 값:", front_section)
print("두 칸 간격 값:", step_two)

# =======================================================================
# 실습2번

import numpy as np

sensor_data = np.array([
    [70, 2.1],  # 설비 0
    [72, 2.3],  # 설비 1
    [68, 2.0]   # 설비 2
])

specific_equipment = sensor_data[1]

rpm_column = sensor_data[:, 0]
torque_column = sensor_data[:, 1]

print("특정 설비(1번) 행 값:", specific_equipment)
print("모든 설비의 회전수 열:", rpm_column)
print("모든 설비의 토크 열:", torque_column)

# ================================================================================
# 실습3번

import numpy as np

rpm = np.array([70, 72, 71, 95, 73])

min_val = rpm.min()
max_val = rpm.max()

normalized_rpm = (rpm - min_val) / (max_val - min_val)

print("원본 회전수 배열:", rpm)
print(f"최솟값: {min_val}, 최댓값: {max_val}")
print("정규화된 배열:", np.round(normalized_rpm, 2))

# ============================================================================
# 실습4번

import numpy as np

rpm = np.array([70, 95, 71, 88, 73])
torque = np.array([2.1, 1.5, 2.2, 1.8, 2.3])

high_rpm_cond = rpm > 85
high_rpm_values = rpm[high_rpm_cond]

danger_cond = (rpm > 85) | (torque < 1.9)

danger_positions = np.where(danger_cond)[0] 

print("■ 단일 조건 필터링 결과")
print("기준 초과 회전수 값:", high_rpm_values)

print("\n■ 다중 조건 필터링 결과 (회전수 > 85 또는 토크 < 1.9)")
print("위험 조건 불리언 배열:", danger_cond)
print("위험 조건을 만족하는 위치(인덱스):", danger_positions)
print(f"위험 시점의 데이터 - 회전수: {rpm[danger_cond]}, 토크: {torque[danger_cond]}")

# ==================================================================================
# 실습5번

import numpy as np

torque = np.array([2.1, 1.5, 2.2, 1.8, 2.3])

cond = torque < 2.0


count = cond.sum()
ratio = cond.mean()

print("토크 배열:", torque)
print("조건 불리언 배열 (토크 < 2.0):", cond)
print("조건 만족 개수:", count)
print(f"전체 대비 비율: {ratio:.2f} ({ratio * 100:.0f}%)")

# ===============================================================================
# 실습6번

import numpy as np

sensor_data = np.array([
    [70, 2.1],
    [72, 2.3],
    [68, 2.0],
    [95, 1.5],
    [73, 2.2]
])

sensor_means = sensor_data.mean(axis=0)

sensor_stds = sensor_data.std(axis=0)

print("센서별 평균 (회전수, 토크):", np.round(sensor_means, 2))
print("센서별 표준편차 (회전수, 토크):", np.round(sensor_stds, 2))
print("-" * 40)
print(f"회전수 열 - 평균: {sensor_means[0]:.2f}, 표준편차: {sensor_stds[0]:.2f}")
print(f"토크 열   - 평균: {sensor_means[1]:.2f}, 표준편차: {sensor_stds[1]:.2f}")
# =========================================================================
# 실습7번

import numpy as np

rpm = np.loadtxt('rpm_data.txt')

rpm_mean = rpm.mean()
rpm_std = rpm.std()

rpm_min = rpm.min()
rpm_max = rpm.max()

print("■ 회전수 기초 통계 분석 결과")
print(f"평균: {rpm_mean:.2f}")
print(f"표준편차: {rpm_std:.2f}")
print(f"최솟값: {rpm_min}")
print(f"최댓값: {rpm_max}")
print(f"데이터 범위(Max - Min): {rpm_max - rpm_min}")