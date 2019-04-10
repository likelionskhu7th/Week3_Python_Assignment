class contact:
    def __init__(self, name, phone_number, sex):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex

result = []
while True:
    name = input("이름을 입력하세요 : ")
    if name == "그만":
        for i in result:
            print("이름은" + i.name + "전화번호는" + i.phone_number + "성별은" + i.sex)
        break
    phone_number = input("전화번호를 입력하세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")

    if sex != "male" and sex != "female" :
        sex = "unknown"

    print("이름은" + name + "전화번호는" + phone_number + "성별은" + sex)

    person = contact(name, phone_number, sex)
    result.append(person)
    for i in result:
        print("이름은" + i.name + "전화번호는" + i.phone_number + "성별은" + i.sex)