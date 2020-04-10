from __future__ import print_function, unicode_literals

import os
import time
import curses
import platform
import subprocess
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

purpose = {
    'type': 'list',
    'name': 'item',
    'message': "What's your purpose?",
    'choices': ['Create Post', 'Edit Post', 'Delete Post'],
    'filter': lambda val: val.lower()
}

custom_desc_edit = {
    'type': 'list',
    'name': 'item',
    'message': "Would you like to alter the index description",
    'choices': ['No', 'Yes', 'Keep Before'],
    'filter': lambda val: val.lower()
}

custom_title_edit = {
    'type': 'list',
    'name': 'item',
    'message': "Would you like to alter the page title",
    'choices': ['No', 'Yes'],
    'filter': lambda val: val.lower()
}

custom_desc = {
    'type': 'list',
    'name': 'item',
    'message': "Would you like to alter the index description",
    'choices': ['No', 'Yes'],
    'filter': lambda val: val.lower()
}

filename_edit = {
    'type': 'list',
    'name': 'item',
    'message': "Would you like to alter the page filename",
    'choices': ['No', 'Yes'],
    'filter': lambda val: val.lower()
}

index_edit = {
    'type': 'list',
    'name': 'item',
    'message': "What would you like to edit?",
    'choices': ['Site_header', 'Site_description', 'Index_page_title'],
    'filter': lambda val: val.lower()
}



# function to create and edit the seperate post file
def seperate_post(input_file, num, title, filename):
        
        # find and read the file
        location = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(location, input_file), 'r') as file:
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
        with open(os.path.join(location, '../template.html'), 'r') as file:
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
        with open(os.path.join(location, '../{}.html' .format(filename)), 'w') as file:
            file.write(str(soup))

        return cleaned_input
    
# edit or insert to the index page
def index_post(title, custom_desc, cleaned_input, num, filename):
        
    # index file in congruence to the post
    body = BeautifulSoup(f"<article class='{num}'></article>", features='html.parser')

    # create the h1 tag  and delete it from the list
    header = BeautifulSoup(cleaned_input[0], features='html.parser')
    header.string.wrap(header.new_tag('h1'))
    body.article.append(header)

    # tag the paragraph and read more and add them to the body
    if custom_desc == 'no':
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
                f"<a href='{filename}.html' class='read'> Read more...</a>", features='html.parser'))
            body.article.append(soup)

        else:
            soup = BeautifulSoup('<p></p>', features='html.parser')
            soup.p.append(cleaned_input[1])
            soup.p.append(BeautifulSoup(
                f"<a href='{filename}.html' class='read'> Read more...</a>", features='html.parser'))
            body.article.append(soup)

    elif custom_desc == 'before':
        location = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
        with open(os.path.join(location, 'index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")

        tag = main_index.find('article', {'class': num})
        para = tag.p
        para.a['href'] = filename
        body.article.append(para)
        
    else:
        desc = BeautifulSoup(custom_desc, features='html.parser')
        soup = BeautifulSoup('<p></p>', features='html.parser')
        soup.p.append(desc)
        soup.p.append(BeautifulSoup(f"<a href='{filename}.html' class='read'> Read more...</a>", features='html.parser'))
        body.article.append(soup)
        
    return body



while True:
    answers = prompt(purpose, style=style)

    if answers['item'] == "create post":   
        # inputs  
        title= input("Enter the page title name: ")
        filename = input("Enter page filename (w/o suffix): ")
        custom_desc = prompt(custom_desc, style=style)
        
        if custom_desc['item'] == 'yes':
            custom_desc = input('Enter the description: ')
        else:
            custom_desc = 'no'

        location = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))

        print('Creating post...')
            
        # the index file
        with open(os.path.join(location, '../index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")
        
        #find the most recent identifier number
        tag = main_index.find_all('article')
        num = int(tag[0]['class'][0]) + 1            
            
        # the heavy work
        cleaned_input = seperate_post('input.txt', num, title, filename)
        body = index_post(title, custom_desc, cleaned_input, num, filename)

        # find the editing location of the source file
        tag = main_index.find('div', {'class': 'wrapper'})
        tag.insert(0, body)

        # save the new edited source file
        with open(os.path.join(location, '../index.html'), 'w') as file:
            file.write(str(main_index))
            
        time.sleep(2)
        print("New post successfully created and appended to the index")
        time.sleep(2)



    if answers['item'] == "edit post":
        # location of the parent folder
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))
        
        # filter .html files
        places = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f)) and f.endswith('.html') and not f.startswith('template')]
         
        post = {
            'type': 'list',
            'name': 'item',
            'message': 'Which post?',
            'choices': places,
        }

        # file selected
        answers = prompt(post, style=style)
        answer = answers['item']
        
        # read the selected file
        with open(os.path.join(location, answer), 'r') as file:
            body = BeautifulSoup(file, features='html.parser')
        
        # check if it's the index or a post that's being edited
        if answer == 'index.html':
            # select what to edit
            function = prompt(index_edit, style=style)['item']
            
            # alterations
            if function == 'site_header':
                print(f'Current header: {body.body.header.h1.a.string}')
                header_string = input("Enter new header: ")
                body.body.header.h1.a.string = header_string
            
                files = [f for f in os.listdir(location) if f.endswith('.html') and not f.startswith('index')]
            
            
                for i in files:
                    file = open(os.path.join(location, i), 'r')
                    post = BeautifulSoup(file, features='html.parser')
                    file.close()
                    
                    post.body.header.h1.a.string = header_string
                    
                    file = open(os.path.join(location, i), 'w')
                    file.write(str(post))
                    file.close()
            
            elif function == 'site_description':
                print(f'Current description:\n{body.body.header.p.string}')
                desc_string = input("Enter new description:\n")
                body.body.header.p.string = desc_string
                
            elif function == 'index_page_title':
                print(f'Current index title: {body.head.title.string}') 
                title_string = input("Enter new index page title: ")
                body.head.title.string = title_string
                
                
            
            #save the modifications
            with open(os.path.join(location, 'index.html'), 'w') as file:
                file.write(str(body))
                
            print("Updating index...")
            time.sleep(2)
            print("Successfully edited the index file and associations.")
            time.sleep(1)
                
        
        else:
            # format the inputs
            custom_title = prompt(custom_title_edit, style=style)
            if custom_title['item'] == 'yes':
                title = input("Enter the page title name: ")
            else:
                custom_title = body.head.title.string
        
            custom_desc = prompt(custom_desc_edit, style=style)
            if custom_desc['item'] == 'yes':
                custom_desc = input('Enter the description: ')
            elif custom_desc['item'] == 'no':
                custom_desc = 'no'
            else:
                custom_desc = 'before'
                
            filename = prompt(filename_edit, style=style)
            if filename['item'] == 'yes':
                filename = input("Enter page filename (w/o suffix): ")
            else:
                filename = answer.replace('.html', '')
            


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
            with open(os.path.join(location, 'temp.txt'), 'w') as file:
                file.write(output)

            # open the temp file for manual editing
            loc = os.path.join(location, 'temp.txt')
            subprocess.run(["notepad", loc])

            # the heavy work
            cleaned_input = seperate_post('../temp.txt', num, title, filename)
            body = index_post(title, custom_desc, cleaned_input, num, filename)

            # delete the temp
            os.remove(os.path.join(location, 'temp.txt'))

            #open up the index file for modifications
            with open(os.path.join(location, 'index.html'), 'r') as file:
                index_whole = BeautifulSoup(file, features="html.parser")

            #find and kill the outdated reference
            filtered_index = index_whole.find('article', class_=num)
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
            with open(os.path.join(location, 'index.html'), 'w') as file:
                file.write(str(index_whole))

            print("Updating post...")
            time.sleep(2)
            print("Successfully edited post and index file.")
            time.sleep(1)



    if answers['item'] == 'Delete Post':
        pass


# ===================goals===================
# -add the delete post func
# -remove filename options from the user
# -make the filename a randomly generated static
# -display the choose file with the post header
