class professor:
    professorId=""
    professorName=""
    address=""
    phoneNumper=""
    age=0
    salary=0
    def __init__(self, professorId,professorName,address,phoneNumper, age):
        self.professorId = professorId
        self.professorName = professorName
        self.address = address
        self.age = age
        self.phoneNumper = phoneNumper
    def printInformation(self):
        print("Professor id : "+self.professorId+"\nProfessor name : "+self.professorName+"\nProfessor address : "+self.address+"\nProfessor age : "+self.age+"\nProfessor phoneNumper : "+self.phoneNumper)
