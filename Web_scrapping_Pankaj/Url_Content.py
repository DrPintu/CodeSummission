import requests as requests_lib
import sys

url_address = sys.argv[1]
response_data = requests_lib.get(url_address)       # Fetching text from the web.
web_content = response_data.text

# Defining container.
hyperlinks = []      # It will contain all anchor links.
# Defining check.
title_start_flag = False
script_start_flag = False
style_start_flag = False
# Defining accumulators.
title_content_text = ""
previous_character = ''
main_text = ''
element_start = ""

# Code to remove html tags.
for character in web_content:
    if character == '<':
        element_start += character
    # This elif block is responsible for removing all the html tags.
    elif element_start != "":
        if character == '>':
            element_start += '>'
            element_start = element_start.lower()
            # If the ending html tag is encountered.
            if '</' in element_start:
                if element_start == '</title>':
                    title_start_flag = False
                    print("Title: ", title_content_text)
                elif element_start == '</script>':
                    script_start_flag = False
                elif element_start == '</style>':
                    style_start_flag = False
                main_text += " "     # Adding the space after end tag to handle if no new line character is there.
            else:
                # handling if the start of the starting html tag is encountered.
                if '<a ' in element_start:
                    try:
                        link_index = element_start.find('"', element_start.index('href'))
                    except ValueError:
                        link_index = len(element_start) - 1
                    extracted_link = ''
                    for c in element_start[link_index + 1:]:     # Extracting links.
                        if c == '"':
                            break
                        else:
                            extracted_link += c
                    if extracted_link[0:4] == 'http':     # Handling if absolute url is encountered.
                        hyperlinks.append(extracted_link)
                    else:
                        if len(extracted_link) > 1 and extracted_link[0] == '/':
                            hyperlinks.append(url_address)
                        else:
                            hyperlinks.append(url_address + '/' + extracted_link)
                elif '<script' in element_start:
                    script_start_flag = True
                elif '<style' in element_start:
                    style_start_flag = True
                elif '<title' in element_start:
                    title_start_flag = True
            element_start = ""       # Making it empty if end tag is found
        else:
            element_start += character
    # Below code block in else deals with extracting main content from the page.
    else:
        if title_start_flag:
            title_content_text += character
        elif script_start_flag or style_start_flag:
            pass
        else:
            if not (previous_character == ' ' and character == ' '):      # removing extra spaces.
                if not character == '\t':        # Removing tabs.
                    main_text += character
    previous_character = character        # Keeping track of previous character.


def trim_text():
    if '\r\n' in main_text:
        extracted_text = main_text.split('\r\n')
    else:
        extracted_text = main_text.split('\n')
    for line in extracted_text:
            if not (line == '' or line == ' '):
                print(f"{line.strip()}")


trim_text()        # Trimming and printing content to terminal.


# Printing  all the url separately.
print("\n All the URLs that the page points/links to: \n ")
for url_link in hyperlinks:
    print(f"{url_link}")
