from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import pandas as pd
import numpy as np
import syllapy
import os

df = pd.read_excel(r'C:/Users/Mi Notebook/Documents/blackcoffer/input/Output Data Structure.xlsx')
df = df.astype(str)
df['URL_ID'] = df['URL_ID'].apply(lambda x: "'" + x + "'")

with open('C:/Users/Mi Notebook/Documents/blackcoffer/input/Dictionary/positive-words.txt', 'r', encoding = 'utf-8') as file:
    data = file.read().replace('\n',' ').lower()
positive_tokens = word_tokenize(data)
with open('C:/Users/Mi Notebook/Documents/blackcoffer/input/Dictionary/negative-words.txt', 'r', encoding = 'ANSI') as file:
    data = file.read().replace('\n',' ').lower()
negative_tokens = word_tokenize(data)

for i in df.index:
    try:
        with open('C:/Users/Mi Notebook/Documents/blackcoffer/cleaned/' + df.iloc[i, 0] + '.txt', 'r', encoding = 'utf-8') as file:
            data = file.read()
        special_char = ['?', '.', ',', ';', ':', '/', '"', "'", '[', ']', '*', '$', '@', '!', '~', '+', '_', '-', '<']
        for z in special_char:
            data = data.replace(z, '')
        tokens = word_tokenize(data)
        positive_score = 0
        negative_score = 0
        total_words = 0
        total_sent = 0
        total_comp = 0
        total_syl = 0
        personal = 0
        pronouns = ['I', 'we', 'my', 'ours', 'us']

        for j in tokens:
            if j in positive_tokens:
                positive_score = positive_score + 1
            if j in negative_tokens:
                negative_score = negative_score + 1
            total_words = total_words + 1
            if syllapy.count(j) > 2:
                total_comp = total_comp + 1
            temp = syllapy.count(j)
            total_syl = total_syl + temp

        with open('C:/Users/Mi Notebook/Documents/blackcoffer/output/' + df.iloc[i, 0] + '.txt', 'r', encoding = 'utf-8') as file:
            info = file.read()
        sent_tokens = sent_tokenize(info)
        tokens = word_tokenize(info)
        for j in sent_tokens:
            total_sent = total_sent + 1
        for j in tokens:
            if j in pronouns:
                personal = personal + 1
        
        avg_len = total_words / total_sent
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / ((total_words) + 0.000001)
        percent_comp = total_comp / total_words
        fog_index = 0.4 * (avg_len + percent_comp)
        data = data.replace(' ', '')
        total_char = len(data)
        avg_word = total_char / total_words

        df.iloc[i, 2] = positive_score
        df.iloc[i, 3] = negative_score
        df.iloc[i, 4] = polarity_score
        df.iloc[i, 5] = subjectivity_score
        df.iloc[i, 6] = avg_len
        df.iloc[i, 7] = percent_comp
        df.iloc[i, 8] = fog_index
        df.iloc[i, 9] = avg_len
        df.iloc[i, 10] = total_comp
        df.iloc[i, 11] = total_words
        df.iloc[i, 12] = total_syl
        df.iloc[i, 13] = personal
        df.iloc[i, 14] = avg_word

    except FileNotFoundError:
        df.iloc[i, 2:] = np.nan
        i = i + 1

df.to_excel('C:/Users/Mi Notebook/Documents/blackcoffer/final_output.xlsx')
