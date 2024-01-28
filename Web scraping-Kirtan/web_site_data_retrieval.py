import sys
import requests
import os
import time

def file_loader(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
        # print(response.text)
            with open('data.txt', 'w', encoding='utf-8') as f:
                f.write(response.text)
            # print(content)`
        else:
            print("Failed to fetch page. Status code:", response.status_code)
            return None

    except Exception as e:
        print("An error occurred:", e)
        return None
    

    with open('data.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    time.sleep(5)
    os.remove('data.txt')

    return data

def readingLines(file):
    flag = False
    spaceFlag = True
    text = ''

    scriptIndex = file.find('<script')
    endOfScript = file.find('</script>')

    while scriptIndex != -1:

        file = file[:scriptIndex] + file[endOfScript+8:]
        scriptIndex = file.find('<script')
        endOfScript = file.find('</script>')


    for i in file:
        if i == '<':
            flag = False

        if i == '>':
            flag = True

        elif flag:
            if i.isspace() and spaceFlag:
                text += i
                spaceFlag = False

            else:
                if not i.isspace():
                    text += i
                    spaceFlag = True
    return text

def linkfinder(file):

    linkIndex = file.find('https')
    endOfLink = file.find('"', linkIndex+1)
    for i in range(len(file)):

        if linkIndex == -1:
            break
        
        linkIndex = file.find('https', endOfLink + 1)
        endOfLink = file.find('"', linkIndex+1)

        link = file[linkIndex:endOfLink]
        print(link)


if __name__=="__main__":
    path = sys.argv[1]
    print(readingLines(file_loader(path)))
    linkfinder(file_loader(path))