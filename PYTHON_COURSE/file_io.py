                                 #FILE I/O
            # READING
# f=open("demo.txt","r")
# data=f.read()          #reads entire file
# print(data)
# data=f.read(5)         #reads first 5 char
# print(data)
# data=f.readline()       #reads one line at a time          
# print(data)  
# data=f.readline()             
# print(data)    
# f.close()
            # WRITING
# f=open("demo.txt","w")                             #over write on the file
# f.write("I want to learn javasript tomorrow.123")
# f.close()
# f=open("demo.txt","a")                              #add the data at the end of the file
# f.write("\nThen i will move to React JS.")
# f.close()

# f=open("sample.txt","w")             #will create a new file
# f.close()
# f=open("sample.txt","a")               #will create a new file
# f.close()

# f=open("demo.txt","r+")       #over writes from starting
# f.write("abc")
# print(f.read())            #after writing abc the pointer goes to s.
# f.close()

# f=open("demo.txt","w+")        # the file gets truncated.
# print(f.read())  
# f.write("abc")          
# f.close()

# f=open("demo.txt","a+")        #pointer is at the last 
# print(f.read())  
# f.write("abc")          
# f.close()

# with open("demo.txt","r") as f:       #as means alias .......with automatically closes the file
#     data=f.read()                     
#     print(data)

# with open("demo.txt","w") as f:   
#     f.write("New Data")   
     
                         # DELETING
# import os
# os.remove("demo.txt")
                       

                                    #PRACTICE QUESTIONS
# with open("practice.txt","w") as f:
#     f.write("Hi everyone \nwe are learning File I/O \nusing Java.\nI like programming in Java.")
    
# with open("practice.txt","r") as f:
#     data=f.read()
# newdata=data.replace("Java","Python")
# print(newdata)
# with open("practice.txt","w") as f:
#        f.write(newdata)
    
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#          data=f.read()
#          if(data.find(word)!=-1):      # word in data
#           print("Found")
#          else:
#           print("Not found")
# check_for_word()
   
# def check_for_line():
#     word="learning"
#     line_no=1
#     data=True
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                print(line_no)
#                return
#             line_no+=1
#     return -1
# check_for_line()
  
# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

#     nums=data.split(",")
#     print(nums)
#     for i in nums:
#         if(int(i)%2==0):
#             count+=1
#     print(count)



    