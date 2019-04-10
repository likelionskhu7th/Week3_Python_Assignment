import sys
human_list=[]

class human:
    def __init__(self,name,phone,sex):
        self.name = name
        self.phone = phone
        self.sex = sex


    def print_infow(self):
        print("이름은",self.name, "전화번호는",self.phone, "성별은",self.sex, "입니다")


def set_contact():
    name =input("이름을 입력하세요: ")
    if(name == "그만"):
        return "그만"
    phone =input("전화번호를 입력하세요:")
    sex = input("성별을 입력하세요: ")
    if ((sex != "male") and (sex != "female")):
        sex = "unknown"
    contact = human(name,phone,sex)
    return contact

while(1):
    contact = set_contact()
    human_list.append(contact)
    for i in human_list:
        i.print_infow()
        if(i.name == "그만"):
            sys.exit()