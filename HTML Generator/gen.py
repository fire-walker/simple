import os
from bs4 import BeautifulSoup


title = input("Enter the title name: ")

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt'), 'r') as file:
    lines = file.readlines()

# clean the input data
line = []
for i in lines:
    line.append(i.replace('\n', '').strip())

line = list(filter(None, line))








# the index file
body = BeautifulSoup('<article></article>', features='html.parser')

# create the h1 tag  and delete it from the list
header = BeautifulSoup(line[0], features='html.parser')
header.string.wrap(header.new_tag('h1'))
body.article.append(header)

# tag the paragraph and read more and add them to the body
x = 0
for i in line[1].split():
    x += 1

if x < 60:
    soup = BeautifulSoup('<p></p>', features='html.parser')
    soup.p.append(line[2])
    soup.p.append(BeautifulSoup(
        f"<a href='{title.lower().replace(' ', '-')}.html' class='read'> Read more...</a>", features='html.parser'))
    thing = BeautifulSoup('<p></p>', features='html.parser')
    thing.p.append(line[1])
    soup.insert(0, thing)
    body.article.append(soup)

elif x > 100:
    thing = ''
    parts = list(filter(None, line[1].split('.')))
    for i in parts:
        thing = (thing + i + '.')
        x = 0
        for i in thing.split():
            x += 1
        if x > 60:
            break
    soup = BeautifulSoup('<p></p>', features='html.parser')
    soup.p.append(thing)
    soup.p.append(BeautifulSoup(
        f"<a href='{title.lower().replace(' ', '-')}.html' class='read'> Read more...</a>", features='html.parser'))
    body.article.append(soup)

else:
    soup = BeautifulSoup('<p></p>', features='html.parser')
    soup.p.append(line[1])
    soup.p.append(BeautifulSoup(
        f"<a href='{title.lower().replace(' ', '-')}.html' class='read'> Read more...</a>", features='html.parser'))
    body.article.append(soup)

# open the source file
with open(os.path.join(__location__, '../index.html'), 'r') as file:
    soup = BeautifulSoup(file, features="html.parser")

# find the editing location of the source file
tag = soup.find('div', {'class': 'wrapper'})
tag.insert(0, body)

# save the new edited source file
with open(os.path.join(__location__, '../index.html'), 'w') as file:
    file.write(str(soup))






# the seperate post
body = BeautifulSoup('<article></article>', features='html.parser')

# create the whole code box
code = {}
code2 = {}
x = 0
for i in line:
    if i.startswith('`') and i.endswith('`'):
        i = i.replace('`', '')
        code[x] = i
    x += 1

for x,y in code.items():
    words = y.split(' ')
    box = BeautifulSoup("<p class='code-box'></p>", features='html.parser')

    for i in words:
        if i.startswith('<') and i.endswith('>'):
            i = i.replace('>', '')
            i = i.replace('<', '')

            soup = BeautifulSoup(i, features='html.parser')
            tag = soup.new_tag('spam')
            tag['class'] = 'code-box3'
            soup.string.wrap(tag)
            box.p.append(soup)
        else:
            soup = BeautifulSoup(i, features='html.parser')
            box.p.append(soup)
    
    box.p.insert(0, BeautifulSoup("<spam class='code-box2'>$</spam>", features='html.parser'))
    code2[x] = box

# delete the codebox lines from the list
t = list(code2.keys())
for i in sorted(t, reverse=True):
    del line[i]

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

# insert the codeboxes to the body
for x, y in code2.items():
    body.article.insert(x, y)

# open the template source file
with open(os.path.join(__location__, 'template.html'), 'r') as file:
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
with open(os.path.join(__location__, '../{}.html' .format(title.lower().replace(' ', '-'))), 'w') as file:
    file.write(str(soup))





# you know what, i could also make a front end for this program. huh
# of a whole site manager suite
