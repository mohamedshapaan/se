class student:
    studentId=""
    studentName=""
    address=""
    studentType=""
    phoneNumper=""
    age=0
    def __init__(self, studentId,studentName,address,studentType,phoneNumper, age):
        self.studentId = studentId
        self.studentName = studentName
        self.address = address
        self.age = age
        self.studentType = studentType
        self.phoneNumper = phoneNumper
    def printInformation(self):
        print("student id : "+self.studentId+"\nstudent name : "+self.studentName+"\nstudent address : "+self.address+"\nstudent age : "+self.age+"\nstudent phoneNumper : "+self.phoneNumper+"\nstudent type : "+self.studentType)
