# 랜덤으로 리스트나, 튜플형 자료구조에서 하나의 값을 뽑기
import random

a =[]

def input_a() :
    for i in range(1,6):
        a.append(i)

input_a()
print(random.choice(a))
