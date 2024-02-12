import requests
import sys

def get_title(html_content):
    """
    Extracts and returns the title of the HTML document.

    Parameters:
    - html_content (str): The HTML content of the webpage.

    Returns:
    - str: The title of the webpage.
    """
    start_pos = None
    end_pos = None
            
    for i in range(len(html_content)):
        if html_content[i:i+7] == '<title>':
            start_pos = i + 7
        elif html_content[i:i+8] == '</title>':
            end_pos = i
            break
    
    if start_pos is not None and end_pos is not None:
        title = html_content[start_pos:end_pos].strip()
        return title

def remove_tags(body):
    """
    Removes HTML tags from the given body of HTML content.

    Parameters:
    - body (str): The HTML content.

    Returns:
    - str: The content with HTML tags removed.
    """
    start = None
    start_css = None
    start_js = None
    end_css = None
    end_js = None 
    main_txt = body
    new_txt = ''

    for i in range(len(body)):
        if body[i] == "<":
            if body[i:i+6] == "<style":
                start_css = i
            if body[i:i+7] == "<script":
                start_js = i
            else:
                start = i
        elif body[i] == ">":
            if body[i-7:i+1] == "</style>":
                end_css = i
                result = body[start_css:end_css+1]
                main_txt = main_txt.replace(result, "").strip()
            if body[i-8:i] == "</script":
                end_js = i
                result = body[start_js:end_js+1]
                main_txt = main_txt.replace(result, "").strip()
            else:
                result = body[start:i+1]
                main_txt = main_txt.replace(result, "").strip()

    main_txt = main_txt.split("\n")
    for i in main_txt:
        if i.strip() != "":
            new_txt += "\n" + i.strip()

    return new_txt 

def url_tags(body):
    """
    Extracts and prints URLs found in the given HTML content.

    Parameters:
    - body (str): The HTML content.

    Returns:
    - None
    """
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

# Main part of the script
if len(sys.argv) != 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
html_content = response.text

title = get_title(html_content)
print('\n')
print("Website Title: ", title)
print('\n')
print("Page Content:")
print("\n")
body_without_tags = remove_tags(html_content)
print(body_without_tags)
print('\n')
print("\n")
print("\n")
print("Page Links Are Given Below:")
print('\n')
url_tags(html_content)