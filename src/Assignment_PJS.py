class Info:
    def __init__(self):
        self.name = []
        self.number = []
        self.sex = []

    def add_name(self, name):
        self.name.append(name)

    def add_number(self, number):
        self.number.append(number)

    def add_sex(self, sex):
        if sex != "male" and sex != "female":
            self.sex.append("unknown")
        else:
            self.sex.append(sex)

    def result_print(self):
        for i in range(0, len(self.name)):
            print("이름:" + self.name[i] + " 전화번호는:" + self.number[i] + " 성별은:" + self.sex[i])
        print("\n")
        


info = Info()

while True:
    """
    반복입력 받기
    이름을 입력하세요:
    전화번호를 입력하세요:
    성별을 입력하세요:
    """
    name_input = input("이름을 입력하세요:")
    if name_input != "그만":
        info.add_name(name_input)
        number_input = input("전화번호를 입력하세요:")
        info.add_number(number_input)
        sex_input = input("성별(male or female)을 입력해주세요:")
        info.add_sex(sex_input)
        info.result_print()
        continue
    else:
        info.result_print()
        break