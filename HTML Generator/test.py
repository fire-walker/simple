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
from __future__ import print_function, unicode_literals

import os
import sys
import time
import json
import random
import string
import shutil
import subprocess
from halo import Halo
from bs4 import BeautifulSoup
from tabulate import tabulate
from tkinter import Tk, filedialog
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt
from bs4 import BeautifulSoup
import os

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes


# digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

# digest.update(b"abc")
# digest2 = digest.copy()
# digest2.update(b'abc')
# digest2.finalize()

# digest.update(b'abc')
# digest.finalize()

# if digest2 == digest:
#     print(True)
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
import hashlib

# with open(os.path.join(__location__, 'input.txt'), 'rb') as file:
#     first = file.read()

# loc = os.path.join(__location__, 'input.txt')
# subprocess.run(["notepad", loc])

# with open(os.path.join(__location__, 'input.txt'), 'rb') as file:
#     second = file.read()

# thing = hashlib.sha3_512(first).hexdigest()
# thing2 = hashlib.sha3_512(second).hexdigest()


# if thing == thing2:
#     print(True)
# else:
#     print(False)
# digest2 = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
# digest2.update(b"abc")

# if digest == digest2:
#     print(True)
# else:
#     print(False)
# custom_desc_input = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter description:",
#     'validate': lambda i: len(i.split(' ')) > 10
# }

# style = style_from_dict({
#     Token.QuestionMark: '#000',
#     Token.Selected: '#535353',
#     Token.Pointer: '#535353 bold',
#     Token.Instruction: '#000',
#     Token.Answer: '#535353',
#     Token.Question: '#E47687',
# })

# post_doubt_edit = {
#     'type': 'confirm',
#     'name': 'item',
#     'message': "Are you sure to continue: [y/n]",
# }

# answers = prompt(post_doubt_edit, style=style)
# print(answers)



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

# thing = max(thing.keys())
# print(type(thing))
# t = list(thing.keys())
# for i in sorted(t, reverse=True):
#     del line[i]

# print(line)
# from datetime import datetime
# from git import Repo
import os

# os.chdir(r'E:/Code\Sites')


# now = datetime.now()
# time = now.strftime("%Y/%m/%d, %H:%M:%S")


# repo_dir = r'just-write.github.io'
# repo = Repo(repo_dir)
# file = r'index.html'
# commit_message = 'a simple message'
# repo.index.add(file)
# repo.index.commit(time)
# origin = repo.remote('origin')
# origin.push()
import curses

# screen = curses.initscr()
# screen.addstr("Press any key...")
# screen.refresh()

# while 1==1:
#     c = screen.getch()

# curses.endwin()

# # Convert the key to ASCII and print ordinal value
# print("You pressed %s which is keycode %d." % (chr(c), c))


# curses.nocbreak()
# thing.keypad(False)
# curses.echo()
# curses.endwin()


import os
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))

# print(__location__)
#

# enter = """
#     <div class='something'>
#     <div class = "wrapper" >
#        <article >
#             <h1 class = "article-h1" > Hello World < /h1 >

#             <p class = "article-p" >
#               Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi sit voluptate deleniti hic amet
#                consequatur earum alias doloribus officiis nulla nam harum ad, expedita ullam accusamus mollitia modi
#                 placeat sapiente. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptate, earum esse.
#                 Molestias quaerat fuga commodi, eligendi deserunt quidem numquam ratione culpa earum, sunt aspernatur
#                 consequuntur suscipit adipisci.
#             </p >

#             <p class = "code-box" > <span class = "code-box2" >$</span > docker < span class = "code-box3" > run < /span > static-site < /p >

#             <p class = "article-p" >
#               Exercitationem cupiditate labore debitis expedita officiis, asperiores
#                sapiente numquam? Hic ut, a debitis quia nobis doloremque sit ipsam impedit temporibus aperiam earum.
#                 Molestias illum unde praesentium veritatis ut optio minima deleniti! Alias porro laboriosam vel.
#                 Quibusdam illum, nihil illo iste neque eveniet corrupti eligendi eaque voluptates nemo? Repellat veniam
#                 iusto cum magnam et nesciunt laborum temporibus atque, quo perferendis repudiandae magni minus quos
#                 tenetur assumenda corrupti natus non, reprehenderit ducimus molestias similique cumque.
#             </p >

#             <p class = "article-p" >
#               Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga nihil nobis reprehenderit
#                error provident. Esse labore eveniet ducimus nihil vel dignissimos delectus enim eaque amet accusantium
#                 porro nesciunt, doloribus maxime similique sint tenetur ad? Illum deleniti tenetur, voluptatum quis,
# #                 architecto unde omnis est natus voluptatibus reprehenderit molestiae quasi dignissimos error!
# #             </p >
# #         </article >

# #         <hr / >
# #         <h1 class = "hr-h1">the end</h1>
# #     </div >
# #     </div>
# # """
# # soup = BeautifulSoup(enter, features='html.parser')

# # tag = soup.find('div', {'class': 'wrapper'})

# # body = """
# # <div class="wrapper">
# #     <h1>Hello World</h1>
# # </div>
# # """

# # body = BeautifulSoup(body, features='html.parser')
# # tag.replace_with(body)
import os
# # # print(soup)
# # from bs4 import UnicodeDammit
# # __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


# # with open(os.path.join(__location__, 'temp.txt'), 'r', encoding='utf8') as file:
# #     soup = BeautifulSoup(file, features='html.parser')


# # print(str(soup))



# # print(soup.decode("windows-1252"))
# # print(soup.decode('utf8'))
# # __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


# # base_files = (file for file in os.listdir(__location__) if os.path.isfile(os.path.join(__location__, file)))

# # temp_child = (file for file in os.listdir(os.path.join(__location__, r'HTML Generator')) if os.path.isfile(os.path.join(os.path.join(__location__, r'HTML Generator'), file)))
# # children = []
# # for i in temp_child:
# #     i = os.path.join(r'HTML Generator', i)
# #     children.append(i)

# # files = children + list(base_files)
# # print(files)
import os
# from bs4 import BeautifulSoup
import subprocess





# __location__ = os.path.realpath(os.path.join(
#     os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


# with open(os.path.join(__location__, 'hello_v2.html'), 'r') as file:
#     body = BeautifulSoup(file, features='html.parser')

# #find the identifier tag
# tag = body.find_all('article')[0]
# num = int(tag['class'][0])


# output = []

# h1 = ' '.join(tag.find('h1').string.split())
# output.append(h1)

# paragraphs = tag.find_all('p')

# for i in paragraphs:
#     if i['class'][0] == 'article-p':
#         p = ' '.join(i.string.split())
#         output.append(p)

#     else:
#         box_checker = []
#         code_box3 = i.find_all('span', {'class' : 'code-box3'})

#         for j in code_box3:
#             box_checker.append(j.string)

#         words = i.get_text(' ').split(' ')
#         for i,val in enumerate(words):
#             if val == '$':
#                 words.remove(val)

#             elif val in box_checker:
#                 words[i] = f'`{val}`'

#         out = ' '.join(words)
#         output.append(f'<-{out}->')


# output = '\n\n'.join(output)
# with open(os.path.join(__location__, 'temp.txt'), 'w') as file:
#     file.write(output)

# with open(os.path.join(__location__, 'temp.txt'), 'r') as file:
#     lines = file.readlines()
# # 22222222222222222222222222222

# for i,j in enumerate(lines):
#     lines[i] = j.replace('\n', '').strip()




# # the seperate post
# article = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

# # create the whole code box
# code = {}
# code2 = {}
# x = 0
# for i in lines:
#     if i.startswith('<-') and i.endswith('->'):
#         i = i.replace('<-', '')
#         i = i.replace('->', '')
#         code[x] = i
#     x += 1

# for x, y in code.items():
#     words = y.split(' ')
#     box = BeautifulSoup("<p class='code-box'></p>", features='html.parser')

#     for i in words:
#         if i.startswith('`') and i.endswith('`'):
#             i = i.replace('`', '')

#             soup = BeautifulSoup(i, features='html.parser')
#             box3 = soup.new_tag('span')
#             box3['class'] = 'code-box3'
#             soup.string.wrap(box3)
#             box.p.append(soup)
#             box.p.append(' ')
#         else:
#             soup = BeautifulSoup(i, features='html.parser')
#             box.p.append(soup)
#             box.p.append(' ')

#     box.p.insert(0, BeautifulSoup("<span class='code-box2'>$ </span>", features='html.parser'))
#     code2[x] = box

# # delete the codebox lines from the list
# t = list(code2.keys())
# for i in sorted(t, reverse=True):
#     del lines[i]

# # create the h1 tag with the class and delete it
# header = BeautifulSoup(lines[0], features='html.parser')
# header_tag = header.new_tag('h1')
# header_tag['class'] = 'article-h1'
# header.string.wrap(header_tag)
# article.article.append(header)
# del lines[0]

# # tag the remaining paragraphs
# for i in lines:
#     soup = BeautifulSoup(i, features='html.parser')
#     para_tag = soup.new_tag('p')
#     para_tag['class'] = 'article-p'
#     soup.string.wrap(para_tag)
#     article.article.append(soup)

# # insert the codeboxes to the body
# for x, y in code2.items():
#     article.article.insert(x, y)

# # also make a thing where you can change the title name also and the index page descrpititon for the said file bmake this an optioneal question after finishing edits obn the fle at hand, so you can update it as per the changed stuff and then make ffurther adjustments


# wrapper = body.find('div', {'class': 'wrapper'})
# wrapper.clear()
# wrapper.append(article)


# os.remove(os.path.join(__location__, 'temp.txt'))

# save the edited data
# with open(os.path.join(__location__, answer), 'w') as file:
#     file.write(str(body))

# test = '       this is    a thing   mate    '

# test = "".join(test.split())

# print(test)

# i = "<p>some <a href='some'>thing</a> cool</p>"
# soup = BeautifulSoup(i, features='html.parser')
# print(soup.a['href'])


# def seperate_post(filename, num, title=None):
#         __location__ = os.path.realpath(os.path.join(
#             os.getcwd(), os.path.dirname(__file__)))

#         with open(os.path.join(__location__, filename), 'r') as file:
#             input_data = file.readlines()

#         # clean the input data
#         line = []
#         for i in input_data:
#             line.append(i.replace('\n', '').strip())

#         cleaned_input = list(filter(None, line))

#         body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

#         # create the whole code box
#         code = {}
#         code2 = {}
#         x = 0
#         for i in cleaned_input:
#             if i.startswith('<-') and i.endswith('->'):
#                 i = i.replace('<-', '')
#                 i = i.replace('->', '')
#                 code[x] = i
#             x += 1

#         for x, y in code.items():
#             words = y.split(' ')
#             box = BeautifulSoup("<p class='code-box'></p>",
#                                 features='html.parser')

#             for i in words:
#                 i = "".join(i.split())
#                 if i.startswith('`') and i.endswith('`'):
#                     i = i.replace('`', '')

#                     soup = BeautifulSoup(i, features='html.parser')
#                     tag = soup.new_tag('span')
#                     tag['class'] = 'code-box3'
#                     soup.string.wrap(tag)
#                     box.p.append(soup)
#                     box.p.append(' ')
#                 else:
#                     soup = BeautifulSoup(i, features='html.parser')
#                     box.p.append(soup)
#                     box.p.append(' ')

#             box.p.insert(0, BeautifulSoup(
#                 "<span class='code-box2'>$ </span>", features='html.parser'))
#             code2[x] = box

#         # delete the codebox lines from the list
#         t = list(code2.keys())
#         for i in sorted(t, reverse=True):
#             del cleaned_input[i]

#         # create the h1 tag with the class and delete it
#         header = BeautifulSoup(cleaned_input[0], features='html.parser')
#         tag = header.new_tag('h1')
#         tag['class'] = 'article-h1'
#         header.string.wrap(tag)
#         body.article.append(header)
#         del cleaned_input[0]

#         # tag the remaining paragraphs and do the inner formatting
#         for i in cleaned_input:
#             seperated = i.split(' ')

#             for i, j in enumerate(seperated):
#                 # the links
#                 if j.startswith('<:') and j.endswith(':>'):
#                     j = j.replace('<:', '')
#                     j = j.replace(':>', '')
#                     elements = j.split('--')

#                     soup = BeautifulSoup('', features='html.parser')
#                     tag = soup.new_tag('a', href=elements[1])
#                     tag['class'] = 'link'
#                     tag.string = elements[0]
#                     soup.append(tag)
#                     seperated[i] = str(soup)

#                 # the code snippets
#                 elif j.startswith('<~') and j.endswith('~>'):
#                     j = j.replace('<~', '')
#                     j = j.replace('~>', '')

#                     soup = BeautifulSoup('', features='html.parser')
#                     tag = soup.new_tag('span')
#                     tag['class'] = 'code-snippet'
#                     tag.string = j
#                     soup.append(tag)
#                     seperated[i] = str(soup)

#             para = ' '.join(seperated)
#             para = BeautifulSoup(para, features='html.parser')

#             soup = BeautifulSoup('', features='html.parser')
#             tag = soup.new_tag('p')
#             tag['class'] = 'article-p'
#             soup.append(tag)
#             soup.p.append(para)
#             body.article.append(soup)

#         # insert the codeboxes to the body
#         for x, y in code2.items():
#             body.article.insert(x, y)

#         # open the template source file
#         with open(os.path.join(__location__, 'template.html'), 'r') as file:
#             soup = BeautifulSoup(file, features="html.parser")

#         # find the insertion location of the template
#         tag = soup.find('div', {'class': 'wrapper'})
#         tag.insert(0, body)

#         # title config
#         if title == None:
#                 title = filename

#         # insert the title
#         tle = BeautifulSoup(title, features='html.parser')
#         tag = tle.new_tag('title')
#         tle.string.wrap(tag)
#         soup.head.insert(0, tle)

#         # save the edited file
#         with open(os.path.join(__location__, '../{}.html' .format(title.lower().replace(' ', '-'))), 'w') as file:
#             file.write(str(soup))


# seperate_post('input.txt', 2)

# thing = [1, 2, 3, 4, 5]
# # for i in thing[1:]:
# #     print(i)


# soup = BeautifulSoup('<p>something mate</p>', features='html.parser')

# thing = soup.find('article', class_=f'{1 + 5}')
# print(thing)


# # remember the keep before for the custom desc
# while True:
#     print('thing')
#     while True:
#         break

# print(soup)
# # para = 'something'
# # soup.p.string = para
# # # print(soup
import os

# location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
# # files = [f for f in os.listdir(f'{loc}/../') + os.listdir(loc) if f.endswith('.html') and not f.startswith('index')]

# print(files)

# file = open(os.path.join(location, '../hello_v2.html'), 'r+')

# print(post.body.header.h1.a.string)
# num = 1
# with open(os.path.join(location, 'index.html'), 'r') as file:
#     body = BeautifulSoup(file, features='html.parser')

# wrapper = body.find('div', {'class': 'wrapper'})
# # article = body.find('article', {'class': num})
# # article.decompose()
# print(wrapper)
import time
# from halo import Halo

# spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
# spinner.start()

# time.sleep(5)
# spinner.stop()

# # file_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# # base_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
# cleaned_input = ['some', 'thing', '<-some->\n', '<-dude->']
# # code = {i:j for (i,j) in enumerate(cleaned_input) if j.startswith('<-') and j.endswith('->')}
# # code = {i:j.replace('<-', '').replace('->', '') for (i,j) in code.items()}
# print(code)
# line = []
# for i in input_data:
#     line.append(i.replace('\n', '').strip())

# line = [f.replace('\n', '').strip() for f in input_data]
# dthing = {1:'some', 2:'somesomeosme'}

# clear = [y for (x,y) in enumerate(input_data) if x not in dthing.keys()]
# clear.insert(2, '<-some->')
# clear.insert(1, 'thing')
# print(clear)

# for x,y in enumerate(input_data):
#     if x in dthing.keys():
# #         print(True)
# #     else:
# #         print(False)
# cleaned_input = [filter(None, [f.replace('\n', '').strip() for f in input_data])]
# print(cleaned_input)

# x = 0
# some = len(cleaned_input[1].split())

# print(some)
# dthing = {1:1, 2:2, 3:3}
# x = 0
# for i in dthing.items():
#     x += 1
# y = len(dthing.keys())
# print(x, y)


# n = ''
# if n is None:
#     print('None')
# else:
#     print("Not None")
import random
import string
# filename = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
# print(filename)
import json


some = """
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi sit voluptate deleniti hic amet
    consequatur earum alias doloribus officiis nulla nam harum ad, expedita ullam accusamus mollitia modi
    placeat sapiente. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptate, earum esse.
    Molestias quaerat fuga commodi, eligendi deserunt quidem numquam ratione culpa earum, sunt aspernatur
    consequuntur suscipit adipisci.<a class="read" href="TUzBQiyw88TMwCLOxuQBdY1hRZngYh.html"> Read
        more...</a></p>
"""
soup = BeautifulSoup(some, features='html.parser')
soup.p.a.decompose()
print(" ".join(soup.p.string.split()))
# # {post_num: [last_edited, filename, date_created]}{
# table ={"0": ["index", "index.html", "last_edited", "date_created"],
#         "1": ["hello_v1", "hello_v1.html", "last_edited", "date_created"],
#         "2": ["hello_v2", "hello_v2.html", "last_edited", "date_created"],
#         "3": ["hello_v3", "hello_v3.html", "last_edited", "date_created"],
#         "4": ["hello_v4", "hello_v4.html", "last_edited", "date_created"],
#         "5": ["hello_v5", "Pudd2565O9KcSr0jHGWjzguY7FZJUo.html", "2020/04/15 20:47", "2020/04/15 20:46"]}

# places = [y[1] for x, y in dthing.items()]# if x != 0
# print(dthing[2][1])

import time
# thing = time.strftime('%Y/%m/%d %H:%M')
# print(thing)
# file_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# with open(os.path.join(file_dir, 'post_data.json'), "r") as file:
#     post_data = json.load(file)
#     post_data = {int(x) : y for x, y in post_data.items()}


# print(post_data[0])
import time
# dict_key = [x for x, y in dthing.items() if x == 2][0]
# dthing[dict_key][0] = time.strftime('%Y/%m/%d %H:%M')
# dthing[5] = ['some', 'some', 'some']
# print(dthing)
# from tabulate import tabulate

# # num = [x for x, y in table.items()]
# # title = [y[0] for x, y in table.items()]
# # filename = [y[1] for x, y in table.items()]
# # last = [y[2] for x, y in table.items()]
# # created = [y[3] for x, y in table.items()]

# # table =[[1, 'some', 'some'], [2, 'some2', 'some2'], [3, 'some3', 'some3']]
# table = [[x, y[0], y[2], y[3], y[1]] for x, y in table.items()]

# headers = 'class', 'title', 'last_edited', 'date_created', 'filename'
# print(tabulate(table, headers, tablefmt="pretty"))

import sys
# from termcolor import colored, cprint

# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')


# def print_red_on_cyan(x): return cprint(x, 'red', 'on_cyan')


# print_red_on_cyan('Hello, World!')
# print_red_on_cyan('Hello, Universe!')

# for i in range(10):
#     cprint(i, 'magenta', end=' ')

# cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

# from PyInquirer import Validator, ValidationError
# from PyInquirer import style_from_dict, Token, prompt

# style = style_from_dict({
#     Token.QuestionMark: '#000',
#     Token.Selected: '#535353',
#     Token.Pointer: '#535353 bold',
#     Token.Instruction: '#000',
#     Token.Answer: '#535353',
#     Token.Question: '#E47687',
# })

# custom_desc_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "thing is the default\n  Enter new description:"
# }

# custom_title_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter new page title name:"
# }

# custom_title_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter new page title name:"
# }

# index_title_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter new index page title:"
# }

# index_desc_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter new description:"
# }

# index_header_input_edit = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter new header:"
# }

# custom_desc_input = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter description:"
# }

# custom_title_input = {
#     'type': 'input',
#     'name': 'item',
#     'message': "Enter page title name:"
# }

# custom_desc = prompt(custom_desc_input_edit, style=style)['item']


# thing = 'some.txt'

# endings = ('.png')
# if thing.endswith(endings):
# # #     print('True')
# # # else:
# # #     print(False)

# # from bs4 import BeautifulSoup

# i = BeautifulSoup("<p class='article-vid'><video controls=''><source src='media/some2.mp4' type='video/mp4'/></video></p>", features='html.parser')
# # soup.img['src'] = 'some.jpg'
# # print(soup)
# # cleaned_input = {0 : '<media>',
#                  1 : '<media--some.png'}

# media = {i: j for (i, j) in cleaned_input.items() if j.startswith('<media')}
# media_new = {i: j for (i, j) in cleaned_input.items() if j == '<media>'}
# media_old = {i: j for (i, j) in cleaned_input.items() if j.startswith('<media--')}

# if media_old != {}:
#     for x, y in media_old.items():
#         files = y.split('--')[1]
        
#         image_endings = ('.png', '.jpg', '.jpeg')
#         if files.endswith(image_endings):
#             soup = BeautifulSoup('<p><img>', features='html.parser')
#             soup.p['class'] = 'article-img'
#             soup.img['src'] = f"media/{files}"
#             print(soup)
            
#         else:
#             extension = os.path.splitext(files)[1].replace('.', '')
#             soup = BeautifulSoup("<p><video controls><source>", features='html.parser')
#             soup.p['class'] = 'article-vid'
#             soup.source['src'] = f"media/{files}"
#             soup.source['type'] = f'video/{extension}'
#             print(soup)

# print(f"<media--{i.source['src'].split('/')[1]}>")
# thing = {1 : 33,
#          2 : 576,
#          3 : 465}
# print(list(thing.values()))
# thing2 = [4, 5, 6]
# thing1 = [4, 6, 7]
# for i in thing1:
#     if i not in thing2:
#         print(i)
# # print(thing + thing2)
# thing = [1, 3]
# thing2 = {}
# print(thing + list(thing2.values()))


# soup = BeautifulSoup('<img>', features='html.parser')
# soup.img['src'] = f"media/{media_name}"
# cleaned_input[x].append(soup)

# # thing = 'some'
# # if thing != '':
# #     print(True)

# thing = {
#     "0": [
#         "index",
#         "index.html",
#         "2020/04/17 19:46",
#         "date_created"
#     ],
#     "1": [
#         "hello_v1",
#         "hello_v1.html",
#         "2020/04/17 19:46",
#         "date_created"
#     ],
#     "2": [
#         "hello_v2",
#         "hello_v2.html",
#         "2020/04/17 19:46",
#         "date_created"
#     ],
#     "3": [
#         "hello_v3",
#         "hello_v3.html",
#         "2020/04/17 19:46",
#         "date_created"
#     ],
#     "5": [
#         "hello_v5",
#         "Pudd2565O9KcSr0jHGWjzguY7FZJUo.html",
#         "2020/04/17 19:46",
#         "2020/04/15 20:46"
#     ],
#     "6": [
#         "hello_v4",
#         "z0FTLyrS9CiLk333J14oaCyB1hyQqR.html",
#         "2020/04/21 20:08",
#         "2020/04/21 20:08"
#     ]
# }

# dict_key = [x for x, y in thing.items() if y[1] == 'hello_v3.html']
# del dict_key


# thing = {x : y for x, y in thing.items() if y[1] != 'hello_v3.html'}
# print(thing)

# thing = {
#     0 : 'sdfg',
#     1 : 'sdfh',
#     2 : 'asdgf'
# }

# some = 0, 8, 6

# for x, y in {x : y for (x, y) in thing.items() if x not in some and x != 2}.items():
#     print(x)

# thing = {x: y for (x, y) in thing.items() if x == 4}
# if thing == {}:
#     print(True)
# print(thing)

