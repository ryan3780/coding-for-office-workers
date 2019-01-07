# 구구단!!
def gugu():
    a = int(input("몇 단이요?"))
    for i in range(1,10):
        print("{} * {} = {}".format(a,i,a*i))

gugu()

# 5x5 2차원 배열
# a = [[i for i in range(j, j+5)] for j in range(1, 26, 5)]
#
# for item in a :
#     print(item)
