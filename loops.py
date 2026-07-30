#1.no is zero or not
# a=int(input("enter a:"))
# if(a==0):
#     print("the no is zero")
# else:
#     print("not zero")

#2.largest of 2 nos
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# if(a>b):
#     print("a is largest")
# else:
#     print("b is largest")

#3.postive or negative
# a=int(input("enter a:"))
# if(a>0):
#     print("postive")
# else:
#     print("negative")

#4.vowel or consonent
# a=str(input("enter a:"))
# if(a=="a",a=="o",a=="e",a=="i",a=="u"):
#     print("vowel")
# else:
#     print("consonent")

#5.student performance
# marks=int(input("enter marks:"))
# if(marks>=90):
#     print("excellent peformance")
# elif(marks>=80):
#     print("very good peformance")
# elif(marks>=70):
#     print(" good peformance")
# elif(marks>=60):
#     print("averge performance")
# else:
#     print("poor performance")

#6.largest of 3 nos
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if(a>b and a>c):
#     print("a is largest")
# elif(b>c and b>c):
#     print("b is largest")
# else:
#     print("c is largest")

#7.smallestt of 3
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if(a<b and a<c):
#     print("a is smallest")
# elif(b<a and b<c):
#     print("b is smallest")
# else:
#     print("c is smallest")

#8.even or odd
# a=int(input("enter a:"))
# if(a%2==0):
#     print("even no")
# else:
#     print("odd no")

# 9.leap year
# year=int(input("enter a:"))
# if(year%4==0):
#     print("leap year")
# else:
#     print("not a leap year")

#10.application for driver
# age = int(input("Enter your age: "))
# gender = input("Enter gender (male/female): ").lower()
# marital_status = input("Enter marital status (married/unmarried): ").lower()

# if marital_status == "married":
#     print("Driver is insured")

# elif marital_status == "unmarried" and gender == "male" and age > 30:
#     print("Driver is insured")

# elif marital_status == "unmarried" and gender == "female" and age > 25:
#     print("Driver is insured")

# else:
#     print("Driver is not insured")


# for loop
# 11.print n natura no
# n=int(input("enter n:"))
# for i in range (1,n+1):
#     print(i)

# 12.even no
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(i)

#  12.even no
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if(i%2!=0):
#         print(i)

# 13.print 1,4,9...
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     print(i*i)

#14. 1+1/1!+1/2!+1/3!...+1/n!
# n = int(input("Enter the value of n: "))

# fact = 1
# sum = 1

# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + (1 / fact)

# print("Sum of the series =", sum)

# 15.1-x^2!/2+x^4/4!+....x^n/n! print
# x = int(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))

# fact = 1
# sum_series = 1
# sign = -1

# for i in range(2, n + 1, 2):
#     fact = fact * (i - 1) * i
#     sum_series = sum_series + sign * (x ** i / fact)
#     sign = -sign

# print("Sum =", sum_series)

# 16.square root of no is prime or not
# n=int(input("enter n:"))

# if n <= 1: 
#     print(n, "is not a prime number")
# else:
#     prime = True

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

# 17.ABC
#    ABC
#    ABC
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     print("ABC")

# 18.A
#    AB
#    ABC
#    ABCD
#    ABCDE
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(65 + j), end="")
#     print()

# 19.ABCDE
#    ABCD
#    ABC
#    AB
#    A
# for i in range(5, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end="")
#     print()

# 20.1
#    12
#    123
#    1234
#    12345
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# 21.1
#    22
#    333
#    4444
#    55555
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# 22.natural no upto n
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     print(i)

# 23.sum of n natural no
# n = int(input("Enter the value of n: "))

# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum =", total)


# while 
# 25.sum of odd natural no
# n = int(input("Enter n: "))

# total = 0

# for i in range(1, 2 * n, 2):
#     total = total + i

# print("Sum =", total)

# 26.sum of even no
# n = int(input("Enter the value of n: "))

# total = 0

# for i in range(2, 2 * n + 1, 2):
#     total = total + i

# print("Sum =", total)

# 27.print no up to n in reverse order
# n=int(input("enter n:"))
# for i in range(n,0,-1):
#     print(i)

# # 28.fibonacii series
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 29.factorial
# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i

# print("Factorial =", fact)

#30.prime no
# n = int(input("Enter a number: "))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

# 31.sum of digits
# n = int(input("Enter a number: "))

# total = 0

# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10

# print("Sum of digits =", total)

# 32.palandrome no
# n = int(input("Enter a number: "))

# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# 33.reverse the given no
# n = int(input("Enter a number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print("Reversed number =", reverse)

# 34.multilication table
# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# 35.largest of n nos
# n = int(input("Enter how many numbers: "))

# largest = int(input("Enter a number: "))

# for i in range(n - 1):
#     num = int(input("Enter a number: "))

#     if num > largest:
#         largest = num

# print("Largest number =", largest)

# 36.smallest of n nos
# n = int(input("Enter how many numbers: "))

# smallest = int(input("Enter a number: "))

# for i in range(n - 1):
#     num = int(input("Enter a number: "))

#     if num < smallest:
#         smallest = num

# print("Smallest number =", smallest)
