#다이아몬드 구하기 !! 가지고 싶당...

for a in range(1,6):
    a = a - 3
    if a < 0 :
        a = -a
    print("0" * a + "1" * (5 - a * 2)+ "0" * a)
