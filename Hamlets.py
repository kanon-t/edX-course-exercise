import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "\\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return num_unique, counts


'''
Exercise 1
In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x).

Instructions
Read in the data as a pandas dataframe using pd.read_csv. Use the index_col argument to set the first column in the csv file as the index for the dataframe. 
'''

hamlets = '/Users/Kanon/Desktop/Coding/Python/3.2/hamlets.csv'    
df = pd.read_csv(hamlets, index_col=0)
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

counted_text = count_words_fast(text)
#counted_text = {}

for language in df:
    for word in text:
        text = str(df['text'])
        #num_unique, counts = word_stats(count_words_fast(text))
        data = pd.DataFrame({
            "word": list(counted_text.keys()),
            "count": list(counted_text.values())})

print(counted_text)
