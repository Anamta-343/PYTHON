    # LOOP  (WHILE)
# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)

# i=1
# while i<= 100:     # stopping condition
#     print("apna college",i)
#     i+=1

# num = 1          #print numbers from 1 to 5
# while num<=5:
#     print(num)
#     num+=1

# i=5               #print numbers from 5 to 1
# while i >= 1 :
#     print(i)
#     i-=1

                                       # PRACTICE QUESTIONS
# i=1
# while i<= 100:
#     print(i)
#     i+=1
# print("LOOP ENDED")    

# i=100
# while i>=1:
#     print(i)
#     i-=1

# n = int(input("Enter the number n :"))
# i=1
# while(i<=10):
#     table = n*i
#     print(table)
#     i+=1

# i=1
# while i<=10:
#     square=[i*i]
#     print(square)
#     i+=1
 
# list=[1,4,9,16,25,36,49,64,81,100]       #traverse
# index=0
# while index<=len(list)-1:
#     print(list[index])
#     index+=1

# tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter the number to be searched :"))
# i=0
# while i<len(tup):
#     if(tup[i]==x):
#         print("Found at index",i)
#         break
#     else:
#         print("Not Found")
#     i+=1
# print("END OF LOOP")

                                            # BREAK & CONTINUE
# i = 1         
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("END OF LOOP")

# i = 0        
# while i<=5:
#     if(i==3): 
#         i+=1
#         continue     #skips
#     print(i)
#     i+=1

# i=1
# while i<=10 :
#     if(i%2!=0):  #if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1  

                                                         # FOR LOOP
# veggies=["potato","lady finger","tomato","cucumber"]
# for val in veggies :
#     print(val)
   
# tup=(1,2,3,4,5)
# for num in tup:
#     print(num)

# str="apnacollege"
# for el in str:
#     if(el=="o"):
#         print("o found")
#         break
#     print(el)
# else:
#     print("END")

                                                  # LETS PRACTICE
# list=[1,4,9,25,36,49,64,81,100]
# for val in list:
#     print(val)
   
# tup=(1,4,9,25,36,49,64,81,100,49)                           # Linear search
# x=int(input("ENTER THE NUMBER TO BE SEARCHED :"))
# index =0
# for val in tup:
#     if(val==x):
#         print("Number found at",index)
#         break
#     index+=1

# seq = range(10)                                        # Range
# for i in seq:
#     print(i)

# for i in range(10): #stopping condition
    # print(i)
# for i in range(2,10): #range(start,stop)
#     print(i)
# for i in range(2,10,2): #range(start,stop,step)
#     print(i)
 
# for i in range(2,101,2):       #even numbers
#     print(i)
# for i in range(1,101,2):       #odd numbers
#     print(i)

                                 # PRACTICE QUESTIONS
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)

# n=int(input("ENTER THE NUMBER n:"))
# for i in range(1,11):
#     print(n*i)

# for i in range(5):                              #pass statement
#     pass
# print("Some useful work")      
# if i>5:
#     pass                                     

                             #PRACTICE QUESTIONS
# n=int(input("ENTER n :"))            ("SUM OF NUMBERS")
# sum=0
# i=1
# while i<=n:
#     sum +=i
#     i+=1
# print("Total sum",sum)

# n=int(input("ENTER n :")) 
# fact=1
# for i in range(1,n+1):
#     fact *=i
#     i+=1
# print("FACTORIAL:",fact)