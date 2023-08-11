from bs4 import BeautifulSoup
import pandas as pd
import requests

df = pd.read_csv(r'C:/Users/Mi Notebook/Documents/blackcoffer/input/url_list.csv')
df = df.astype(str)
df['URL_ID'] = df['URL_ID'].apply(lambda x: "'" + x + "'")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

for i in df.index:
    hit_site = requests.get(df.iloc[i, 1], headers = headers).text
    soup = BeautifulSoup(hit_site, 'lxml')
    if soup.find('h1', class_ = 'tdb-title-text') == None:
        i = i + 1
    else:
        title = soup.find('h1', class_ = 'tdb-title-text').text + " "
        html_body = soup.find('div', class_ = 'td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
        body = ''
        points = ''
        for j in html_body.find_all('p'):
            body = body + str(j.get_text() + " ")
        for j in html_body.find_all('li'):
            points = points + str(j.get_text() + " ") 
        content = title + body + points
        with open('C:/Users/Mi Notebook/Documents/blackcoffer/output/' + df.iloc[i, 0] + '.txt', 'w', encoding = 'utf-8') as file:
            data = file.write(content)
        print(df.iloc[i, 0])

for i in df.index:
    hit_site = requests.get(df.iloc[i, 1], headers = headers).text
    soup = BeautifulSoup(hit_site, 'lxml')
    if soup.find('h1', class_ = 'entry-title') == None:
        i = i + 1
    else:
        title = soup.find('h1', class_ = 'entry-title').text + " "
        html_body = soup.find('div', class_ = 'td-post-content tagdiv-type')
        body = ''
        points = ''
        for j in html_body.find_all('p'):
            body = body + str(j.get_text() + " ")
        for j in html_body.find_all('li'):
            points = points + str(j.get_text() + " ") 
        content = title + body + points
        with open('C:/Users/Mi Notebook/Documents/blackcoffer/output/' + df.iloc[i, 0] + '.txt', 'w', encoding = 'utf-8') as file:
            data = file.write(content)
        print(df.iloc[i, 0])
