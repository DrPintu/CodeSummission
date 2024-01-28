import requests 
import sys

# Website 1 : "https://sitare.org"

# Website 2 : 'https://github.com/'

# Website 3 : "https://www.vidyagyan.in/" 



 
url = sys.argv[1]  # Taking Website from command line

r= requests.get(url)
html_content = r.content

def get_title():
    start_pos = 0
    end_pos = 0
            
    for i in range(len(r.text)):
        if r.text[i:i+7] == '<title>':
            start_pos = i + 7
        elif r.text[i:i+8] == '</title>':
            end_pos = i
            break
    
    if start_pos is not None and end_pos is not None:
        title = r.text[start_pos:end_pos].strip()
        return title
    

def remove_tags(body):
    start = None
    main_txt = body
    new_txt = ''
    for i in range(len(body)):
        if body[i] == "<":
            start = i
        elif body[i] == ">":
            result = body[start:i+1]
            main_txt = main_txt.replace(result, "").strip()
    main_txt = main_txt.split("\n")
    for i in main_txt:
        if i.strip() == "":
            continue
        else:
            new_txt = new_txt +"\n"+ i.strip()
    return new_txt 
           
        

def url_tags(body):
    start = None
    main_txt = body.split()
    for i in main_txt:
        if i.find("https") != -1:
            start = i.find('="')
            if i.find('"') != -1 :
                end = i.find('"', start+2)
                result = i[start+2: end]
                print(result)
        else:
            continue


title = get_title()
print('\n')
print("Website Tittle : ", title)
print('\n')
print('\n')



body = remove_tags(r.text)
print(body)
print('\n')


my_url_list = url_tags(r.text)
print(my_url_list)



