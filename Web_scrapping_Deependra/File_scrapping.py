import requests
import sys

URL = sys.argv[1]
# URL = "https://en.wikipedia.org/wiki/The_Garden_of_Words"

# URL = "https://sitare.org/univ/"

response = requests.get(URL)
data = response.text


def title(data):
    title_start = data.find('<title>')+7
    title_end = data.find('</title>')
    return data[title_start : title_end]

def body(data):
    data = data[data.find('<body'):data.find('</body>')]
    data = data_cleaning(data)
    body_content = ""
    tag_open = False
    for i in data:
        
        if i == "<":
            tag_open = True
        elif i == ">":
            tag_open = False
        elif not tag_open:
            body_content = body_content + i
    body_content = body_content.split()
    body = ''
    for i in body_content:
        body = body + " " + i

    return body


def links(data):
    link_from = 0
    while data.find('https', link_from) != -1:
        link_start = data.find('https', link_from)
        link_end = data.find('"', link_start)
        link_from = link_end
        print(data[link_start : link_end])


def data_cleaning(data):
    for i in range (data.count("<script")):
        data = data[:data.find('<script')] + data[data.find('</script')+9:]

    for i in range (data.count("<style")):
        data = data[:data.find('<style')] + data[data.find('</style')+8:]
    

    return (data)


print('\n')
print("Title :", title(data))

print("Body Content : ")
print(body(data))
print("\n", "All the Links Founds in the Page :")
links(data)