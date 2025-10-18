import pandas as pd
import random as rd
df = pd.read_csv('books.csv', sep=';', encoding='utf-8')

# 1
def cnt_name():
    return (df['Название'].str.len() > 30).sum()
print(cnt_name())


# 2
name_author = input('Введите название автора:').strip()
min_price = 150
df['Автор'] = df['Автор'].str.strip()
df['Цена поступления'] = pd.to_numeric(df['Цена поступления'])
mask = (df['Автор'] == name_author) & (df['Цена поступления'] >= min_price)
result = df[mask]
print(result[['Название', 'Автор', 'Цена поступления']])


#3
def rndclub():
    author = rd.choice(df['Автор'])
    if str(author)[0]=='n':
        author='Автор не известен'
    name = rd.choice(df['Название'])
    year = rd.choice(df['Дата поступления'])[6:10]
    return f'{author}. {name} - {year}'

with open('bibliography.txt', 'w', encoding='utf-8') as f:
    for _ in range(20):
        f.write(rndclub()+'\n')
print('file done')


# 4
df = pd.read_xml('currency.xml', parser='etree', encoding='cp1251')
df['Value'] = df['Value'].str.replace(',','.').astype(float)
print(df['Value'].sum()/len(df['Value']))

# 5 additional
tags = df['Название']
list_tags = []
pop_list = []
set_tags = set()
for i in tags:
    if '#' in i:
        list_tags.append(i.strip().split('#'))
print(list_tags)
for j in list_tags:
    for h in j:
        clean_tag = h.strip()
        if clean_tag:
            set_tags.add(clean_tag)
            pop_list.append(clean_tag)

for _ in range(20):
    most_popular = max(set_tags, key=pop_list.count)
    print(most_popular)
    pop_list.remove(most_popular)
print(set_tags)
