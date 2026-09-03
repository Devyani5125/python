# Stemming is a Natural Language Processing (NLP) technique that reduces a word to its root/base form by removing prefixes or suffixes.
# 1.stemming a single word
# from nltk.stem import PorterStemmer

# ps = PorterStemmer()

# word = input("Enter a word: ")

# print("Original:", word)
# print("Stem:", ps.stem(word))

# 2.steamming multipl words
# from nltk.stem import PorterStemmer

# ps = PorterStemmer()

# words = ["playing", "played", "plays", "player"]

# for word in words:
#     print(word, "→", ps.stem(word))

# 3.steamming a sentence
# from nltk.stem import PorterStemmer

# ps = PorterStemmer()

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# for word in words:
#     print(word, "→", ps.stem(word))

# 4.stemming using snowball stemmer
# from nltk.stem import SnowballStemmer

# stemmer = SnowballStemmer("english")

# word = input("Enter a word: ")

# print("Original:", word)
# print("Stem:", stemmer.stem(word))

# 5.stemming a list of words
# from nltk.stem import LancasterStemmer

# stemmer = LancasterStemmer()

# words = ["running", "jumps", "easily", "studies"]

# for word in words:
#     print(word, "→", stemmer.stem(word))