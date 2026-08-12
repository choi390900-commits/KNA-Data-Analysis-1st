# 실습1번
import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")

try:
  df = pd.read_csv(filepath, encoding="utf-8", sep=",", index_col="측정시각", nrows=5,
                    usecols=["측정시각", "가동상태"])
  print(df.shape)

  print(df.head(8))
except FileNotFoundError:
  print(f"파일이 없습니다 : {filepath}")

# ====================================================================================
# 실습2번

import pandas as pd

df_ss = pd.read_csv('data/12_metro_compressor.csv', encoding='utf-8')
print(df_ss.head(10))
print(df_ss.shape)

# ==================================================================================
# 실습3번

import pandas as pd

df = pd.read_csv('data/12_metro_compressor_semicolon.csv', sep=';', encoding='utf-8')
print(df.sh)
print(df.head(6))

# =============================================================================
# 실습4번

import pandas as pd

df = pd.read_csv('data/12_metro_compressor.csv',
                 usecols=['측정시각', '오일온도', '모터전류', '가동상태'])
print(df.sp)
print(df.head(5))

# ======================================================================
# 파일 : data 폴더 안의 12_metro_compressor_semicolon.csv
# sep를 잘 사용해서 여러 컬럼이 읽히도록 해주세요
# encoding도 지정해주세요
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요