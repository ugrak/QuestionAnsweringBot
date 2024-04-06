"""Created by SeaBearYak for JetBrains Academy"""
from nltk.tokenize import word_tokenize
import string

punctuation = string.punctuation.replace("'", "")
with open('jeopardy.json') as input_file:
    print("Hello! I'm Questian, a question answering bot who knows "
          "answers to all questions from the 'Jeopardy!' game.")
    question = word_tokenize(input("Ask me something!").lower())
    print("Let's play!")
    # Таблица трансляции для удаления знаков пунктуации
    trans_table = str.maketrans('', '', punctuation)
    # Удаление знаков пунктуации из каждого слова
    cleaned_words = [word.translate(trans_table) for word in question if word.translate(trans_table)]
    print(cleaned_words)
