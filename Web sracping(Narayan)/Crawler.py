"""
This module is designed to parse html and extract content from it.

The code blocks and functions are implemented assuming that html pages are
well written in html. Some weird cases will be handled. All links that page points
to are printed separately at the end.

Author: Narayan Jat
Date: 11 January 2024
"""

# Importing required module.
import requests as r

url = input("Hey enter url and see content: ")
# Getting text from the web.
response = r.get(url)
content = response.text

# Defining container.
links = []      # Contains all anchor links.
# Defining flags.
title_start = False
script_start = False
style_start = False
# Defining accumulators.
title_content = ""
previous_char = ''
text = ''
start_of_element = ""

# Code to remove html tags.
for char in content:
    if char == '<':
        start_of_element += char
    # This elif block is responsible for removing all the html tags.
    elif start_of_element != "":
        if char == '>':
            start_of_element += '>'
            start_of_element = start_of_element.lower()
            # If the ending html tag is encountered.
            if '</' in start_of_element:
                if start_of_element == '</title>':
                    title_start = False
                    print("Title: ", title_content)
                elif start_of_element == '</script>':
                    script_start = False
                elif start_of_element == '</style>':
                    style_start = False
            else:
                # handling if the start of the starting html tag is encountered.
                if '<a ' in start_of_element:
                    try:
                        link_index = start_of_element.find('"', start_of_element.index('href'))
                    except ValueError:
                        link_index = len(start_of_element) - 1
                    link = ''
                    for c in start_of_element[link_index + 1:]:     # Extracting links.
                        if c == '"':
                            break
                        else:
                            link += c
                    if link[0:4] == 'http':     # Handling if absolute url is encountered.
                        links.append(link)
                    else:
                        if len(link) > 1 and link[0] == '/':
                            links.append(url)
                        else:
                            links.append(url + '/' + link)
                elif '<script' in start_of_element:
                    script_start = True
                elif '<style' in start_of_element:
                    style_start = True
                elif '<title' in start_of_element:
                    title_start = True
            start_of_element = ""       # Making it empty if end tag is found
        else:
            start_of_element += char
    # Below code block in else deals with extracting main content from the page.
    else:
        if title_start:
            title_content += char
        elif script_start or style_start:
            pass
        else:
            if not (previous_char == ' ' and char == ' '):      # removing extra spaces.
                if not char == '\t':        # Removing tabs.
                    text += char
    previous_char = char        # Keeping track of previous character.


def trim_lines():
    if '\r\n' in text:
        t = text.split('\r\n')
    else:
        t = text.split('\n')
    for j in t:
        if not (j == '' or j == ' '):
            print(f"{j.lstrip()}")


trim_lines()        # Trimming and printing content to terminal.

# Printing  all the url separately.
print("\n All the URLs that the page points/links to: \n ")
for i in links:
    print(f"{i}")
