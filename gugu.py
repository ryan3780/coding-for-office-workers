# 구구단!!
#에러 예외 처리 하기
def gugu():
    result = "2~9사이 숫자만 입력해주세요."

    try:
        a = int(input("몇 단이요?"))
        if a < 2 or a > 9:
            print(result)
            return gugu()

    except UnboundLocalError:
        print(result)
        return gugu()

    except ValueError:
        print(result)
        return gugu()

    else :
        for i in range(1,10):
            print("{} * {} = {}".format(a,i,a*i))

gugu()
