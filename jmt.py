# 맛집 고르기
# 한식, 중식, 일식 중 한가지 고르기(input)
# 1개 고르면 식당 이름을 1개 임의로 추천(list, random)
# list 여러개를 사용하고, 입력을 받아야 한다.
import random

kf = ["홍이네", "정이네", "연이네", "범이네", "국이네"]
cf = ["중화반점", "국풍각", "화양연화", "필각", "칭따오"]
jf = ["스시네", "오니기리", "참치와연어", "이라시예맛세", "곤니찌와"]

def choose_f() :
    hello = int(input("1.한식, 2.중식, 3.일식 중 한가지를 숫자로 입력해주세 : "))

    if hello is 1 :
        print(random.choice(kf))
    elif hello is 2 :
        print(random.choice(cf))
    elif hello is 3 :
        print(random.choice(jf))
    else :
        print("잘 못 입력하셨습니다.")
        choose_f()

choose_f()
