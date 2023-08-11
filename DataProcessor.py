from nltk.tokenize import word_tokenize
import pandas as pd
import os

df = pd.read_csv(r'C:/Users/Mi Notebook/Documents/blackcoffer/input/url_list.csv')
df = df.astype(str)
df['URL_ID'] = df['URL_ID'].apply(lambda x: "'" + x + "'")

path = 'C:/Users/Mi Notebook/Documents/blackcoffer/input/StopWords/'
os.chdir(path)
with open('C:/Users/Mi Notebook/Documents/blackcoffer/input/StopWords_Currencies.txt', 'r', encoding = 'ANSI') as file:
    stopwords = file.read().replace('\n',' ').lower()
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = file.read().replace('\n',' ').lower()
        stopwords = stopwords + ' ' + data
stopwords = word_tokenize(stopwords)

for i in df.index:
    try:
        with open('C:/Users/Mi Notebook/Documents/blackcoffer/output/' + df.iloc[i, 0] + '.txt', 'r', encoding = 'utf-8') as file:
            data = file.read().lower()
        tokens = word_tokenize(data)
        cleaned_list = []
        for j in tokens:
            if j not in stopwords:
                cleaned_list.append(j)
        cleaned_str = ''
        for j in cleaned_list:
            cleaned_str = cleaned_str + ' ' + j
        with open('C:/Users/Mi Notebook/Documents/blackcoffer/cleaned/' + df.iloc[i, 0] + '.txt', 'w', encoding = 'utf-8') as file:
            data = file.write(cleaned_str)
    except FileNotFoundError:
        i = i + 1
