import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text: str) -> Counter:
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "\\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts: Counter):
    num_unique = len(word_counts)
    counts = dict(word_counts)
    return num_unique, counts


'''
Exercise 1
In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x).

Instructions
Read in the data as a pandas dataframe using pd.read_csv. Use the index_col argument to set the first column in the csv file as the index for the dataframe. 
'''

def exercise_1():
    file_name = 'hamlets.csv'
    df = pd.read_csv(file_name, index_col=0)
    print(df)


'''
Exercise 2
In this exercise, we will summarize the text for a single translation of Hamlet in a pandas dataframe.

Instructions
Find the dictionary of word frequency in text by calling count_words_fast(). Store this as counted_text.
Create a pandas dataframe named data.
Using counted_text, define two columns in data:
word, consisting of each unique word in text.
count, consisting of the number of times each word in word is included in the text.
'''

def exercise_2():
    file_name = 'hamlets.csv'
    df = pd.read_csv(file_name, index_col=0)
    
    df_languages = df['language']
    df_texts = df['text']
    
    for language_key in df_languages.keys():
        language_name = df_languages[language_key]
        text = df_texts[language_key]
    
        num_unique, word_counts = word_stats(count_words_fast(text))
    
        print(f'Language name: {language_name}')
        print(f' - Unique words: {num_unique}')
        print(f' - Hamlet mentioned {word_counts["hamlet"]} times.\n')


if __name__ == '__main__':
    exercise_2()

