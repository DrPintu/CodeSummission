import requests
import sys
inp = sys.argv[1]

def htmlTag(url):
    html_tag = requests.get(url=url).text
    return html_tag

def parseTag(s):
    sub_str=""
    if ('<a' in s) and (".php" in s):
        start = s.index('href')
        end = s.index('>',start)
        print((inp + s[start+6:end-1]).strip(),end="")
    elif ('<a' in s) and ("img" not in s):
        start = s.index('href')
        end = s.index('>',start)
        print((s[start+6:end-1]).strip(),end="")
    elif ('<h' in s):
        start = s.index('>')
        end = s.index('<', start)
        end_str = s[end:]
        for j in range(len(end_str)):
            range=[]
            if end_str[j] == '<':
                range.append(j)
                end = end_str.index('>')
                range.append(end)
            elif range[0] <= j <= range[1]:
                sub_str+=""
            else:
                sub_str+=end_str[j]
    
    start = s.index('>')
    end = s.index('<', start)
    return s[start + 1:end] + sub_str

with open('output.txt', 'w') as file:
    file.write(htmlTag(inp))


with open('output.txt', 'r') as file:
    
    for line in file:
        try:
            print(parseTag(line).strip())
        
        except:
            continue
    
