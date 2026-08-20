# 실습1번

import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")

corr_value = df['지표07'].corr(df['지표08'])
print(f"지표07-08 상관계수: {corr_value:.3f}") 

selected_columns = ['지표05', '지표06', '지표07', '지표08']
corr_matrix = df[selected_columns].corr()

print("\n네 열의 상관 행렬:")
print(corr_matrix.round(3))

# ==================================================================
# 실습2번

import pandas as pd

corr_matrix = df[selected_columns].corr()

strong_pairs = []
threshold = 0.4 

cols = corr_matrix.columns
for i in range(len(cols)):
    for j in range(i + 1, len(cols)): 
        col1 = cols[i]
        col2 = cols[j]
        corr_val = corr_matrix.iloc[i, j]
        
        if abs(corr_val) >= threshold:
            strong_pairs.append((col1, col2, corr_val))

strong_pairs.sort(key=lambda x: abs(x[2]), reverse=True)

print(f"절댓값 {threshold} 이상 쌍 {len(strong_pairs)}개 출력:")
for pair in strong_pairs:
    print(f"{pair[0]}-{pair[1]} : {pair[2]:.3f}")

# ==================================================================
# 실습3번

import pandas as pd

overall_corr = df['지표07'].corr(df['지표08'])

df_pass = df[df['판정'] == '합격']
df_fail = df[df['판정'] == '불합격']

pass_corr = df_pass['지표07'].corr(df_pass['지표08'])
fail_corr = df_fail['지표07'].corr(df_fail['지표08'])

fail_count = len(df_fail)

print(f"전체 상관: {overall_corr:.3f}")
print(f"합격 그룹 상관: {pass_corr:.3f}")
print(f"불합격 그룹 상관: {fail_corr:.3f} (불합격 {fail_count}건 주의)")

