# single quotes
# print('hello')

# Double quotes
# print('he said, "hello"')
# print("Beunas Dias")

# double triple quotes
# print("""for mltiple lines""")

# single triple quotes
# print('mucho gusto')


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
