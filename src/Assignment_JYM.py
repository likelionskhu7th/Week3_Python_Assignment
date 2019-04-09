class assignment:
    '''전화번호 목록 프로그램'''
    def __init__(self, name, number, sex):   
        self.name =name
        self.number = number
        self.sex = sex
    def __str__(self):
        return "이름은 {}, 전화번호는 {}, 성별은 {} 입니다." .format(self.name,self.number,self.sex)

phone_book=[]   
while True:
    name = input("이름을 입력하세요 :")
    if name == "그만":
        break
    number = input("전화번호를 입력하세요 :")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) :")
    if sex == "male":
        sex ='male'
        
    elif sex == "female":
        sex = 'female'
    else: 
        sex = 'unknown'
    phone_book.append( assignment(name,number,sex) )
    for a in phone_book:
        print(a)
    
for a in phone_book:
    print(a)