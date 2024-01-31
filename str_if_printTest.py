# standard library (표준 라이브러리)
# 1. math 모듈
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi) # 변수 또한 호출가능

# 2. random 모듈
import random

# 0.0과 1.0 사이의 랜덤 수가 리턴됨 
print(random.random())

# 3. os 모듈
import os
# 로그인 계정
print(os.getlogin())
# 설치 파일 경로
print(os.getcwd())
