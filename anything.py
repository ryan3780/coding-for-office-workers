# def gugu():
#     a = int(input("몇 단이요?"))
#     for i in range(1,10):
#         print("{} * {} = {}".format(a,i,a*i))
#
# gugu()

# 코너가 말한 5x5 2차원 배열
a = [[i for i in range(j, j + 6)] for j in range(1, 36, 6)]


for item in a :
    print(item)
    
