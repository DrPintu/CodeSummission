import requests
import re

def get_html_content(url):
    # Fetch HTML content from the given URL
    response = requests.get(url)
    return response.text

def extract_title(html_content):
    # Extract and print the title of the webpage
    title_start = html_content.find("<title>") + len("<title>")
    title_end = html_content.find("</title>")
    title = html_content[title_start:title_end].strip()
    return title

def extract_body(content):
    opn_tag = content.find("<body>") + len("<body>")
    clse_tag = content.find("</body>")
    html_body = content[opn_tag:clse_tag].strip()
    
    # Removing all script tag and content
    scpt_start_indx = html_body.find("<script")
    scpt_end_indx = html_body.find("</script>")
    while scpt_start_indx!=-1:
        html_body = html_body[:scpt_start_indx] + html_body[scpt_end_indx+8:]
        scpt_start_indx = html_body.find("<script")
        scpt_end_indx = html_body.find("</script>")
        
    # Removing all style tags and content
    scpt_start_indx = html_body.find("<style")
    scpt_end_indx = html_body.find("</style>")
    while scpt_start_indx!=-1:
        html_body = html_body[:scpt_start_indx] + html_body[scpt_end_indx+8:]
        scpt_start_indx = html_body.find("<style")
        scpt_end_indx = html_body.find("</style>")
    
    contentWithoutTags = ""
    var = False
    for char in html_body:
        if char=='>':
            var = True
        elif char=='<':
            var = False
        elif var:
            contentWithoutTags += char

    fresh_content = ""
    previous = "-1"
    for line in contentWithoutTags.split("\n"):
        if line.strip()=="&nbsp;":
            continue
        if previous=="" and line.strip()=="":
            previous = line.strip()
            continue
        else:
            fresh_content += "\n" + line.strip()
            previous = line.strip()
    fresh_content = re.sub(r'&#[^;]+;', '', fresh_content)
    try:
        fresh_content = fresh_content[fresh_content.index("From Wikipedia, the free encyclopedia"):]
    except:
        None
    return fresh_content

    
def extract_links(html_content):
    # Extract and print links in the webpage
    links = []
    start_index = 0

    while start_index < len(html_content):
        a = html_content.find("https://", start_index)
        if a == -1:
            break
        b = html_content[a:].find('"')
        links.append(html_content[a:a + b])
        start_index = a + b + 1

    for link in links:
        print(f"Link:opening_tag_index {link}")