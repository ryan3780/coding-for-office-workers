# 가위 바위 보 만들기
# 3번 이기거나 3번 지면, 최종 스코어 보여주고, 끝!!
import random

pocket = [1, 2, 3]

def fight() :

    win_count = 0
    lose_count = 0
    draw = 0
# 변수 result 사용해서 print문의 중복을 피하고 싶은데, 방법이 안 떠오르네요 ㅠ
    result = ""
    print("환영합니다. 마르코 :-)")
    while True :

        input_h = int(input("1.가위 2.바위 3.보 중에 선택 : "))
        input_b = random.choice(pocket)

        if input_h != 1 and input_h != 2 and input_h != 3:
            print("잘못 입력하셨어요")

        elif input_h == 1 and input_b == 3 :
            win_count = win_count + 1
            print("승")


        elif input_h == 2 and input_b == 1:
            win_count = win_count + 1
            print("승")

        elif input_h == input_b :
            draw = draw + 1
            print("무")

        else :
            lose_count = lose_count + 1
            print("패")

        if win_count == 3 :
            print("승리 : " + str(win_count), '\n'"무 : " + str(draw), '\n' "패 : " + str(lose_count), '\n' "마르코 승리입니다...쳇")
            break

        elif lose_count == 3 :
            print("제가 이겼군요 훗.")
            break

fight()
