class likelion():
    def __init__(self, name, phonenumber, sex):
        self.name = name
        self.phonenumber = phonenumber
        self.sex = sex

lionmember = []
while True:
    name = input('이름을 입력하세요:') 
    if name =='그만':
        for members in lionmember:
            print('이름은 {},전화번호는 {},성별은 {}입니다.'.format(members.name, members.phonenumber, members.sex))
        break
    phonenumber = input('전화번호를 입력하세요:')
    sex = input('성별을 입력하세요:') 
        
    if sex == 'male':
        pass
    elif sex == 'female':
        pass
    else:
        sex = 'unknown'
    member = likelion(name, phonenumber, sex)
    lionmember.append(member)
    for members in lionmember: 
        print('이름은 {},전화번호는 {},성별은 {}입니다.'.format(members.name, members.phonenumber, members.sex))