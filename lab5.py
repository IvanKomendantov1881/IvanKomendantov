import re, html, csv

# 1
f = open('task1-ru.txt', 'r').read()
numbers = re.findall(r'\b[0-9]\b', f)
combination = re.findall(r'\b(?=\w*[A-Za-zА-Яа-я])(?=\w*\d)\w+\b', f)
print(numbers, combination, sep='\n')

#2
with open('task2.html', 'r', encoding='utf-8') as f:
    html_text = f.read()
pattern = r'https://[\w.-/]+?\.(?:jpg|jpeg|png|gif)'
result = re.findall(pattern, html_text)
print(result)

#3
pattern = r'\d\s+(\w+\@[\w.-]+\.\w+)\s(\w+)\s(\d{4}-\d{2}-\d{2})\s()'
f = open('task3.txt', 'r').readline().split()
idu = [id for id in f if re.fullmatch(r'\d+', id)]
email = [em for em in f if re.fullmatch(r'\S+@\S+', em)]
name = [name for name in f if re.fullmatch(r'[A-Z][a-zA-Z]+', name)]
date = [dt for dt in f if re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt)]
link = [lk for lk in f if re.fullmatch(r'https?://[^\s]+', lk.strip())]
row = [[idu[i], name[i], email[i], link[i], date[i]] for i in range(len(idu))]

with open('result.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Id', 'Name', 'Email', 'URL', 'Date'])
    writer.writerows(row)