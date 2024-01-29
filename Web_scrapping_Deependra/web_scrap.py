import requests
import sys

URL = sys.argv[1]

# URL = "https://sitare.org/univ/"
response = requests.get(URL)
data = response.text

# print(data[data.find('<body>'):data.find('People')+6])

def title(data):
    title_start = data.find('<title>')+7
    title_end = data.find('</title>')
    return data[title_start : title_end]



def body(text):
    start = None
    main_txt = text
    new_txt = ''
    for i in range(len(text)):
        if text[i] == "<":
            start = i
        elif text[i] == ">":
            result = text[start:i+1]
            main_txt = main_txt.replace(result, "").strip()
    main_txt = main_txt.split("\n")
    for i in main_txt:
        if i.strip() == "":
            continue
        else:
            new_txt = new_txt +"\n"+ i.strip()
    return new_txt


def links(data):
    link_from = 0
    while data.find('href=', link_from) != -1:
        link_start = data.find('href', link_from) + 6
        link_end = data.find('"', link_start)
        link_from = link_end
        print(data[link_start : link_end])


web_body = body(data)
print('\n')
print("Title :", title(data))

print("Body Content : ")
print(web_body)
print('\n')
print("\n", "All the Links Founds in the Page : ")
links(data)
