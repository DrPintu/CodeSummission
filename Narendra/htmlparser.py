import requests

#Taking input of url from user 
url = input()
url = url

#html code of the url
text = requests.get(url = url).text

title_index = text.find("<title>") + 7
title_end_index = text.find("</title>")
print('\n')
print(f"Title of the site {url} is: ",text[title_index:title_end_index])
print('\n')

body_content = ""

#start from the body tag
i = text.find("<body")

while i < text.find("</body>"):
    content_start_index = text.find(">",i)
    content_end_index = text.find("<",i+1)
    content = text[content_start_index+1:content_end_index]
    
    if "jQuery" in content:
        break
    body_content+=content
    i+=(content_end_index-i)
    if i==-1:
        break

list_body_content = body_content.split()
new_body_content = ""

for i in list_body_content:
    new_body_content += (i+" ")


    
i = text.find("<a")

all_links = []
while i < len(text):
    content_start_index = text.find("<a href=",i)
    content_end_index = text.find("</a>",i+1)
    content = text[content_start_index+1:content_end_index]
    all_links.append(content)
    i+=(content_end_index-i)
    if i==-1:
        break
    
actual_links = []
for i in all_links:
    index = i.find("http")
    space = i.find(" ",index)
    if i[index:space] =="":
        continue
    actual_links.append(i[index:space])
print("Body content: ",new_body_content)
print("\n")
print("actual_links:  ",actual_links)