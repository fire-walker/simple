# from bs4 import BeautifulSoup

# line = ['Lorem ipsum.',
#         'Possimus mollitia ex ipsa. Molestias eum aspernatur tempore. thing thing thing. help help help.',
#         'Laboriosam odit reiciendis omnis officia itaque sit vel numquam voluptatibus.']


# x = 0
# for i in line[1].split():
#     x += 1

# if x < 60: #60
#     soup = BeautifulSoup('<p></p>', features='html.parser')
#     soup.p.append(line[2])
#     soup.p.append(BeautifulSoup(f"<a href='thing.html' class='read'> Read more...</a>", features='html.parser'))
#     thing = BeautifulSoup('<p></p>', features='html.parser')
#     thing.p.append(line[1])
#     soup.insert(0, thing)

# if x > 100: #100
#     thing = ''
#     parts = list(filter(None, line[1].split('.')))
#     for i in parts:
#         thing = (thing + i + '.')
#         x = 0
#         for i in thing.split():
#             x += 1
#         if x > 60:
#             break
#     soup = BeautifulSoup('<p></p>', features='html.parser')
#     soup.p.append(thing)
#     soup.p.append(BeautifulSoup(f"<a href='thing.html' class='read'> Read more...</a>", features='html.parser'))
# if larger, just split by '.' and join till the word count goes up to the amount







# from bs4 import BeautifulSoup



# line = ['Lorem ipsum.',
#         'Possimus mollitia ex ipsa. Molestias eum aspernatur tempore.',
#         '`docker <run> static-site`',
#         '`pip <install> discord.py`',
#         'Laboriosam odit reiciendis omnis officia itaque sit vel numquam voluptatibus.']

# code = {}
# code2 = {}
# x = 0
# for i in line:
#     if i.startswith('`') and i.endswith('`'):
#         i = i.replace('`', '')
#         code[x] = i
#     x += 1

# for x,y in code.items():
#     del line[x]
#     words = y.split(' ')
#     box = BeautifulSoup("<p class='code-box'></p>", features='html.parser')

#     for i in words:
#         if i.startswith('<') and i.endswith('>'):
#             i = i.replace('>', '')
#             i = i.replace('<', '')

#             soup = BeautifulSoup(i, features='html.parser')
#             tag = soup.new_tag('spam')
#             tag['class'] = 'code-box3'
#             soup.string.wrap(tag)
#             box.p.append(soup)
#         else:
#             soup = BeautifulSoup(i, features='html.parser')
#             box.p.append(soup)
    
#     box.p.insert(0, BeautifulSoup("<spam class='code-box2'>$</spam>", features='html.parser'))
#     code2[x] = box

    
# print(code2)
# line = [1, 2, 3, 4, 5, 6, 7, 8]

# thing = {2 : 'thing',
#          5 : 'thing'}


# t = list(thing.keys())
# for i in sorted(t, reverse=True):
#     del line[i]

# print(line)
from datetime import datetime
from git import Repo
import os

os.chdir(r'E:/Code\Sites')


now = datetime.now()
time = now.strftime("%Y/%m/%d, %H:%M:%S")


repo_dir = r'just-write.github.io'
repo = Repo(repo_dir)
file = r'index.html'
commit_message = 'a simple message'
repo.index.add(file)
repo.index.commit(time)
origin = repo.remote('origin')
origin.push()
