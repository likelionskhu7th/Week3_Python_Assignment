class people:
     def __init__(self,name,phoneNum,sex):

         self.name=name
         self.phoneNum=phoneNum
         if sex =="female":
            self.sex=sex
         elif sex=="male":
            self.sex=sex
         else:
             self.sex="unknown"
                
     def printabout(self):
         print("이름은" + self.name +","+ "전화번호는"+ self.phoneNum + ","+ "성별은" + self.sex + "입니다.")
 
result=[]
         
while True:
    name=input("이름을 입력하세요: ")
    if name =="그만":
         break
                   
    phoneNum=input("전화번호를 입력하세요:  ")
    sex=input("성별을 입력하세요(female이나 male로 작성해주세요): ")

    result.append(people(name,phoneNum,sex))

    for i in result:
        i.printabout()
for i in result:
    i.printabout()