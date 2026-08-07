# except들의 연속과 finally 코드

# text ="24.5" # 정상
text = "영크크" # 비정상

try:
  temp = float(text)

except ValueError:
  print("ValueError문제가 발생했습니다")
  temp = 0
except NameError:
  print("NameError 문제가 발생했습니다")
finally:
  # 오류가 있건 없건 fianally의 코드를 실행해 마무리
  print(temp * 2)

# =================================================================
# continue
# 반복문 안에서 예외처리

my_list = ["123", "456", "영크크", "32", "53"]

# 문제가 

for text in my_list:
   # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고
   # 게속 빈복을 이어서 진행시키기

    try:
      my_number = int(text)
    except:
     print("문제발생")
     # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안되겠다
     # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

     # 갈 때 가더라도 문제상황 카운팅 정도는 좋잔아
     problems += 1

     continue

    print(my_number)

print(f"{problems}개는 문제가 있어서 건너뜀")

# ============================================================================
