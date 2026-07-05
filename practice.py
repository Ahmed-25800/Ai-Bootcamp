# a=int(input("enter the first side of triangle:"))
# b=int(input("enter the second side of triangle:"))
# c=int(input("enter the third side of triangle:"))
# if (a==b==c):
#     print("The traingle is equilateral ")
# elif(a==b and  b!=c):
#     print("triangle is isosceles ")
# else:
#     print("The triangle is scalene ")
#     if (a**2 + b**2 == c**2):
#         print("The triangle is right angled ")

# age=int(input("enter the age of the person:"))
# day=str(input("enter :"))
# if age <12:
#     if day=="weekday" :
#         print("check the discounts applied ")
#     else:
#         print("no discount invalid day")
# elif age>=60:
#     if day=="weekday" :
#         print("Check the membership status for the discounts ")
#     else:
#         print("no discount invalid day")
# else:
#     print("full price applied")        


# username=str(input("enter the name :"))
# password=int(input("Enter the password:"))
# a="Huzaifa Ahmed"
# pas=1234
# flag=True
# if username==a:
#     if  password==pas: 
#         if flag==True:
#             print("login succesfull")
#         else:
#             print("login failed")
            
#     else:
#         print("password is incorrect")
# else:
#     print("username is incorrect")

#NESTED LOOPS 

# rows=5
# num=1
# for i in range(1,rows+1):
#     print(" " * (rows-i),end="")
    
#     for j in range(1,i+1):
#         print(num," ",end="")
#         num+=1
#     print()
    
# rows = 5
# num = 1  # This keeps track of our continuous count

# for i in range(1, rows + 1):
#     # 1. Print leading spaces for alignment
#     print(" " * (rows - i), end="")
    
#     # 2. Print the numbers for this row
#     for j in range(1, i + 1):
#         print(num, end=" ")  # Notice the space inside end=" " to keep numbers separated
#         num += 1             # Move to the next number
        
#     # 3. Move to the next line after the row finishes
#     print()
    
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")  # Use tab for better alignment
#     print()  # Move to the next line after each row 
# for i in range(1, 11):
#     if i % 2 == 0:
#         for j in range(1, i + 1):
#             if j % 2 == 0:
#                 print(j, end=" ")
#         print()   
          

 #NESTED LOOPS WITH NESTED CONDITIONAL STATEMENTS
 
# for i in range(1,51):
#      if i%3==0 and i%5==0 :
#          print("FizzBuzz")
#      elif i%3==0:
         
#          print("divisble by 3")
#      elif i%5==0:
#          print("divisible by 5")
#      else:
#          print(i)        
prime_num=0
perf_num=0
neither_num=0

# for i in range(1,100):
    
#     is_prime=True
#     if i<2:
#         is_prime=False
#     else:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
                  
#              is_prime=False
#              break
#     if is_prime==True:
#             print(i,"is prime number")
#             prime_num+=1
#     elif (i**0.5)%1==0:
#             print(i,"is perfect square")
#             perf_num+=1
#     else:
#             print(i,"is neither prime nor perfect square")
#             neither_num+=1
# print("Total prime numbers:", prime_num)
# print("Total perfect squares:", perf_num)   
# nums = [50,51,52,53,54,55]

# for i,n in enumerate(nums):
#     if n>50:
#         print(n,i)        

# one={32,45,67}
# two={23,32,67}
# x=set(one).difference(two)
# print(x)





             
            
        
        
            
    
    
                  
      
                    

        
    
    
        