# 파이썬에서의 자료형(Data-type)

# int형을 출력해봄
print(type(17))

#float형을 출력해봄
print(type(10.77779))

# str형을 출력해봄
print(type("안녕하세요."))


# 반지름이 r인 구의 부피는 4/3 * pi * r ** 3
# 반지름이 5인 구의 부피를 계산하는 프로그램
from math import *
r = 5.0
volume = 4.0 / 3.0 * pi * r ** 3
print("구의 부피 : ", volume)

# 구의 겉넓이 공식 : 4 * pi * r ** 2
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 : ", outer_area)