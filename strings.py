# single quotes
# print('hello')

# Double quotes
# print('he said, "hello"')
# print("Beunas Dias")

# double triple quotes
# print("""for mltiple lines""")

# single triple quotes
# print('''mucho gusto''')


# 1.Write a program to input a string and
#  display its length without using the len() function. 
# string=input("enter string:")
# count = 0
# for character in string:
#     count = count + 1
# print("Length of string =", count)

# 2.Count the number of vowels, consonants,
# digits, spaces, and special characters in a given string. 
# string = input("Enter a string: ")
# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special = 0
# for char in string:
#     if char in "AEIOUaeiou":
#         vowels = vowels + 1
#     elif ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
#         consonants = consonants + 1
#     elif '0' <= char <= '9':
#         digits = digits + 1
#     elif char == " ":
#         spaces = spaces + 1
#     else:
#         special = special + 1
# print("Vowels =", vowels)
# print("Consonants =", consonants)
# print("Digits =", digits)
# print("Spaces =", spaces)
# print("Special characters =", special)

# 3.Reverse a String 
# text = input("Enter a string: ")
# reverse = ""
# for character in text:
#     reverse = character + reverse
# print("Reversed string =", reverse)

# 4.Palindrome Check 
# string=input("enter string:")
# original=string
# duplicate=""
# for char in string:
#     duplicate=char+duplicate
# if(original==duplicate):
#      print("palandrome string")
# else:
#     print("not a palandrome")

#5.Uppercase and Lowercase Count 
# string = input("Enter a string: ")
# upper_count = 0
# lower_count = 0
# for char in string:
#     if 'A' <= char <= 'Z':
#         upper_count = upper_count + 1
#     elif 'a' <= char <= 'z':
#         lower_count = lower_count + 1

# print("Uppercase letters =", upper_count)
# print("Lowercase letters =", lower_count)

#6.Replace Characters 
# string = input("Enter a string: ")
# old_char = input("Enter character to replace: ")
# new_char = input("Enter new character: ")
# result = ""
# for char in string:
#     if char == old_char:
#         result = result + new_char
#     else:
#         result = result + char
# print("Updated string =", result)

# 7.Remove Spaces 
# string = input("Enter a string: ")
# result = ""
# for char in string:
#     if char != " ":
#         result = result + char
# print("String without spaces =", result)

# 8.Frequency of a Character 
# string = input("Enter a string: ")
# search_char = input("Enter the character: ")
# count = 0
# for char in string:
#     if char == search_char:
#         count = count + 1
# print("Frequency of", search_char, "=", count)

# 9.First and Last Character 
# string = input("Enter a string: ")
# if string == "":
#     print("String is empty")
# else:
#     print("First character =", string[0])
# #     print("Last character =", string[-1])
# negative indexing starts from last letter and positive indexing start from beginning

# 10.ASCII Values 
# string = input("Enter a string: ")
# for char in string:
#     print(char, "=", ord(char))

# 11.Count the total number of words in a sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# count = 0
# for word in words:
#     count = count + 1
# print("Total number of words =", count)

# 12.a.	Find the longest word in a given sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word =", longest)

# 13.Find the smallest word in a given sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# smallest = words[0]
# for word in words:
#     if len(word) < len(smallest):
#         smallest = word
# print("Smallest word =", smallest)

# 14.turn the first letter of every word in uppercase
# sentence = input("Enter a sentence: ")

# result = sentence.title()

# print("Updated sentence =", result)
# 15.print all the duplicate char from string
# string = input("Enter a string: ")

# printed = ""

# for char in string:
#     if string.count(char) > 1 and char not in printed:
#         print(char)
#         printed = printed + char

# 16.Display the frequency of every character in a string
# string = input("Enter a string: ")
# checked = ""
# for char in string:
#     if char not in checked:
#         print(char, "=", string.count(char))
#         checked = checked + char

# # 17.Check whether two strings are anagrams
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# string1 = string1.replace(" ", "").lower()
# string2 = string2.replace(" ", "").lower()
# if sorted(string1) == sorted(string2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")

# 18.Remove duplicate characters while maintaining the original order. 
# string = input("Enter a string: ")
# result = ""
# for char in string:
#     if char not in result:
#         result = result + char

# print("String after removing duplicates =", result)string = input("Enter a string: ")
# result = ""
# for char in string:
#     if char not in result:
#         result = result + char

# print("String after removing duplicates =", result)

# 19.a.	Check whether a given substring exists in the main string. 
# main_string = input("Enter the main string: ")
# substring = input("Enter the substring: ")
# if substring in main_string:
#     print("Substring exists")
# else:
#     print("Substring does not exist")

# # 20.a.	Count how many times a specific word appears in a sentence.
# sentence = input("Enter a sentence: ")
# word = input("Enter the word to search: ")
# words = sentence.split()
# count = words.count(word)
# print("Frequency of", word, "=", count)

# # 21.●	Validate a password based on these conditions: 
# Minimum 8 characters 
# At least one uppercase letter 
# One lowercase letter 
# One digit 
# One special character
# password=input("enter password:")
# upper=False
# lower=False
# digit=False
# special=False
# for char in password:
#     if char.isupper():
#         upper=True
#     elif char.islower():
#         lower=True
#     elif char.isdigit():
#         digit=True
#     else:
#         special=True
# if len(password)>=8 and upper and lower and digit and special:
#     print("valid passsword")
# else:
#     print("invalid password")

# 22.●	Compress a string by counting consecutive repeated characters. 
# ●	Example:
# 	Input: aaabbccccd
	# Output: a3b2c4d1
# string=input("enter string:")
# result=" "
# count=1
# for i in range(1,len(string)):
#     if string[i]==string[i-1]:
#         count=count+1
#     else:
#         result=result+string[i-1]+str(count)
#         count=1
# result=result+string[-1]+str(count)
# print("compressed string=",result)

# 23.●	Compress repeated characters and return the original string if compression does not reduce the length.
# string=input("enter string:")
# result=""
# count=1
# for i in range(1,len(string)):
#  if string[i]==string[i-1]:
#     count=count+1
# else:
#     result=result+string[i-1]+str(count)
#     count=1
# result=result+string[-1]+str(count)
# if len(result)<len(string):
#     print("result=",result)
# else:
#     print("result+",string)

# 24.●	Find the character with the highest frequency. 
# string=input("enter string")
# highest_char=""
# highest_count=0
# for char in string:
#     count=string.count(char)
#     if count>highest_count:
#         highest_count=count
#         highest_char=char
# print("highest frequency character=",highest_char)
# print("frequency=",highest_count)

# 25.●	Find the second most frequently occurring character. 
# string = input("Enter a string: ")

# first_count = 0
# second_count = 0
# second_char = ""

# for char in string:
#     count = string.count(char)

#     if count > first_count:
#         second_count = first_count
#         second_char = ""
#         first_count = count

#     elif first_count > count > second_count:
#         second_count = count
#         second_char = char

# if second_count == 0:
#     print("Second most frequent character does not exist")
# else:
#     for char in string:
#         if string.count(char) == second_count:
#             second_char = char
#             break

#     print("Second most frequent character =", second_char)
#     print("Frequency =", second_count)

# 26.●	Encrypt and decrypt a message using the Caesar Cipher algorithm.
# message = input("Enter the message: ")
# shift = int(input("Enter shift value: "))
# choice = input("Enter E for encryption or D for decryption: ").upper()

# if choice == "D":
#     shift = -shift

# result = ""

# for char in message:
#     if 'A' <= char <= 'Z':
#         result += chr((ord(char) - 65 + shift) % 26 + 65)

#     elif 'a' <= char <= 'z':
#         result += chr((ord(char) - 97 + shift) % 26 + 97)

#     else:
#         result += char

# print("Result =", result) 

# 27.●	Validate whether a given email address follows a valid format. 
# import re

# email = input("Enter email address: ")

# pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# if re.fullmatch(pattern, email):
#     print("Valid email address")
# else:
#     print("Invalid email address")

# 28.●	Count the frequency of every word in a paragraph
# paragraph = input("Enter a paragraph: ").lower()

# words = paragraph.split()
# frequency = {}

# for word in words:
#     word = word.strip(".,!?;:\"'()")

#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# for word in frequency:
#     print(word, "=", frequency[word])


# 29.●	Reverse the order of words in a sentence without changing the words themselves. 
# ●	Example:
# ●	Input: Python is easy
# Output: easy is Python
# sentence = input("Enter a sentence: ")

# words = sentence.split()
# words.reverse()

# print("Reversed sentence =", " ".join(words))

# 30.●	Check whether one string is a rotation of another. 
# ●	Example:
# ●	ABCD
# ●	CDAB
# Output: Yes
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")

# combined = string1 + string1

# if len(string1) == len(string2) and string2 in combined:
#     print("Yes, the strings are rotations")
# else:
#     print("No, the strings are not rotations")


