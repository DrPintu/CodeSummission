import requests
import sys

#Function for Fetching the title from url's content
def title_fetch(content):
    start_index = content.find("<title>")+7
    end_index = content.find('</title>')
    result = content[start_index:end_index]
    return result

# Function for fetching Body's content only text from url's content
def body_fetch(content):
    start_index = content.find('<body')
    end_index = content.find('/body>')+6
    content = content[start_index:end_index]
    
    while '<script' in content:
        start_index = content.find('<script')
        end_index = content.find('/script>')+8
        content = (content[:start_index] + content[end_index:])
    while '<style' in content:
        start_index = content.find('<style')
        end_index = content.find('/style>')+7
        content = (content[:start_index] + content[end_index:])
        

    data = []

    while '<' in content:
        start_index = content.find('<')
        end_index = content.find('>')+1

        if content[start_index: start_index+2] == '<p':
            ps = content.find('<p')
            pe = content.find('/p>')+3
            sub_content = content[ps:pe]
            content = content[pe:]
            data.append(body_helper(sub_content))
        elif content[start_index: start_index+3] == '<li':
            lis = content.find('<li')
            lie = content.find('/li>')+4
            sub_content = content[lis:lie]
            content = content[lie:]
            data.append(body_helper(sub_content))
        else:
            result = content[:start_index].strip()
            content = content[end_index:]
            if len(result) >1:
                data.append(result)
    return data


def body_helper(content):

    result = ""
    while '<' in content:
        s_ind = content.find('<')
        e_ind = content.find('>')+1
        if len(content[:s_ind].strip()) > 1:
            result += content[:s_ind].strip()+" "
        content = content[e_ind:]
    return result.strip()



# Function for fetching urls from anchor tag
def link_fetch(content):
    links = []
    while '/a>' in content:
        start_index = content.find('<a')
        end_index = content.find('/a>')+3
        result = content[start_index+1 : end_index]

        s_index = result.find("http")
        e_index = result.find("\"", s_index)
        result = result[s_index:e_index]
        if len(result.strip()) != 0:
            links.append(result)
        content = content[end_index:]
    return links


def PrintBodyContent(content):
    content = body_fetch(content)
    result = []
    for i in content:
        while '&#' in i:
            s = i.find('&#')
            e = i.find(';', s)
            i = i[:s] + " "+i[e]
        if i[0:2] in [' ,', ' .', ' ;', " '", ";", ". ", ", ", ": "]:
            i = i[2:]
        if len(i) > 1 or i.isalnum():
            result.append(i)
    return result


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response = response.text.lower()
        fileobj = open("Craling.txt", 'w+')
        fileobj.write("Title of the website is :-    "+'\n'+'\t'+title_fetch(response)+'\n'+'\n'+'\n')
        fileobj.write("Body's content of the website is :-  "+'\n'+'\n')
        for i in PrintBodyContent(response):
            fileobj.write(i+'\n')
        fileobj.write('\n'+"Links in the website for changing the page of website:-   "+'\n'+'\n'+'\t')
        for j in link_fetch(response):
            fileobj.write(j+'\n')
    except:
        print("Enable to find response. Facing some problem")