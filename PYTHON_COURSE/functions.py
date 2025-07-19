#function definition                                              # FUNCTIONS
# def calc_sum(a,b): #parameters
#     return a+b
# sum=calc_sum(1,2) #function call; (arguments)
# print(sum)

# def print_hello():
#     print("hello")
# print_hello()
# output=print_hello()
# print(output)

#average of 3 nos
# def calc_avg(a,b,c):
#     average=(a+b+c)/3
#     print (average)
#     return average
# calc_avg(98,97,95)
  
                                                    # BUILT IN FUNCTIONS (Already written in python)
#print("GlobalCollege","Anamta Koty")   #sep=" "
# print("GlobalCollege",end=" ")                  #end=\n
# print("AnamtaKoty")
# len()
# range()
# type()

                                                    # Default Parameters
# def calc_prod(a=7,b=2):
#     print(a*b)
#     return a*b
# calc_prod()

# def calc_prod(a,b=2):  #always give default parameter from the last
#     print(a*b)
#     return a*b
# calc_prod(8)

                                    # PRACTICE QUESTIONS
# nums=[1,3,6,4,6,4,3]
# veggies=["tomato","potato","beans","brinjal"]
# def calc_length(nums):
#     print(len(nums))
# calc_length(nums)
# calc_length(veggies)

# list=["cat","dog","tiger","lion","dear"]
# def sameline(list):
#     i=0
#     while i<len(list):             #for i in list
#         print(list[i],end =" ")
#         i+=1
# sameline(list)

# def calc_fact(n):
#     factorial=1
#     i=1
#     while(i<=n):    #for i in range(1,n+1):
#         factorial=factorial*i
#         i+=1
#     print(factorial)  
#     return factorial
# calc_fact(6)
    
# def convertto_INR(USD):
#     print(USD,"USD=",USD*83,"INR")
# convertto_INR(190)    

# def hwfunct():
#     n=int(input("Enter n: "))
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# hwfunct()

                                                  # RECURSION
# Recursive Function(call stack)
# def show(n):    
#    if(n==0):   #base case
#       return   #control return
#    print(n)
#    show(n-1)
#    print("end")
# show(5)  

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1) * n
# print(fact(5))

# def sum(n):
#     if(n==0):
#         return 0
#     else:
#         return sum(n-1)+n
# print(sum(10))

# list=[1,2,3,4,5,6]
# def get_list(list,n=0):
#     if(n==len(list)):
#         return
#     else:
#         print(list[n])
#         get_list(list,n+1)
# get_list(list)
