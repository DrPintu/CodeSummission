# importing required module
import requests

# Taking necessary inputs 
url = input("Enter the url:- ")

#html code of the url
text = requests.get(url = url).text


def title(text):
    title_index = text.find("<title>") + 7
    title_end_index = text.find("</title>")
    return text[title_index:title_end_index]


def body_content(text):
    body_content = ""
    i = text.find("<body")
    while i < text.find("</body>"):
        content_start_index = text.find(">",i)
        content_end_index = text.find("<",i+1)
        content = text[content_start_index+1:content_end_index].strip()
        if "{" not in content and content!=" " and "}" not in content:
            body_content+=content
        i+=(content_end_index-i)
        if i==-1:
            break
    list_body_content = body_content.split(" ")
    new_body_content = ""
    for i in list_body_content:
        new_body_content += (i+" ")
    return new_body_content


def links(text):
    actual_links = []
    start_link = text.find("<a")
    while start_link != -1:
        start_href = text.find('href="', start_link)
        end_href = text.find('"', start_href + 6)
        link = text[start_href + 6:end_href]
        if link.startswith("http"):
            actual_links.append(link)
        start_link = text.find("<a", end_href)
    return actual_links

print("Title of the page is ",title(text))
print("\n")
print("body_content",body_content(text))
print("\n")
print("links",links(text))