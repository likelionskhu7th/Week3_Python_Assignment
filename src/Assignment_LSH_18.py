class cal:
    def __init__(self,name,phonenum,sex): 
        self.name=name
        self.phonenum=phonenum
        if sex=="male":
            self.sex = sex
        elif sex == "female":
            self.sex = sex
        else:
            self.sex = "unknown"
    
    def printcal(self): 
        print("이름은 "+self.name+", 전화번호는 "+self.phonenum+",성별은 "+self.sex+"입니다.")

result=[] 
while True:
    name=input("이름을 입력하세요: ")
    if name=="그만":
        break
    phonenum=input("전화번호를 입력하세요: ")
    sex=input("성별을 입력하세요(male이나 female로 작성해주세요): ")
    result.append(cal(name,phonenum,sex)) 
    for i in result: 
        i.printcal()
    print()

for i in result:
    i.printcal()   