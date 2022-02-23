# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는 문자에 번호(인덱스)가 존재한다
# [인덱스]하면 문자열에서 문자를 추출할 수 있다.
# 인덱스는 무조건 0부터 시작된다. 마지막 인덱스는 n-1이 된다.
# 파이썬 특수기능인 인덱스를 처리할 때 음수도 사용이 가능하다.

word = "Python"
print(len(word))

print(word[0])
print(word[5])

# len(word)는 문자열의 길이인 6을 반환하기 때문에 -1을 해주면 끝문자를 반환해준다.
print(word[len(word) - 1])

# 파이썬에서는 한 번 작성된 문자열은 변경이 불가능하다.
# word[2] = "B"

# 사용자로부터 문자열 입력을 3개를 받도록 한다. 각 해당 문자열의 첫 번째 문자를 인덱싱하여 문자를 합쳐서 문자열로 만드는 프로그램을 만들어 보자
item1 = input("첫 번째 단어를 입력하시오 : ")
item2 = input("두 번째 단어를 입력하시오 : ")
item3 = input("세 번째 단어를 입력하시오 : ")

# 위의 3개의 문자열 중 첫 번째 단어만 추출하여 또 다른 문자열을 만들고 있다.
word = item1[0] + item2[0] + item3[0]
print("새로 만든 문자열 : ", word)