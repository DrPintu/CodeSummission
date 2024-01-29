import requests
import sys

def fetch_html_content(url):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            return response.text  # Return the HTML content
        else:
            print(f"Failed to fetch URL: {url}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

html_content = fetch_html_content(sys.argv[1])

def find_title(html_content):
    start = html_content.find("<title>")+len("<title>")
    end = html_content.find("</title>")
    title=""
    for i in range(start, end):
        title+=html_content[i]
    return title

def find_body(text):
    text = ' '.join(text.split())

    start = text.find("<body>")+len("<body>")
    end = text.find("</body>")
    body=""
    tag=False
    for i in range(start, end):
        if text[i] == "<":
            tag=True
        elif text[i] == ">":
            tag=False
        elif text[i] == " " and text[i+1]==" ":
            tag=False
        elif not tag:
            body+=text[i]
    return body

def listOfLinks(text):
    start = 0
    for i in range(text.count("http")):
        result = ""
        start = text.find("http", start+4)
        end = text.find("\"", start)
        for j in range(start, end):
            result +=text[j]
        print(result)

if html_content:
    print("Title of the given URL is: ", find_title(html_content), "\n")
    print("Body of the given URL is: ", find_body(html_content), "\n")
    listOfLinks(html_content)


