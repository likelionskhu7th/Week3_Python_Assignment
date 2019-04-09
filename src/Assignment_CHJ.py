class data:
    list1 = []
    
    def setdata(self, name, number, sex):
        self.x = name
        self.y = number
        self.z = sex
        self.list1 = [self.x,self.y,self.z]
    
a = data()
b = []

while True :
    
    name = input("이름을 입력하세요 : ")
    if name == '그만':
        break
    number = input("전화번호를 입력허세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if sex != 'male' and sex != 'female':
        sex = "unknwon"
    a.setdata(name, number, sex)
    b.append(a.list1)
    for i in range(len(b)):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." %(b[i][0], b[i][1],b[i][2]))
for i in range(len(b)):
     print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." %(b[i][0], b[i][1],b[i][2]))