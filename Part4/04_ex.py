# 부울(bool) 변수 알아보기
# 부울변수는 플래그 변수 형태로 사용을 많이 한다.

# 타 프로그래밍 언어에서는 부울 변수의 값은 소문자로 시작하는 true, false를 사용하지만 파이썬은 대문자로 시작하는 True, False를 사용한다.
flag = True
print(type(flag))
print(flag)

flag = not flag
print(flag)

if flag:
  print("참이라서 실행됩니다.")
else:
  print("거짓이라서 실행됩니다.")
  flag = not flag


if flag:
  print("참이라서 실행됩니다.")
else:
  print("거짓이라서 실행됩니다.")
  flag = not flag
  