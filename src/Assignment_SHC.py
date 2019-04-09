list_name = list()
list_pnumber = list()
list_sex = list()

class information:
    def __init__(self, name="asd", phone_number="asd", sex="asd"):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex

    def save_name(self, name):
        list_name.append(name)

    def save_phone_number(self, phone_number):
        list_pnumber.append(phone_number)

    def save_sex(self, sex):
        list_sex.append(sex)

a = information()
while True:
    name = input("이름을 입력하세요: ")
    if name == "그만":
        break
    else:
        a.save_name(name) 
    
    phone_number = input("전화번호를 입력하세요: ")
    a.save_phone_number(phone_number)
    
    sex = input("성별을 입력하세요: ")
    if sex=="male" or sex=="female":
        a.save_sex(sex)
    
    else:
        list_sex.append("unknown")

    times = len(list_name)
    
    i = 0
    while i < times:
        print("이름은 "+list_name[i]+", 전화번호는 "+list_pnumber[i]+", 성별은 "+list_sex[i]+"입니다.")
        i += 1

x = 0
while x < times:
    print("이름은 "+list_name[x]+", 전화번호는 "+list_pnumber[x]+", 성별은 "+list_sex[x]+"입니다.")
    x += 1