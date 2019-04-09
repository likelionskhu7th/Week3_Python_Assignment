class assignment:
    def __init__(self,name='',phone='',sex=''):
        self.name = name
        self.phone = phone
        self.sex = sex
    def __str__(self):
        return "이름은 {}, 전화번호는 {}, 성별은 {} 입니다." .format(self.name,self.phone,self.sex)


phone_book_list = []
while(1):
    name = input('이름을 입력하세요 : ')
    if(name == '그만'):
        break
    phone = input('전화번호를 입력하세요 : ')
    sex = input('성별을 입력하세요 (male이나 female로 작성해주세요) : ')
    if(sex == 'male'):
        sex = 'male'   
    elif(sex == 'female'):
        sex = 'female'   
    else:
        sex = 'unknown'
    phone_book_list.append( assignment(name,phone,sex) )
    for a in phone_book_list:
        print(a)
for a in phone_book_list:
    print(a)
