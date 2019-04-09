class info:
    def __init__(self, name="", phone="", sex=""):
        self.name = name
        self.phone = phone
        self.sex = sex
    def setName(self):
        self.name = input("이름을 입력하세요 :")
    def setphone(self):
        self.phone = input("전화번호를 입력하세요 :")
    def setsex(self):
        self.sex = input("성별을 입력하세요(male이나 female로 작성해주세요) :")
        if self.sex != 'male' and self.sex != 'female':
            self.sex = 'unknown'
    def __str__(self):
        return '이름은 {}, 전화번호는 {} 성별은 {}'.format(self.name, self.phone, self.sex)

i = 0

objectList = list()
while (True):
    objectList.append(info())
    objectList[i].setName()
    if objectList[i].name == "그만":
        del objectList[i]
        for a in objectList:
            print(a)
        break
    objectList[i].setphone()
    objectList[i].setsex()
    for a in objectList:
        print(a)
    i += 1