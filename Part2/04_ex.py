# 한 사람의 돈이 5000원이 있는데 사탕의 가격이 120원이라면 최대로 살 수 있는 사탕의 수는?

myMoney = 5000
candyPrice = 120

# 최대로 살 수 있는 사탕의 개수
# / : 실수, // : 정수
numCandies = myMoney // candyPrice
print("최대로 살 수 있는 사탕의 개수 : ", numCandies)

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
change = myMoney % candyPrice
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ", change)