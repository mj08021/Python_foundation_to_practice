# 문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = " Min Ji"
last_name = "Kim"

name = last_name + first_name
print(name)

# 같은 데이터 타입으로만 연결이 가능합니다.
temp = "Person" + str(100)
print(temp)

temp = "Person" + str(100.188)
print(temp)

# 문자열을 숫자로 변환
price = int("123456")
print(type(price))
print(price)

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복이된다.
arrow = "->" * 10
print(arrow)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있을 경우 이런 형식을 지정하여 출력.
# %s에 정수 대입
price = 1000
print("가격 : %s" % price)

# %s에 문자열 대입
time = "13:49"
print("현재 시간 : %s" % time)

# %s를 2개 이상을 사용하고자 할 때는 해당하는 %s의 개수 만큼 소괄호로 묶어서 형식 지정자에 대입
temp = "현재 시간은 %s시 %s분 %s초 입니다."
print(temp % (10, 38, 12))
