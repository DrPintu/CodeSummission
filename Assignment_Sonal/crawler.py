"""
Run the script by executing the following command:
    python crawler.py <url>
Replace <url> with the URL of the webpage you want to crawl.
"""

import requests
import os
import sys

def crawl(url):
    """
    Fetches the HTML content of a given URL, saves it to a file, processes the content to extract text and links,
    and then prints the extracted text and links.

    Parameters:
        url (str): The URL of the webpage to crawl.
    """
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Save HTML content to a file
            with open("crawing.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
        else:
            print("Failed to fetch page. Status code:", response.status_code)
            return 
    except Exception as e:
        print("An error occurred:", e)
        return
    
    # Read HTML content from the file
    with open("crawing.txt", "r", encoding = "utf-8") as f:
        content = f.read()

    # Remove the temporary file
    os.remove("crawing.txt")
    
    # Initialize variables
    i = 0
    spaceFlag = True
    links = []

    text = ''
    # Process HTML content character by character
    while i < len(content):
        # Check for HTML tags
        if content[i] == "<":
            # Skip <script> tags and their content
            if content[i:i+7] == "<script":
                i = content.find("</", i+3) 
                continue
            # Skip <style> tags and their content
            if content[i:i+6] == "<style":
                i = content.find("</", i+3)
                continue
            # Process <a> tags to extract links
            if content[i+1] == 'a':
                link_index = content.find('href', i)
                if content[link_index + 6: link_index + 11] == 'https':
                    closing_index = content.find('"', link_index + 6)
                    links.append(content[link_index + 5: closing_index + 1])
            # Move to the next character after the HTML tag
            i = content.find('>',i+1)
        else:
            # Process text content
            if content[i].isspace() and spaceFlag:
                text += content[i]
                spaceFlag = False
            else:
                if not content[i].isspace():
                    text += content[i]
                    spaceFlag = True
        i += 1  

    # Print the extracted text
    print(text)
    # Print the extracted links
    for link in links:
        print(link)

if __name__=="__main__":
    # Get the URL from command-line arguments
    path = sys.argv[1]
    # Call the crawl function with the URL
    crawl(path)


if __name__=="__main__":
    path = sys.argv[1]
    crawl(path)