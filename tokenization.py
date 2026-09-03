# Tokenization is the process of breaking a Python program into small individual units called tokens.
# Python provides a built-in module called tokenize for this

# 1.simple tokenization
# import tokenize
# from io import BytesIO

# code = b"x = 10 + 20"

# tokens = tokenize.tokenize(BytesIO(code).readline)

# for token in tokens:
#     print(tokenize.tok_name[token.type], ":", token.string)

#2.tokenization with user input
# import tokenize
# from io import BytesIO

# code = input("Enter Python code: ")

# tokens = tokenize.tokenize(BytesIO(code.encode()).readline)

# for token in tokens:
#     print(tokenize.tok_name[token.type], ":", token.string)

# # 3.toookenization of python file
# a = 10
# b = 20
# print(a + b)
# import tokenize

# with open("tokenization.py", "rb") as file:
#     tokens = tokenize.tokenize(file.readline)

#     for token in tokens:
#         print(tokenize.tok_name[token.type], ":", token.string)

# 4.Tokenize an if Statement
# import tokenize
# from io import BytesIO

# code = b"if a > 10: print(a)"

# tokens = tokenize.tokenize(BytesIO(code).readline)

# for token in tokens:
#     print(tokenize.tok_name[token.type], ":", token.string)

# 5.Tokenize a String and Variable
# import tokenize
# from io import BytesIO

# code = b'name = "Rahul"'

# tokens = tokenize.tokenize(BytesIO(code).readline)

# for token in tokens:
#     print(tokenize.tok_name[token.type], ":", token.string)

# 1. Simple Statement
# Tokenizes x = 10 + 20 and identifies names, numbers, and operators.

# 2. User Input
# Takes Python code from the user and identifies each token.

# 3. Python File
# Reads a .py file and displays all the tokens in the file.

# 4. If Statement
# Tokenizes an if condition and identifies keywords, names, numbers, and operators.

# 5. String and Variable
# Tokenizes a variable containing a string and identifies the variable, operator, and string.