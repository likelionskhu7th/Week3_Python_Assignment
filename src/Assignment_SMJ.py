class person:

    def __init__(self, name, phone, sex):
        self.name = name
        self.phone = phone
        self.sex = sex

people = []

def printAll():
    for human in people:
        print('이름은 {}, 전화번호는 {}, 성별은 {} 입니다. \n'.format(human.name, human.phone, human.sex))

while True:
    name = input('이름을 입력하세요 : ')
    if(name == '그만'):
        printAll()
        break
    phone = input('전화번호를 입력하세요 : ')
    sex = input('성별을 입력하세요 : ')
    if sex != 'female' and sex != 'male':
        sex = 'unknown'
    people.append(person(name,phone,sex))      
    printAll()