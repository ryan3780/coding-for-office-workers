# 과제 2 - 회사 조직도 만들기

# 클래스 생성

class Human :

    def __init__(self, name, age, sex) :
        self.name = name
        self.age = age
        self.sex = sex


class Dhuman(Human):
    rank = "manager"

human1 = Human("fate", 31, "male")
human2 = Dhuman("ele",32,"male")
print(human2.name, human2.age, human2.sex, human2.rank)
print(human1.name, human1.age, human1.sex)
