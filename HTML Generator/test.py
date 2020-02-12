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
from bs4 import BeautifulSoup
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
#                 architecto unde omnis est natus voluptatibus reprehenderit molestiae quasi dignissimos error!
#             </p >
#         </article >

#         <hr / >
#         <h1 class = "hr-h1">the end</h1>
#     </div >
#     </div>
# """
# soup = BeautifulSoup(enter, features='html.parser')

# tag = soup.find('div', {'class': 'wrapper'})

# body = """ 
# <div class="wrapper">
#     <h1>Hello World</h1>
# </div>
# """

# body = BeautifulSoup(body, features='html.parser')
# tag.replace_with(body)
import os
# # print(soup)
# from bs4 import UnicodeDammit
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


# with open(os.path.join(__location__, 'temp.txt'), 'r', encoding='utf8') as file:
#     soup = BeautifulSoup(file, features='html.parser')


# print(str(soup))



# print(soup.decode("windows-1252"))
# print(soup.decode('utf8'))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


base_files = (file for file in os.listdir(__location__) if os.path.isfile(os.path.join(__location__, file)))

temp_child = (file for file in os.listdir(os.path.join(__location__, r'HTML Generator')) if os.path.isfile(os.path.join(os.path.join(__location__, r'HTML Generator'), file)))
children = []
for i in temp_child:
    i = os.path.join(r'HTML Generator', i)
    children.append(i)

files = children + list(base_files)
print(files)