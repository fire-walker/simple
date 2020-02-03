import os
from bs4 import BeautifulSoup

title = input("Enter the title name: ")

with open('input.txt', 'r') as file:
    lines = file.readlines()

# clean the input data
line = []
for i in lines:
    line.append(i.replace('\n', '').strip())

# filter the white spaces left
line = list(filter(None, line))

# the index file
body = BeautifulSoup('<article></article>', features='html.parser')






# create the h1 tag  and delete it from the list
header = BeautifulSoup(line[0], features='html.parser')
header.string.wrap(header.new_tag('h1'))
body.article.append(header)

# tag the paragraph and read more and add them to the body
soup = BeautifulSoup('<p></p>', features='html.parser')
soup.p.append(line[1])
soup.p.append(BeautifulSoup(f"<a href='{title.under()}.html' class='read'> Read more...</a></p>", features='html.parser'))
body.article.append(soup)

# open the source file
with open('../index.html', 'r') as file:
    soup = BeautifulSoup(file, features="html.parser")

# find the editing location of the source file
tag = soup.find('div', {'class': 'wrapper'})
tag.insert(0, body)

# save the new edited source file
with open('../index.html', 'w') as file:
    file.write(str(soup))

del body



# the seperate post
body = BeautifulSoup('<article></article>', features='html.parser')

# create the h1 tag with the class and delete it
header = BeautifulSoup(line[0], features='html.parser')
tag = header.new_tag('h1')
tag['class'] = 'article-h1'
header.string.wrap(tag)
body.article.append(header)
del line[0]

# tag the remaining paragraphs
for i in line:
    soup = BeautifulSoup(i, features='html.parser')
    tag = soup.new_tag('p')
    tag['class'] = 'article-p'
    soup.string.wrap(tag)
    body.article.append(soup)

# open the template source file
with open('template.html', 'r') as file:
    soup = BeautifulSoup(file, features="html.parser")

# find the insertion location of the template
tag = soup.find('div', {'class': 'wrapper'})
tag.insert(0, body)

# insert the title
tle = BeautifulSoup(title, features='html.parser')
tag = tle.new_tag('title')
tle.string.wrap(tag)
soup.head.insert(0, tle)

# save the edited file
with open(f'../posts/{title.under()}.html', 'w') as file:
    file.write(str(soup))


# the next thing to do is to automate the codebox. also i gotta invent some syntax to make it possible to add the colors and all
# the $ should be a constant so no input there
# i could use the ```docker `run` static-site``` like this sorta

# you know what, i could also make a front end for this program. huh