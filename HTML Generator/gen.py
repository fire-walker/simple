from __future__ import print_function, unicode_literals

import os
import time
import curses
import platform
import subprocess
from git import Repo
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt


# screen = curses.initscr()


style = style_from_dict({
    Token.QuestionMark: '#000',
    Token.Selected: '#535353',
    Token.Pointer: '#535353 bold',
    Token.Instruction: '#000',
    Token.Answer: '#535353',
    Token.Question: '#E47687',
})

questions = {
        'type': 'list',
        'name': 'item',
        'message': "What's your purpose?",
        'choices': ['Create Post', 'Edit Post', 'Commit Changes'],
        'filter': lambda val: val.lower()
}


while True:
    answers = prompt(questions, style=style)

    if answers['item'] == "create post":
        
        title = input("Enter the title name: ")

        print('Creating post...')

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
        file = open(os.path.join(__location__, '../index.html'), 'r+')
        soup = BeautifulSoup(file, features="html.parser")
        
        #find the most recent identifier number
        tag = soup.find_all('article')
        num = int(tag[0]['class'][0]) + 1

        body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

        # create the h1 tag  and delete it from the list
        header = BeautifulSoup(line[0], features='html.parser')
        header.string.wrap(header.new_tag('h1'))
        body.article.append(header)

        # tag the paragraph and read more and add them to the body
        x = 0
        for i in line[1].split():
            x += 1

        if x > 70:
            thing = ''
            parts = list(filter(None, line[1].split('.')))
            for i in parts:
                thing = (thing + i + '.')
                x = 0
                for i in thing.split():
                    x += 1
                if x > 70:
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


        # find the editing location of the source file
        tag = soup.find('div', {'class': 'wrapper'})
        tag.insert(0, body)

        # save the new edited source file
        file.write(str(soup))
        file.close





        # the seperate post
        body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

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
                if i.startswith('<-') and i.endswith('->'):
                    i = i.replace('->', '')
                    i = i.replace('<-', '')

                    soup = BeautifulSoup(i, features='html.parser')
                    tag = soup.new_tag('span')
                    tag['class'] = 'code-box3'
                    soup.string.wrap(tag)
                    box.p.append(soup)
                    box.p.append(' ')
                else:
                    soup = BeautifulSoup(i, features='html.parser')
                    box.p.append(soup)
                    box.p.append(' ')
            
            box.p.insert(0, BeautifulSoup("<span class='code-box2'>$ </span>", features='html.parser'))
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

        time.sleep(2)
        print("New post successfully created and appended")
        time.sleep(2)
        # screen.clear()



    
    if answers['item'] == "edit post":
        # location of the parent folder
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
        
        # filter .html files
        places = [f for f in os.listdir(__location__) if os.path.isfile(os.path.join(__location__, f)) and f.endswith('.html') and not f.startswith('index')]
         
        questions2 = {
            'type': 'list',
            'name': 'item',
            'message': 'Which post?',
            'choices': places,
        }

        # ask about which post
        answers = prompt(questions2, style=style)
        answer = answers['item']

        # read the selected file
        with open(os.path.join(__location__, answer), 'r') as file:
            body = BeautifulSoup(file, features='html.parser')

        #find the identifier tag
        tag = body.find_all('article')
        num = int(tag[0]['class'][0])

        # locate the wrapper and save it one a txt
        tag = body.find('div', {'class': 'wrapper'})
        with open(os.path.join(__location__, 'temp.txt'), 'w') as file:
            file.write(tag.prettify())

        # check platform and open txt file
        if platform == 'win32':
            loc = os.path.join(__location__, 'temp.txt')
            subprocess.run(["notepad", loc])
        else:
            import texteditor
            loc = os.path.join(__location__, 'temp.txt')
            texteditor.open(filename=loc)

        print("Updating post...")

        # read the temp with edited data
        with open(os.path.join(__location__, 'temp.txt'), 'r') as file:
            soup = BeautifulSoup(file.read(), features='html.parser')

        # replace old with new
        tag.replace_with(soup)
        os.remove(os.path.join(__location__, 'temp.txt'))

        # save the edited data
        with open(os.path.join(__location__, answer), 'w') as file:
            file.write(str(body))
        

        #updating the index file in congruence to the post
        updated_body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

        #add the new header
        header = BeautifulSoup("<h1></h1>", features="html.parser")
        header.h1.append(tag.h1.string)
        updated_body.article.append(header)

        #grab all the new paras
        all_paragraphs = tag.find_all('p', {'class': 'article-p'})

        #add the updated paragraphs
        x = 0
        for i in all_paragraphs[0].string.split():
            x += 1

        if x > 70:
            paragraph = ''
            updated_paragraph = BeautifulSoup('<p></p>', features='html.parser')
            sentenses = list(filter(None, all_paragraphs[0].string.split('.')))
            for i in sentenses:
                paragraph = (paragraph + i + '.')
                x = 0
                for i in paragraph.split():
                    x += 1
                if x > 70:
                    break

            updated_paragraph.p.append(paragraph)
            updated_paragraph.p.append(BeautifulSoup(f"<a href='{answer}.html' class='read'> Read more...</a>", features='html.parser'))
            updated_body.article.append(updated_paragraph)

        else:
            updated_paragraph = BeautifulSoup('<p></p>', features='html.parser')
            updated_paragraph.p.append(all_paragraphs[0].string)
            updated_paragraph.p.append(BeautifulSoup(f"<a href='{answer}' class='read'> Read more...</a>", features='html.parser'))
            updated_body.article.append(updated_paragraph)



        #open up the index file for modifications
        with open(os.path.join(__location__, 'index.html'), 'r') as file:
            index_whole = BeautifulSoup(file, features="html.parser")

        #find and kill the outdated reference
        filtered_index = index_whole.find('article', class_=num)
        filtered_index.decompose()

        #add the modifications to the whole file
        wrapper = index_whole.find('div', {'class': 'wrapper'})
        post_after = wrapper.find('article', class_=f'{num - 1}')
        post_after.insert_before(updated_body)


        #save the modifications
        with open(os.path.join(__location__, 'index.html'), 'w') as file:
            file.write(str(index_whole))


        time.sleep(2)
        print("Successfully edited post and index file.")
        time.sleep(1)








    if answers['item'] == 'commit changes':
        print('Committing...')
        __location__ = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__)))))
        os.chdir(__location__)
        now = datetime.now()
        time = now.strftime("%Y/%m/%d, %H:%M:%S")


        repo_dir = r'just-write.github.io'

        repo = Repo(repo_dir)

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))


        base_files = (file for file in os.listdir(__location__) if os.path.isfile(os.path.join(__location__, file)))
        temp_child = (file for file in os.listdir(os.path.join(__location__, r'HTML Generator')) if os.path.isfile(os.path.join(os.path.join(__location__, r'HTML Generator'), file)))
        
        children = []
        for i in temp_child:
            i = os.path.join(r'HTML Generator', i)
            children.append(i)

        files = children + list(base_files)

        commit_message = time
        repo.index.add(files)
        repo.index.commit(time)
        origin = repo.remote('origin')
        origin.push()
        print("Successfully pushed to Origin")
        
