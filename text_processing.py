# 1)Remove Puncuation
# Removing punctuation is the process of removing punctuation marks such as . , ! ? ; : from text.
# //1.
# import string

# text = input("Enter text: ")

# result = text.translate(str.maketrans("", "", string.punctuation))

# print("Original:", text)
# print("Result:", result)
# 2.
# text = input("Enter text: ")

# result = text.replace("!", "").replace("?", "")

# print("Result:", result)
# 3.
# text = input("Enter text: ")

# result = text.replace(",", "").replace(".", "")

# print("Result:", result)
# 4.
# import string

# text = input("Enter text: ")
# result = ""

# for ch in text:
#     if ch not in string.punctuation:
#         result += ch

# print("Result:", result)
# 5.
# import string

# text = input("Enter sentence: ")

# words = text.split()
# result = []

# for word in words:
#     word = word.strip(string.punctuation)
#     result.append(word)

# print("Result:", " ".join(result))

# 2)remove number
# Removing numbers is the process of removing numerical characters such as 0–9 from text.
# 1.
# text = input("Enter text: ")

# result = ""

# for ch in text:
#     if not ch.isdigit():
#         result += ch

# print("Result:", result)
# 2.
# import re

# text = input("Enter text: ")

# result = re.sub(r'[0-9]', '', text)

# print("Result:", result)
3.
# text = input("Enter sentence: ")

# words = text.split()
# result = []
# for word in words:
#     if not word.isdigit():
#         result.append(word)

# print("Result:", " ".join(result))


