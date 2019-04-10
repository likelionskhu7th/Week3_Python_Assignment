class intro:
    def __init__(self, name="unknown", number="unknown", sex="unknown"):
        self.name = name
        self.number = number
        self.sex = sex

humanList = []
while True:
    a = intro()
    a.name = input('이름을 입력하세요 : ')
    if a.name == '그만':
        for human in humanList:
            print(human)
        break
    a.number = input('전화번호를 입력하세요 : ')
    a.sex = input('성별을 입력하세요(male이나 female로 작성해주세요) : ')
    if a.sex != 'male' and a.sex != 'female':
        a.sex='unknown'
    str = '이름은 {}, 전화번호는 {}, 성별은 {}입니다.'.format(a.name, a.number, a.sex)
    humanList.append(str)

    for human in humanList:
        print(human)
    print()