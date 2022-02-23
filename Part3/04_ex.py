# 문자열에 대한 실습

# 큰따옴표(double quotation marks)으로 묶으면 문자열이 된다. (권장)
welcome = "Happy New Year 2022"
print(welcome)

# 작은따옴표(single quotation marks)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2022'
print(welcome)


message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하도가 할 때, \를 이용한다.
# \가 따옴표 앞에 있으면 '는 특수한 의미를 잃어버리고 하나의 문자로 편승이 되어 문자열을 이룬다.
message = 'dosen\'t'
print(message)

message = "\"yes\", I can do it"
print(message)

# 특수문자 형태인 \n은 개행(Enter)을 하는 문자이다.
message = "First\nSecond\nThird"
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자이다.
message = "c:\temp\name"
print(message)

# \t, \n 등의 이스케이프 문자들의 기능을 제거하기 위해서는 문자열 시작 앞에 r을 붙여준다.
message = r"c:\temp\name"
print(message)

# 문자열(영어나 한글 상관 없음)의 길이를 알고자 한다면 len() 함수를 이용한다.
message = "신은혁"
print("문자열의 길이 : ", len(message))