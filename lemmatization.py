# Lemmatization is the process of converting a word into its meaningful base or dictionary form (lemma) using vocabulary and grammatical rules.

# 1.lemmatize a single word
# from nltk.stem import WordNetLemmatizer

# l = WordNetLemmatizer()

# word = input("Enter a word: ")

# print("Original:", word)
# print("Lemma:", l.lemmatize(word))

# 2.lemmatize multiple words
# from nltk.stem import WordNetLemmatizer

# l = WordNetLemmatizer()

# words = ["dogs", "cats", "cars", "houses"]

# for word in words:
#     print(word, "→", l.lemmatize(word))

# 3.lemmatize a sentence
# from nltk.stem import WordNetLemmatizer

# l = WordNetLemmatizer()

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# for word in words:
#     print(word, "→", l.lemmatize(word))

# 4.lemmatize
# from nltk.stem import WordNetLemmatizer

# l = WordNetLemmatizer()

# words = ["playing", "played", "running", "eating"]

# for word in words:
#     print(word, "→", l.lemmatize(word, pos="v"))

# 5.lemmatize irregular words
# from nltk.stem import WordNetLemmatizer

# l = WordNetLemmatizer()

# words = ["children", "mice", "feet", "teeth"]

# for word in words:
#     print(word, "→", l.lemmatize(word, pos="n"))