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
# from datetime import datetime
# from git import Repo
# import os

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
# import curses

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


# import os
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
# # import os
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
# import os
# from bs4 import BeautifulSoup
# import subprocess





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
from bs4 import BeautifulSoup
import os

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
# for i in thing[1:]:
#     print(i)


i = "<p>some <a href='some'>thing</a> cool</p>"
soup = BeautifulSoup(i, features='html.parser')
    
thing = soup.find('article', class_=f'{1 + 5}')
print(thing)
    

# remember the keep before for the custom desc
while True:
    print('thing')
    while True:
        break