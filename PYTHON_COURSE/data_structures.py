# marks = [94.4,87.5,95.2,66.4,45.1]                                    # LISTS
# print(marks)                                                           (mixed data type)
# print(marks[0])
# print(type(marks))
# print(len(marks))

# student = ["karan",95.4,17,"Delhi"]                                      # MUTABLE(THE VALUES CAN BE ACCESSED AND CHANGED ALSO)
# print(student)
# student[0]="Arjun"
# print(student)

# marks=[85,94,76,63,48]                                                # SLICING
# # print(marks[1:4])
# # print(marks[0:4])
# # print(marks[1: ])
# print(marks[-3:-1])

#list=[2,1,3,1]                   # METHODS
#list.append(4)
#list.sort()                    #characters can be done in characters also
#list.sort(reverse=True)
#list.reverse()
#list.insert(1,5)
#list.remove(1)
#list.pop(2)
#print(list)
#print(list.count(1)) 
# num=list.copy()
#print(num)



                                              # TUPLES  (IMMUTABLE)
# tup=(2,1,1,3)
# print(type(tup))
# print(tup[0])
# tup=(1,)                #(correct of way of writing single valued tuple,else it would take the type as int)
# print(tup)
# print(type(tup))

# tup=(1,2,3,4)                         # Slicing
# print(tup[1:3])

# tup=(2,1,3,1)
# print(tup.index(2))
# print(tup.count(1))

                                                 #PRACTICE QUESTIONS
# Movie=[]
# m1=input("Enter 1st movie")
# m2=input("Enter 2nd movie")
# m3=input("Enter 3rd movie")
# Movie.append(m1)
# Movie.append(m2)
# Movie.append(m3)
# print(Movie)

#list=[2,8,8,2,1]
# l1=list.copy()
# l1.reverse()
# if(list==l1):
#     print("I am Palindrome")
# else:
#     print("Not a Palindrome")

#tup=("C","D","A","A","B","B","A")
# print(tup.count("A"))

# list=["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

                                                   # DICTIONARY

# info={
#     "name":"apna college",
#     "subjects":["python","C","Java"],         # can also store list and tuple in dictionary.
#     "Topics":("dictionary","set"),
#     "learning":"coding",
#     "age":21,
#     "is_adult":True,
#     "marks":94.4
#    }
# print(info)
# print(type(info))   
# print(info["name"])     #if key dont exist then there will be a "key error"
# print(info["subjects"])
# print(info["Topics"]) 
# print(info["age"])               

# info["name"]="Anamta"     #can change the values of the key
# info["surname"]="Koty"     #can add a new key
# print(info)

# null_dict={}                # Null DICTIONARIES
# null_dict["name"]="Anamta"
# print(null_dict)

# Student={                           #NESTED DICTIONARIES
#     "name":"Anamta Koty",
#     "Subjects":{
#         "Physics":97,
#         "Chemistry":98,
#         "Maths":99
#     }
# }
# print(Student)
# print(Student["Subjects"])
# print(Student["Subjects"]["Chemistry"])

# print(Student.keys())                   # DICTIONARY METHODS
# print(list(Student.keys()))  #type casting
# print(len(Student))
          ##print(len(list(Student.keys())))
#print(Student.values())
# pairs=list(Student.items())
# print(pairs[0])
#print(Student["name2"])       # error
#print(Student.get("name2"))   #none
#Student.update({"city":"Delhi"})
# city={"City":"Delhi","age":21,"name":"Neha"}
# Student.update(city)
# print(Student)

                                    # SETS
# collection = {1,2,3,4,"hello","world"}
# print(collection)            ### ignores duplicate values
# print(type(collection))
# print(len(collection))

#set={}  #empty dictionary
# empty =set()      #empty set
# print(type(empty))

# collection = set()             # SETS METHODS
# collection.add(1)
# collection.add(2)
# collection.add((1,2,3,4))
# collection.add("apna college")
# collection.remove(1)
# #collection.clear()
# print(collection)
# print(len(collection))

# print(collection.pop())

# set1={1,2,3}
# set2={3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1)

                                                   # PRACTICE QUESTIONS
# Python = {
#     "Table": ["a piece of furniture","list of facts & figures"],
#     "cat": "a small animal"
# }
# print(Python)

# subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(subjects)
# print(len(subjects))

# marks = {}
# marks["Physics"]=int(input("Enter marks of physics : "))
# marks["Chem"]=int(input("Enter marks of Chem : "))
# marks["Bio"]=int(input("Enter marks of Bio : "))
# print(marks)

# num={9,"9.0"}
# print(num)

# num={("float",9.0),("int",9)}
# print(num)


