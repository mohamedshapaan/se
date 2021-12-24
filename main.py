import professor
import student
class courses(professor.professor,student.student):
    coursesId=""
    coursesName=""
    maxNumperOfStudent=0
    minNumperOfStudent=0
    professors=[]
    studentIds=[]
    grades=[]
    def __init__(self, coursesId,coursesName,maxNumperOfStudent,minNumperOfStudent, professors,studentIds,grades):
        self.coursesId = coursesId
        self.coursesName = coursesName
        self.maxNumperOfStudent = maxNumperOfStudent
        self.minNumperOfStudent = minNumperOfStudent
        self.professors.append(professors)
        self.studentIds.append(studentIds)
        self.grades.append(grades)
    def cheakActivationOfCourse(self):
        if self.minNumperOfStudent>len(self.studentIds):
           print("course is cancilled")
        else:
            print("it is have "+str(len(self.studentIds))+" students")
    def printInformation(self):
        cheakActivationOfCourse()
        print("coursesid : "+self.coursesId+"\ncourses name : "+self.coursesName+"\n\nmaximum numper of student : "+str(self.maxNumperOfStudent)+"\n minimum numper of student : "+str(self.minNumperOfStudent)+"\nnumper of Professor : "+str(len(self.professors))+"\nnumper of student : "+str(len(self.studentIds)))
students=[] #array of student
professors=[] #array of professors
course=[] #array of courses
item=[] #i use it like temp to put a information
item2=[]
grade=[]
counter=0
while 1==1:
    print("welcome\n1-input a new students\n2-enter new professors\n3-enter new courses\n4-print all professors\n5-print all students \n6-print information of all courses\n7-print spicial course\n8-resite")
    choose = input("your choose:")

    if choose==1:
        chooses = input("Enter the number of student:")
        for i in range (chooses):
            studentId=input("Enter the studentId:")
            studentName=input("Enter the studentName:")
            studentType=input("Enter the studentType:")
            address=input("Enter the address:")
            phoneNumper=input("Enter the phoneNumper:")
            age=input("Enter the age:")
            studentobject=student.student(studentId,studentName,studentType,address,phoneNumper,age)
            students.append(studentobject)
    if choose==2:
        chooses = input("Enter the number of professors:")
        for i in range (chooses):
            professorId=input("Enter the professorId:")
            professorName=input("Enter the professorName:")
            address=input("Enter the address:")
            phoneNumper=input("Enter the phoneNumper:")
            age=input("Enter the age:")
            professorobject=professor.professor(studentId,studentName,address,phoneNumper,age)
            professors.append(professorobject)
    if choose==3:
        chooses = input("Enter the number of courses:")
        for i in range (chooses):
            coursesId=input("Enter the coursesId:")
            coursesName=input("Enter the coursesName:")
            maxNumperOfStudent=input("Enter the maxNumperOfStudent:")
            minNumperOfStudent=input("Enter the minNumperOfStudent:")
            chooseing = input("Enter the number of professors:")
            for j in range (chooseing):
                professorName=input("Enter the professorName:")
                for v in professors:
                    if v.professorName==professorName:
                        item.append(v)
                    else:
                        print("the name of professor is ronge")
                        j=0
            chooseing = input("Enter the number of students:")
            for j in range (chooseing):
                studentName=input("Enter the studentName:")
                ranges=input("Enter the student grade:")
                for v in students:
                    if v.studentName==studentName:
                        item2.append(v)
                        grade.append(ranges)
                    else:
                        print("the name of student is ronge")
                        j=0      
            course.append(courses(coursesId,coursesName,maxNumperOfStudent,minNumperOfStudent,professors,students,grade))
    if choose==4:
        for v in students:
            v.printInformation()
            for i in course:
                for j in i.studentIds:
                    if j.studentIds==v.studentName:
                        counter=counter+1
                        
            if counter<3:
                print("\npart time")
            else:
                print("\nfull time")
    if choose==5:
        for v in professors:
            v.printInformation()
            for i in course:
                for j in i.professors:
                    if j.professors==v.professorName:
                        counter=counter+1
            if counter>4:
                print("\nsalary: "+str(counter*200+20000)+"$")
            else:
                print("\nsalary: "+str(counter*200)+"$")

    if choose==6:
        for v in course:
            v.printInformation()
    if choose==7:
        coursesName=input("Enter the coursesName:")
        for v in course:
             if v.coursesName==coursesName:
                 v.printInformation()
                 print("the professors they in course\n")
                 for i in v.professors:
                     v.professors.printInformation()
                 print("the students in course\n")
                 for i in v.studentIds:
                     v.studentIds.printInformation()
                     v.grades[i]
    if choose==8:
        students=[] #array of student
        professors=[] #array of professors
        course=[] #array of courses
        item=[] #i use it like temp to put a information
        item2=[]
        grade=[]
        counter=0    



    
