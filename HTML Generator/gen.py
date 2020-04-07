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
    'choices': ['Create Post', 'Edit Post', 'Delete Post'],
    'filter': lambda val: val.lower()
}

# function to create and edit the seperate post file
def seperate_post(filename, num, title):
        if title.endswith('.html'):
            title = title.replace('.html', '')
        
        # find and read the file
        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(__location__, filename), 'r') as file:
            input_data = file.readlines()
            
        # clean the input data
        line = []
        for i in input_data:
            line.append(i.replace('\n', '').strip())

        cleaned_input = list(filter(None, line))
        
        body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

        # create the whole code box
        code = {}
        code2 = {}
        x = 0
        for i in cleaned_input:
            if i.startswith('<-') and i.endswith('->'):
                i = i.replace('<-', '')
                i = i.replace('->', '')
                code[x] = i
            x += 1

        for x, y in code.items():
            words = y.split(' ')
            box = BeautifulSoup("<p class='code-box'></p>",
                                features='html.parser')

            for i in words:
                i = "".join(i.split())
                if i.startswith('`') and i.endswith('`'):
                    i = i.replace('`', '')

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

            box.p.insert(0, BeautifulSoup(
                "<span class='code-box2'>$ </span>", features='html.parser'))
            code2[x] = box

        # delete the codebox lines from the list
        t = list(code2.keys())
        for i in sorted(t, reverse=True):
            del cleaned_input[i]

        # create the h1 tag with the class and delete it
        header = BeautifulSoup(cleaned_input[0], features='html.parser')
        tag = header.new_tag('h1')
        tag['class'] = 'article-h1'
        header.string.wrap(tag)
        body.article.append(header)

        # tag the remaining paragraphs and do the inner formatting
        for i in cleaned_input[1:]:
            seperated = i.split(' ')

            for i, j in enumerate(seperated):
                # links
                if j.startswith('<:') and j.endswith(':>'):
                    j = j.replace('<:', '')
                    j = j.replace(':>', '')
                    elements = j.split('--')

                    soup = BeautifulSoup('', features='html.parser')
                    tag = soup.new_tag('a', href=elements[1])
                    tag['class'] = 'link'
                    tag.string = elements[0]
                    soup.append(tag)
                    seperated[i] = str(soup)

                # code snippets
                elif j.startswith('<~') and j.endswith('~>'):
                    j = j.replace('<~', '')
                    j = j.replace('~>', '')

                    soup = BeautifulSoup('', features='html.parser')
                    tag = soup.new_tag('span')
                    tag['class'] = 'code-snippet'
                    tag.string = j
                    soup.append(tag)
                    seperated[i] = str(soup)

                # bold
                elif j.startswith('<**') and j.endswith('**>'):
                    j = j.replace('<**', '')
                    j = j.replace('**>', '')

                    soup = BeautifulSoup('', features='html.parser')
                    tag = soup.new_tag('b')
                    tag.string = j
                    soup.append(tag)
                    seperated[i] = str(soup)
                    
                # italic
                elif j.startswith('<*') and j.endswith('*>'):
                    j = j.replace('<*', '')
                    j = j.replace('*>', '')

                    soup = BeautifulSoup('', features='html.parser')
                    tag = soup.new_tag('i')
                    tag.string = j
                    soup.append(tag)
                    seperated[i] = str(soup)

            para = ' '.join(seperated)
            para = BeautifulSoup(para, features='html.parser')

            soup = BeautifulSoup('', features='html.parser')
            tag = soup.new_tag('p')
            tag['class'] = 'article-p'
            soup.append(tag)
            soup.p.append(para)
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

        return cleaned_input
    
# edit or insert to the index page
def index_post(title, custom_desc, cleaned_input, num):
    if title.endswith('.html'):
        title = title.replace('.html', '')
        
    # index file in congruence to the post
    body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

    # create the h1 tag  and delete it from the list
    header = BeautifulSoup(cleaned_input[0], features='html.parser')
    header.string.wrap(header.new_tag('h1'))
    body.article.append(header)


    # tag the paragraph and read more and add them to the body
    if custom_desc['item'].lower() == 'no':
        x = 0
        for i in cleaned_input[1].split():
            x += 1

        if x > 70:
            thing = ''
            parts = list(filter(None, cleaned_input[1].split('.')))
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
            soup.p.append(cleaned_input[1])
            soup.p.append(BeautifulSoup(
                f"<a href='{title.lower().replace(' ', '-')}.html' class='read'> Read more...</a>", features='html.parser'))
            body.article.append(soup)

    elif custom_desc['item'].lower() == 'yes':
        desc = BeautifulSoup(input('Enter description: '), features='html.parser')
        soup = BeautifulSoup('<p></p>', features='html.parser')
        soup.p.append(desc)
        soup.p.append(BeautifulSoup(f"<a href='{title.lower().replace(' ', '-')}.html' class='read'> Read more...</a>", features='html.parser'))
        body.article.append(soup)
        
    else:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
        with open(os.path.join(__location__, 'index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")
        
        tag = main_index.find('article', {'class': num})
        para = tag.p
        para.a['href'] = title.lower().replace(' ', '-')
        body.article.append(para)
        
    return body



while True:
    answers = prompt(questions, style=style)

    if answers['item'] == "create post":
        custom_desc = {
            'type': 'list',
            'name': 'item',
            'message': "Add custom description",
            'choices': ['No', 'Yes'],
            'filter': lambda val: val.lower()
        }
        
        title = input("Enter the title/file name: ")

        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))
            
        # custom description
        custom_desc = prompt(custom_desc, style=style)

        print('Creating post...')
            
        # the index file
        with open(os.path.join(__location__, '../index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")
        
        #find the most recent identifier number
        tag = main_index.find_all('article')
        num = int(tag[0]['class'][0]) + 1            
            
        cleaned_input = seperate_post('input.txt', num, title)
        body = index_post(title, custom_desc, cleaned_input, num)



        # find the editing location of the source file
        tag = main_index.find('div', {'class': 'wrapper'})
        tag.insert(0, body)

        # save the new edited source file
        with open(os.path.join(__location__, '../index.html'), 'w') as file:
            file.write(str(main_index))
            
        time.sleep(2)
        print("New post successfully created and appended to the index")
        time.sleep(2)



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
        
        custom_desc = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the index description",
            'choices': ['No', 'Yes', 'Keep Before'],
            'filter': lambda val: val.lower()
        }
        
        custom_title = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the page title",
            'choices': ['No', 'Yes'],
            'filter': lambda val: val.lower()
        }

        # questions
        answers = prompt(questions2, style=style)
        custom_title = prompt(custom_title, style=style)
        custom_desc = prompt(custom_desc, style=style)
        
        answer = answers['item']

        # read the selected file
        with open(os.path.join(__location__, answer), 'r') as file:
            body = BeautifulSoup(file, features='html.parser')

        #find the identifier tag
        tag = body.find_all('article')[0]
        num = int(tag['class'][0])

        #the whole list with the output data
        output = []

        #add the header to the out list
        h1 = ' '.join(tag.find('h1').string.split())
        output.append(h1)

        # add the paragraphs to the out list
        paragraphs = tag.find_all('p')
        for i in paragraphs:
            if i['class'][0] == 'article-p':
                if i.a is not None:
                    i.a.replace_with(f"<:{i.a.string}--{i.a['href']}:>")

                if i.span is not None:
                    i.span.replace_with(f"<~{i.span.string}~>")
                    
                p = ' '.join(i.get_text().split()) #to get rid of unnecessary white space
                output.append(p)

            else:
                box_checker = []
                code_box3 = i.find_all('span', {'class' : 'code-box3'})
                
                for j in code_box3:
                    box_checker.append(j.string)

                words = i.get_text('').split()
                for i,val in enumerate(words):
                    val = "".join(val.split())
                    if val == '$':
                        words.remove(val)
                        
                    elif val in box_checker:
                        words[i] = f'`{val}`'
                    
                    else:
                        words[i] = val
                
                out = ' '.join(words).strip()
                output.append(f'<-{out}->')

        # join the whole out list into a single variable
        output = '\n\n'.join(output)

        # open and write the temp file
        with open(os.path.join(__location__, 'temp.txt'), 'w') as file:
            file.write(output)

        # open the temp file for manual editing
        loc = os.path.join(__location__, 'temp.txt')
        subprocess.run(["notepad", loc])
        
        if custom_title['item'].lower() == 'yes':
            title = input("Enter title: ")
        else:
            title = answer

        # the heavy work
        cleaned_input = seperate_post('../temp.txt', num, title)
        body = index_post(title, custom_desc, cleaned_input, num)

        # delete the temp
        os.remove(os.path.join(__location__, 'temp.txt'))

        #open up the index file for modifications
        with open(os.path.join(__location__, 'index.html'), 'r') as file:
            index_whole = BeautifulSoup(file, features="html.parser")

        #find and kill the outdated reference
        filtered_index = index_whole.find('article', class_=num)
        index_desc = filtered_index.p
        filtered_index.decompose()

        #add the modifications to the whole file
        wrapper = index_whole.find('div', {'class': 'wrapper'})
        
        x = 1
        while True:
            post_after = wrapper.find('article', class_=f'{num - x}')
            post_before = wrapper.find('article', class_=f'{num + x}')
            
            if post_after is not None:
                post_after.insert_before(body)
                break
            elif post_before is not None:
                post_before.insert_after(body)
                break
            else:
                x += 1
        

        #save the modifications
        with open(os.path.join(__location__, 'index.html'), 'w') as file:
            file.write(str(index_whole))

        print("Updating post...")
        time.sleep(2)
        print("Successfully edited post and index file.")
        time.sleep(1)



    if answers['item'] == 'Delete Post':
        pass


# ===================goals===================
# -add the delete post func
# -add seperate filename and title name questions
# -add a method to edit the site name
# -add a method to edit the site description
# -when you edit or create the filename check it with the others
# - seperate option in choose edit file for the index
