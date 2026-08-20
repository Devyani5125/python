# A module is a Python file (.py) that contains functions, variables, classes, or statements.
# Modules help us organize code and reuse it in different programs.
# Python provides many built-in modules such as math, random, datetime, and os.
# there are 3 thyes of modules:
# 1.bulit-i:These modules are already provided with Python. No separate installation is required
# 2.user defined:A user-defined module is a Python file created by the programmer. It can contain functions and variables that can be reused in another Python program
# 3.third party:

# 1)built-in:
# 1.
# import math
# print(math.sqrt(25))
# 2.
# import random
# print(random.randint(1, 10))
# 3.
# import datetime
# today = datetime.date.today()
# print(today)
# 4.
# import calendar
# print(calendar.month(2026, 8))


# 2)User defined
# def add(a, b):
#     return a + b

# def square(n):
#     return n * n

# def check_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# def multiply(a, b):
#     return a * b


# 3)third party modules
# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print("Array:", numbers)
# print("Sum:", np.sum(numbers))
# print("Maximum:", np.max(numbers))

# import pandas as pd

# data = {
#     "Name": ["Amit", "Rahul", "Sneha"],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)

# print(df)


