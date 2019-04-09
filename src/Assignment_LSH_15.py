class Contact:
    def __init__(self, name, phone_number,sex):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex


def set_contact():
    
    name = input("이름을 입력하세요: ")
    if name=='그만':
        return -1
    phone_number = input("전화번호를 입력하세요: ")
    sex = input("성별을 입력하세요(male과 female로): ")
    contact = Contact(name, phone_number, sex)
    return contact

humanList=[]
def run():
  #  contact_list = []
    while True:

        contact = set_contact()
        if contact==-1:
            for human in humanList:
                print(human)
            break
        if contact.sex != 'male' and contact.sex!= 'female':
            contact.sex = 'unknown'
       
        str = '이름은 {}, 전화번호는 {}, 성별은 {}입니다.'.format(contact.name, contact.phone_number, contact.sex)
        humanList.append(str)
        for human in humanList:
            print(human)
    
       # contact_list.append(contact)
       

     

if __name__ == "__main__":
    run()