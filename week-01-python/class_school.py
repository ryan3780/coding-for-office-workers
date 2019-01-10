# What is the class? school 클래스 만들기

class School :
    open = "24 hour"
    close = "never"
    like_count = 0

    def __init__(self, name, esb_y, address) :
        self.name = name
        self.esb_y = esb_y
        self.address = address

    def read(self) :
        self.like_count = self.like_count + 1

school1 = School("ele", "1988", "Korea")
school2 = School("jenny", "1992", "Korea")
school3 = School("dana", "1996", "korea")

school1.read()
print(school1.name, school1.esb_y, school1.address)
print(school1.like_count)
school2.read()
print(school2.name, school2.esb_y, school2.address)
print(school2.like_count)
school3.read()
print(school3.name, school3.esb_y, school3.address)
print(school3.like_count)
