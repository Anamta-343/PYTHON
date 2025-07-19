  # OOPS
        #CLASSES AND OBJECTS
# class Student:
#     name="Karan"
# s1=Student()
# print(s1.name)
# s2=Student()
# print(s2.name)

#class Car:
#     color="blue"  
#     brand="mercedes"
# c1=Car()
# print(c1.color)
# print(c1.brand)

         #CONSTRUCTOR(INIT FUNCTION)
# class Student:
#      college = "abc college"   #class attr

#      def __init__(self):      #Default constructors
#         pass

#      def __init__(self,name,marks):      ##Parameterized onstructors #pointing to the object(self)
#         self.name=name         #obj attr
#         self.marks=marks
#         print("Adding new student in database..") 

#      def welcome(self):                               # METHODS
#             print("Welcome Student,",self.name)
#      def getmarks(self):
#           return self.marks 
     

# s1=Student("Karan",98)
# print(s1.name,s1.marks)
# s1.welcome()
# print(s1.getmarks())
# s2=Student("Arjun",76)
# print(s2.name,s2.marks)
# print(s2.college)   #print(Student.college)

                                     # PRACTICE QUESTIONS
# class Student:
    
#     def __init__(self,name,marks):      #constructor
#         self.name=name
#         self.marks=marks
                               
#                                #STATIC METHOD
#     @staticmethod        # decorator               
#     def hello():
#         print("hello")
       
     

#     def average(self):                   #method
#         sum=0
#         for value in self.marks:
#             sum=sum+value
#         avg=sum/3
#         print("Hi!!",self.name,".","Your marks are",self.marks,"The average score is:",avg)

# s1=Student("Tony Stark",[99,98,97])       #object
# s1.average()
# s1.name="Ironman"
# s1.average()
# s1.hello()

                        # PILLARS OF OOPS
        # ABSTRACTION
# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car Started..")

# car1=car()
# car1.start()

       # ENCAPSULATION

#All the codes written above use encapsulation.We wrap up the data and methods into a class and then use it in the object.

                            # PRACTICE QUESTION
# class Account:
#      def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#    # debit method
#      def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"was debited")
#         print("Total balance is",self.get_balance())

#     #credit method
#      def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"was credited to your account")
#         print("Total balance is",self.get_balance())
         
#      def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)








