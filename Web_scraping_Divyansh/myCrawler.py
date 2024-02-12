"""
Submitted by: Divyansh Mishra
Completion date: 10/02/2024
"""

import requests

def crawl(url):
    '''
    Returns the list of all the links preent in the html content given
    
    Parameter_url: The URL for the web to be crawled.
    Precondition: Should be in string and well defined (i.e. valid url)
    '''
    
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        print()
        _print_title(html)
        
        print()
        _print_content(html)

        print()
        links = _print_link(html)
        print("All the link contained in the page are: ")
        print()
        for i in links:
            print(i)
    else:
        print()
        print("!OOPS! We don't have access to the link porvided.")

def _find_content(tag, html_content):
    """
    Retruns the content between the given tag of the html_content

    Parameter_tag: The tag to be searched between
    Precondition: It should be of string type

    Parameter_html_content: The content in which we have to search
    Precondition: Type is string
    """

    assert type(tag) == str, repr(tag) + "is not a string, please provide a string"
    assert type(html_content) == str, "Html content should be provided in the string formate"

    start_tag = f'<{tag}'
    end_tag = f'</{tag}>'

    start = html_content.find(start_tag)
    end = html_content.find(end_tag)

    content = None
    if start != -1 and end != -1:
        content = html_content[start + len(start_tag):end]

        # Manually remove script tags
        script_start = content.find('<script')
        while script_start != -1:
            script_end = content.find('</script>', script_start)
            if script_end != -1:
                content = content[:script_start] + content[script_end + len('</script>'):]
            script_start = content.find('<script', script_start)

    return content

def _remove_tags(content):
    """
    Returne the given string after removing most of the html content
    
    Assumption: The content is not containing any < or > symbols.

    Parameter_content: The content to be proccessed
    Precondition: Type is string
    """
    assert (len(content)>=0), "The content is not present in the file."
    result = ''
    is_tag = False
    
    for i in range(len(content)):

        if content[i] == '<':
            is_tag = True

        elif content[i] == '>':
            is_tag = False
            continue
        
        elif not is_tag:
            if (i>1) and content[i-1] == " " and content[i] == " ":
                continue
            elif True:
                result += content[i]

    return result

def _print_title(html):
    '''
    Returns the title of the html content given
    
    Parameter_html: The text to be processed
    Precondition: Type should be string.
    '''
    
    content = _find_content('title', html)
    print("Title of the given URL is: \n", content)

def _print_content(html):
    '''
    Returns the content present in the body tag of the html content provided
    
    Parameter_html: The text to be processed
    Precondition: Type should be string.
    '''
    
    content = _find_content('body', html)
    tag_free = _remove_tags(content)
    blank_free = _remove_line_breaks(tag_free)
    print("The content found on the page is: \n",blank_free)

def _print_link(html):
    '''
    Returns the list of all the links present in the html content given
    
    Parameter_html: The text to be processed
    Precondition: Type should be string.
    '''
    # Extract all links on the page
    links = []

    # Find all occurrences of 'href=' and extract the URL
    start_index = 0
    while True:
        start_index = html.find('href="', start_index)
        if start_index == -1:
            break
        end_index = html.find('"', start_index + 6)
        if end_index == -1:
            break
        links.append(html[start_index + 6:end_index])
        start_index = end_index

    return links

def _remove_line_breaks(input_text):
    '''
    Retruns the input text after removing all the uneccessary line breaks and white spaces

    Parameter_input_text: The text to be processed
    Precondition: Type should be string.
    '''
    lines = input_text.split('\n') 

    non_empty_lines = [line for line in lines if line.strip() != '']
    result_text = '\n'.join(non_empty_lines)

    return result_text

url = input("Please enter the URL to be crawled: \n")
crawl(url)