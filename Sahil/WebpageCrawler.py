"""
The general skeleton of a website

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website Title</title>
</head>

<body>

    <!-- Your content goes here -->

</body>

</html>
 

WHAT EACH FUNCTION IS DOING WRITTEN IN THE SRCIPT;

Title Extraction (get_title):

first sends an HTTP GET request to the specified URL.
then retrieves the raw HTML content from the response.
then it searches for the <title> tags in the HTML and extracts the text between them.
finally we are printing the extracted title.


Body Extraction (get_body):

first sends an HTTP GET request to the URL.
then retrieves the raw HTML content.
then it searches for the <body> tag to locate the start of the body content.
then extracting text between HTML tags within the body (tags are not included).
then prints the extracted text content.


Links Extraction (get_links):

first sends an HTTP GET request to the URL.
then retrieves the raw HTML content.
then searches for occurrences of URLs starting with "http" within the HTML content.
then appends the extracted links to a list(use as a accumulator).
then prints the extracted links.

"""

import requests
import sys

def get_title(url):
    #send a GET request to the URL and get the raw HTML content.
    response = requests.get(url) #sends an http get request
    raw_content = response.text  #extract the raw html content from the request
    
    #extract the title from the HTML content
    title_start = raw_content.find("<title>") + len("<title>")
    title_end = raw_content.find("</title>")
    title = raw_content[title_start:title_end]
    
    #print the extracted title
    print("Title:", title)

def get_body(url):
    #send a GET request to the URL and get the raw HTML content
    response = requests.get(url)
    html_content = response.text #all the content between html tag
    
    #extract text content from the body of the HTML
    texts = []
    start_index = html_content.find("<body") #finding the index from where body starts

    if start_index != -1:  #checks if body tag is found
        start_index = html_content.find(">", start_index) + 1

        while start_index != -1:
            end_index = html_content.find("<", start_index)
            
            if end_index != -1:
                #extract text between HTML tags and add to the texts list
                text = html_content[start_index:end_index].strip()
                if text:
                    texts.append(text)
                start_index = html_content.find(">", end_index) + 1
            else:
                break
    
    #print the extracted text content
    print("Body:")
    for t in texts:
        print(t, end=" ")

def get_links(url):
    #send a GET request to the URL and get the raw HTML content
    response = requests.get(url)
    raw_content = response.text

    #extract links from the HTML content
    body_raw_content = raw_content
    links = []
    while len(body_raw_content) > 1:
        start = body_raw_content.find("http")
        end = body_raw_content[start:].find('"')
        links.append(body_raw_content[start : start + end])
        body_raw_content = body_raw_content[start + end + 1:]

    #print the extracted links
    print("Links:")
    for link in links:
        print(link)

def main():
	if len(sys.argv) != 2:
		print("Usage: python WebpageCrawler.py <URL>")
		sys.exit(1)

	url=sys.argv[1]
	get_title(url)
	print("")
	print("")
	get_body(url)
	print("")
	print("")
	get_links(url)


if __name__ == "__main__":
    #execute the main function when the script is run
    main()