from __future__ import print_function, unicode_literals

import os
import sys
import time
import json
import random
import string
import shutil
import hashlib
import subprocess
from halo import Halo
from bs4 import BeautifulSoup
from tabulate import tabulate
from tkinter import Tk, filedialog
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt

class Messages:
    def __init__(self):
        self.style = style_from_dict({
            Token.QuestionMark: '#000',
            Token.Selected: '#535353',
            Token.Pointer: '#535353 bold',
            Token.Instruction: '#000',
            Token.Answer: '#535353',
            Token.Question: '#E47687',
        })

        self.purpose = {
            'type': 'list',
            'name': 'item',
            'message': "What's your purpose?",
            'choices': ['Create Post', 'Edit Post', 'Delete Post', 'View Post Data'],
            'filter': lambda val: val.lower()
        }

        self.custom_desc_edit = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the index description",
            'choices': ['No', 'Yes', 'Keep Before'],
            'filter': lambda val: val.lower()
        }

        self.custom_title_edit = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the page title",
            'choices': ['No', 'Yes'],
            'filter': lambda val: val.lower()
        }

        self.custom_desc = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the index description",
            'choices': ['No', 'Yes'],
            'filter': lambda val: val.lower()
        }

        self.filename_edit = {
            'type': 'list',
            'name': 'item',
            'message': "Would you like to alter the page filename",
            'choices': ['No', 'Yes'],
            'filter': lambda val: val.lower()
        }

        self.index_edit = {
            'type': 'list',
            'name': 'item',
            'message': "What would you like to edit?",
            'choices': ['Site_header', 'Site_description', 'Index_page_title'],
            'filter': lambda val: val.lower()
        }




        self.custom_desc_input = {
            'type': 'input',
            'name': 'item',
            'message': "Enter description:",
            'validate': lambda i: len(i.split(' ')) > 10
        }

        self.custom_title_input = {
            'type': 'input',
            'name': 'item',
            'message': "Enter page title name:",
            'validate': lambda i: len(i) > 1
        }



        self.post_doubt_edit = {
            'type': 'confirm',
            'name': 'item',
            'message': "Are you sure to continue: [y/n]",
        }

message = Messages()

file_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
base_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(os.path.dirname(__file__))))

# video and image chooser
def tk_get_file_path():
    root = Tk()
    root.withdraw()
    
    file_path = root.tk.splitlist(filedialog.askopenfilenames(parent=root, title='Choose the file(s)'))
    if not file_path:
        print("Cancelled")
        sys.exit()

    try:
        for file in file_path:
            with open(file, 'r'):
                pass
    except IOError:
        print("Cancelled")
        sys.exit()

    return file_path

# function to create and edit the separate post file
def separate_post(input_file, post_class, title, filename):
    file_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(file_dir, input_file), 'r') as file:
        input_data = file.readlines()

    # clean the input data
    cleaned_output = list(filter(None, [f.replace('\n', '').strip() for f in input_data]))
    cleaned_input = {x : y for (x, y) in enumerate(cleaned_output)}

    non_para = [0]

    # code box
    code = {i: j for (i, j) in cleaned_input.items() if j.startswith('<-') and j.endswith('->')}
    code = {i: j.replace('<-', '').replace('->', '') for (i, j) in code.items()}
    
    # img and vid
    media = {i: j for (i, j) in cleaned_input.items() if j == '<media>'}    
    media_old = {i: j for (i, j) in cleaned_input.items() if j.startswith('<media--')}

    # code box creation
    if code != {}:
        for x, y in code.items():
            non_para.append(x)
            words = y.split(' ')
            box = BeautifulSoup("<p class='code-box'></p>", features='html.parser')

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

            box.p.insert(0, BeautifulSoup("<span class='code-box2'>$ </span>", features='html.parser'))
            cleaned_input[x] = box

    # media generation
    media_files = []
    # new
    if media != {}:
        for x, y in media.items():
            non_para.append(x)
            files = tk_get_file_path()
            cleaned_input[x] = []
            
            
            image_endings = ('.png', '.jpg', '.jpeg')
            for i in files:
                media_name = os.path.basename(i)
                media_files.append(media_name)
                shutil.copyfile(i, os.path.join(file_dir, f"../media/{media_name}"))
                
                if media_name.endswith(image_endings):
                    soup = BeautifulSoup('<p><img>', features='html.parser')
                    soup.p['class'] = 'article-img'
                    soup.img['src'] = f"media/{media_name}"
                    cleaned_input[x].append(soup)
                    
                else:
                    extension = os.path.splitext(media_name)[1].replace('.', '')
                    soup = BeautifulSoup("<p><video controls><source>", features='html.parser')
                    soup.p['class'] = 'article-vid'
                    soup.source['src'] = f"media/{media_name}"
                    soup.source['type'] = f'video/{extension}'
                    cleaned_input[x].append(soup)
    # old
    if media_old != {}:
        for x, y in media_old.items():
            non_para.append(x)
            files = y.split('--')[1].replace('>', '')
            media_files.append(files)

            image_endings = ('.png', '.jpg', '.jpeg')
            if files.endswith(image_endings):
                soup = BeautifulSoup('<p><img>', features='html.parser')
                soup.p['class'] = 'article-img'
                soup.img['src'] = f"media/{files}"
                cleaned_input[x] = soup

            else:
                extension = os.path.splitext(files)[1].replace('.', '')
                soup = BeautifulSoup("<p><video controls><source>", features='html.parser')
                soup.p['class'] = 'article-vid'
                soup.source['src'] = f"media/{files}"
                soup.source['type'] = f'video/{extension}'
                cleaned_input[x] = soup

    # create the h1 tag with the class and delete it
    header = BeautifulSoup(cleaned_input[0], features='html.parser')
    tag = header.new_tag('h1')
    tag['class'] = 'article-h1'
    header.string.wrap(tag)
    cleaned_input[0] = header

    # tag the remaining paragraphs and do the inner formatting
    thing = {x : y for (x, y) in cleaned_input.items() if x not in non_para}
    for x, y in thing.items():
        separated = y.split(' ')

        for i, j in enumerate(separated):

            # links
            if j.startswith('<:') and j.endswith(':>'):
                j = j.replace('<:', '').replace(':>', '')
                elements = j.split('--')

                soup = BeautifulSoup('', features='html.parser')
                tag = soup.new_tag('a', href=elements[1])
                tag['class'] = 'link'
                tag.string = elements[0]
                separated[i] = str(soup.append(tag))

            # code snippets
            elif j.startswith('<~') and j.endswith('~>'):
                j = j.replace('<~', '').replace('~>', '')

                soup = BeautifulSoup('', features='html.parser')
                tag = soup.new_tag('span')
                tag['class'] = 'code-snippet'
                tag.string = j
                separated[i] = str(soup.append(tag))

            # bold
            elif j.startswith('<**') and j.endswith('**>'):
                j = j.replace('<**', '').replace('**>', '')

                soup = BeautifulSoup('', features='html.parser')
                tag = soup.new_tag('b')
                tag.string = j
                separated[i] = str(soup.append(tag))

            # italic
            elif j.startswith('<*') and j.endswith('*>'):
                j = j.replace('<*', '').replace('*>', '')

                soup = BeautifulSoup('', features='html.parser')
                tag = soup.new_tag('i')
                tag.string = j
                separated[i] = str(soup.append(tag))

        soup = BeautifulSoup('', features='html.parser')
        para = BeautifulSoup(' '.join(separated), features='html.parser')
        tag = soup.new_tag('p')
        tag['class'] = 'article-p'
        soup.append(tag)
        soup.p.append(para)
        cleaned_input[x] = soup

    body = BeautifulSoup(f"<article class='{post_class}'></article>", features='html.parser')

    for x, y in cleaned_input.items():
        if type(y) == list:
            for i in y:
                body.article.append(i)
        else:
            body.article.append(y)
        
    # open the template source file
    with open(os.path.join(file_dir, '../assets/template.html'), 'r') as file:
        soup = BeautifulSoup(file, features="html.parser")

    # find the insertion location of the template
    tag = soup.find('div', {'class': 'wrapper'})
    tag.insert(0, body)

    # insert the title
    title_soup = BeautifulSoup(title, features='html.parser')
    tag = title_soup.new_tag('title')
    title_soup.string.wrap(tag)
    soup.head.insert(0, title_soup)

    # save the edited file
    with open(os.path.join(file_dir, '../{}' .format(filename)), 'w') as file:
        file.write(str(soup))
    
    return cleaned_output, media_files

# edit or insert to the index page
def index_post(custom_desc, cleaned_input, post_class, filename):
    base_dir = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(os.path.dirname(__file__))))

    # index file in congruence to the post
    body = BeautifulSoup(
        f"<article class='{post_class} index-article'></article>", features='html.parser')

    # create the h1 tag  and delete it from the list
    header = BeautifulSoup(cleaned_input[0], features='html.parser')
    header.string.wrap(header.new_tag('h1'))
    body.article.append(header)

    # tag the paragraph and read more and add them to the body
    if custom_desc == 'no':

        x = len(cleaned_input[1].split())

        if x > 50:
            thing = ''
            parts = list(filter(None, cleaned_input[1].split('.')))
            for i in parts:
                thing = (thing + i + '.')
                x = 0
                for i in thing.split():
                    x += 1
                if x > 50:
                    break
            soup = BeautifulSoup("<p class='index-p'></p>", features='html.parser')
            soup.p.append(thing)
            soup.p.append(BeautifulSoup(
                f"<a href='{filename}' class='read'> Read more...</a>", features='html.parser'))
            body.article.append(soup)

        else:
            soup = BeautifulSoup("<p class='index-p'></p>", features='html.parser')
            soup.p.append(cleaned_input[1])
            soup.p.append(BeautifulSoup(f"<a href='{filename}' class='read'> Read more...</a>", features='html.parser'))
            body.article.append(soup)

    elif custom_desc == 'keep before':
        with open(os.path.join(base_dir, 'index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")

        tag = main_index.find('article', {'class': post_class})
        para = tag.p
        para.a['href'] = filename
        body.article.append(para)

    else:
        desc = BeautifulSoup(custom_desc, features='html.parser')
        soup = BeautifulSoup("<p class='index-p'></p>", features='html.parser')
        soup.p.append(desc)
        soup.p.append(BeautifulSoup(
            f"<a href='{filename}' class='read'> Read more...</a>", features='html.parser'))
        body.article.append(soup)

    return body

# convert the html to input data
def post_structure(body):
    # find the identifier tag
    tag = body.find_all('article')[0]
    
    # the whole list with the output data
    output = []

    # add the header to the out list
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

            # to get rid of unnecessary white space
            p = ' '.join(i.get_text().split())
            output.append(p)

        elif i['class'][0] == 'code-box':
            box_checker = []
            code_box3 = i.find_all('span', {'class': 'code-box3'})

            for j in code_box3:
                box_checker.append(j.string)

            words = i.get_text('').split()
            for i, val in enumerate(words):
                val = "".join(val.split())
                if val == '$':
                    words.remove(val)

                elif val in box_checker:
                    words[i] = f'`{val}`'

                else:
                    words[i] = val

            out = ' '.join(words).strip()
            output.append(f'<-{out}->')
        
        elif i['class'][0] == 'article-vid':
            out = f"<media--{i.source['src'].split('/')[1]}>"
            output.append(out)
        
        elif i['class'][0] =='article-img':
            out = f"<media--{i.img['src'].split('/')[1]}>"
            output.append(out)

    # join the whole out list into a single variable
    output = '\n\n'.join(output)
    return output
            
while True:
    answers = prompt(message.purpose, style=message.style)

    with open(os.path.join(base_dir, 'assets/post_data.json'), "r") as file:
        post_data = json.load(file)
        post_data = {int(x): y for x, y in post_data.items()}

    if answers['item'] == "create post":
        title = prompt(message.custom_title_input, style=message.style)['item']

        custom_desc = prompt(message.custom_desc, style=message.style)
        if custom_desc['item'] == 'yes':
            custom_desc = prompt(message.custom_desc_input,
                                 style=message.style)['item']
        else:
            custom_desc = 'no'
            
        # the index file
        with open(os.path.join(base_dir, 'index.html'), 'r') as file:
            main_index = BeautifulSoup(file, features="html.parser")

        # find the newest post class
        post_class = max(post_data.keys())

        # generate filename
        filename = f"{''.join(random.choices(string.ascii_letters + string.digits, k=30))}.html"
        
        # the heavy work
        cleaned_input = separate_post('input.txt', post_class, title, filename)
        body = index_post(custom_desc, cleaned_input[0], post_class, filename)

        # update the json of the post creation
        post_data[post_class] = [title, filename, time.strftime('%Y/%m/%d %H:%M'), time.strftime('%Y/%m/%d %H:%M'), cleaned_input[1]]

        # find the editing location of the source file
        tag = main_index.find('div', {'class': 'wrapper'})
        tag.insert(0, body)

        # save the new edited source file
        with open(os.path.join(file_dir, '../index.html'), 'w') as file:
            file.write(str(main_index))
            
        spinner = Halo(text='Creating post...',spinner='pong', text_color='magenta')
        spinner.start()
        time.sleep(4)
        spinner.stop_and_persist(text="New post successfully created and appended to the index", symbol='✔ ')  # ✔

    if answers['item'] == "edit post":
        # filter files
        places = [y[0] for x, y in post_data.items()]

        post = {
            'type': 'list',
            'name': 'item',
            'message': 'Which post?',
            'choices': places,
        }

        # file selected
        answer = prompt(message.post, style=message.style)['item']
        chosen_file = [y[1] for x, y in post_data.items() if y[0] == answer][0]

        # read the selected file
        with open(os.path.join(base_dir, chosen_file), 'r') as file:
            body = BeautifulSoup(file, features='html.parser')

        # check if it's the index or a post that's being edited
        if chosen_file == 'index.html':
            function = prompt(message.index_edit, style=message.style)['item']
            
            if function == 'site_header':
                index_header_input_edit = {
                    'type': 'input',
                    'name': 'item',
                    'message': f"Current header:\n  '{body.body.header.h1.a.string}'\n  Enter new header:",
                    'validate': lambda i: len(i) > 2
                }
                header_string = prompt(message.index_header_input_edit, style=message.style)['item']
                body.body.header.h1.a.string = header_string

                # filter the posts for filenames
                places = [y[1] for x, y in post_data.items() if x != 0]

                # edit the posts
                for i in places:
                    file = open(os.path.join(base_dir, i), 'r')
                    post = BeautifulSoup(file, features='html.parser')
                    file.close()

                    post.body.header.h1.a.string = header_string

                    file = open(os.path.join(base_dir, i), 'w')
                    file.write(str(post))
                    file.close()

                    # update the json last edited time of the posts
                    dict_key = [x for x, y in post_data.items() if y[1] == i][0]
                    post_data[dict_key][2] = time.strftime('%Y/%m/%d %H:%M')
                    
                # edit the template file
                file = open(os.path.join(base_dir, 'assets/template.html'), 'r')
                post = BeautifulSoup(file, features='html.parser')
                file.close()

                post.body.header.h1.a.string = header_string

                file = open(os.path.join(base_dir, 'assets/template.html'), 'w')
                file.write(str(post))
                file.close()

            elif function == 'site_description':
                index_desc_input_edit = {
                    'type': 'input',
                    'name': 'item',
                    'message': f"Current description:\n  '{body.body.header.p.string}'\n  Enter new description:",
                    'validate': lambda i: len(i.split(' ')) > 3
                }
                body.body.header.p.string = prompt(message.index_desc_input_edit, style=message.style)['item']

            elif function == 'index_page_title':
                index_title_input_edit = {
                    'type': 'input',
                    'name': 'item',
                    'message': f"Current index title:\n  '{body.head.title.string}'\n  Enter new index page title:",
                    'validate': lambda i: len(i) > 2
                }
                title_string = prompt(message.index_title_input_edit, style=message.style)['item']
                body.head.title.string = title_string

            # save the modifications
            with open(os.path.join(base_dir, 'index.html'), 'w') as file:
                file.write(str(body))

            # update the json last edited time of index
            post_data[0][2] = time.strftime('%Y/%m/%d %H:%M')

            spinner = Halo(text='Updating Index...', spinner='pong', text_color='magenta')
            spinner.start()
            time.sleep(4)
            spinner.stop_and_persist(text="Successfully edited the index file and associations", symbol='✔ ')  # ✔

        else:
            post_class = [x for x, y in post_data.items() if y[0] == answer][0]
            
            with open(os.path.join(base_dir, 'index.html'), 'r') as file:
                index_file = BeautifulSoup(file, features='html.parser')
            
            # format the inputs
            custom_title = prompt(message.custom_title_edit, style=message.style)
            if custom_title['item'] == 'yes':
                custom_title_input_edit = {
                    'type': 'input',
                    'name': 'item',
                    'message': f"Current title name:\n  '{body.head.title.string}'\n  Enter new page title name:",
                    'validate': lambda i: len(i) > 2
                }
                title = prompt(message.custom_title_input_edit, style=message.style)['item']
            else:
                title = body.head.title.string

            custom_desc = prompt(message.custom_desc_edit, style=message.style)
            tag = index_file.find('article', class_=post_class)
            tag.p.a.decompose()
            if custom_desc['item'] == 'yes':
                custom_desc_input_edit = {
                    'type': 'input',
                    'name': 'item',
                    'message': f"Current index description:\n  '{' '.join(tag.p.string.split())}'\n  Enter new description:",
                    'validate': lambda i: len(i.split(' ')) > 10
                }
                custom_desc = prompt(message.custom_desc_input_edit, style=message.style)['item']
            else:
                custom_desc = custom_desc['item']

            # convert the html
            output = post_structure(body)
            
            # open and write the temp file
            with open(os.path.join(file_dir, 'temp'), 'w') as file:
                file.write(output)

            with open(os.path.join(file_dir, 'temp'), 'w') as file:
                output_b = file.read()
                output_hash_before = hashlib.sha3_512(output_b).hexdigest()  
                      
            while True:
                loc = os.path.join(file_dir, 'temp')

                with open(os.path.join(file_dir, 'temp'), 'rb') as file:
                    output_b = file.read()
                    output_hash = hashlib.sha3_512(output_b).hexdigest()
                    
                if output_hash == output_hash_before:
                    doubt = prompt(message.post_doubt_edit, style=message.style)['item']
                    if doubt is False:
                        continue
                    else:
                        break
                else:
                    break
                    
            # the heavy work
            cleaned_input = separate_post('temp', post_class, title, chosen_file)
            body = index_post(custom_desc, cleaned_input[0], post_class, chosen_file)

            # delete the temp
            os.remove(os.path.join(file_dir, 'temp'))

            # open up the index file for modifications
            with open(os.path.join(base_dir, 'index.html'), 'r') as file:
                index_whole = BeautifulSoup(file, features="html.parser")

            # find and kill the outdated reference
            filtered_index = index_whole.find('article', class_=post_class)
            filtered_index.decompose()

            # add the modifications to the whole file
            wrapper = index_whole.find('div', {'class': 'wrapper'})

            x = 1
            while True:
                post_after = wrapper.find('article', class_=f'{post_class - x}')
                post_before = wrapper.find('article', class_=f'{post_class + x}')

                if post_after is not None:
                    post_after.insert_before(body)
                    break
                elif post_before is not None:
                    post_before.insert_after(body)
                    break
                else:
                    x += 1

            # save the modifications
            with open(os.path.join(base_dir, 'index.html'), 'w') as file:
                file.write(str(index_whole))
            
            # update the json last edited time
            dict_key = [x for x, y in post_data.items() if y[0] == answer][0]
            
            prev_media = post_data[dict_key][4]
            post_data[dict_key][2] = time.strftime('%Y/%m/%d %H:%M')
            post_data[dict_key][4] = cleaned_input[1]

            # checking the media files and deleting if necessary
            for i in prev_media:
                if i not in cleaned_input[1]:
                    os.remove(os.path.join(base_dir, f'media/{i}'))
                    

            spinner = Halo(text='Editing post...', spinner='pong', text_color='magenta')
            spinner.start()
            time.sleep(4)
            spinner.stop_and_persist(text="Successfully edited post and index file", symbol='✔ ')  # ✔

    if answers['item'] == 'delete post':
        # filter the files
        places = [y[0] for x, y in post_data.items() if x != 0]

        post = {
            'type': 'list',
            'name': 'item',
            'message': 'Which post?',
            'choices': places,
        }

        # file selected
        answer = prompt(message.post, style=message.style)['item']
        post_num = [x for x, y in post_data.items() if y[0] == answer][0]

        # delete the file, images and info from json
        os.remove(os.path.join(base_dir, post_data[post_num][1]))
        
        for i in post_data[post_num][4]:
            os.remove(os.path.join(base_dir, f'media/{i}'))

        # read the index file
        with open(os.path.join(base_dir, 'index.html'), 'r') as file:
            body = BeautifulSoup(file, features='html.parser')

        # delete the index entry
        article = body.find('article', {'class': post_num})
        article.decompose()

        # save the modifications
        with open(os.path.join(base_dir, 'index.html'), 'w') as file:
            file.write(str(body))
            
        post_data = {x : y for x, y in post_data.items() if x != post_num}

        spinner = Halo(text='Deleting post...',spinner='pong', text_color='magenta')
        spinner.start()
        time.sleep(4)
        spinner.stop_and_persist(text="Successfully deleted the post and it's remnants", symbol='✔ ')  # ✔

    if answers['item'] == 'view post data':

        spinner = Halo(text='Tabulating data...', spinner='pong', text_color='magenta')
        spinner.start()
        time.sleep(4)
        spinner.stop()

        table = [[x, y[0], y[2], y[3], y[1]] for x, y in post_data.items()]

        headers = 'class', 'title', 'last_edited', 'date_created', 'filename'
        print(tabulate(table, headers, tablefmt="pretty"))


    print('='*50 + '\n\n')
    time.sleep(2)

    with open(os.path.join(base_dir, 'assets/post_data.json'), "w") as file:
        json.dump(post_data, file)


# ===================goals/problems===================
# make a site refresh thing, where the title, header and paras are kept but the template is updated
# error checking, checksums, title matches

# post_data = {post_num: [page_title, filename.html, last_edited, date_created, media_linked]}
 
