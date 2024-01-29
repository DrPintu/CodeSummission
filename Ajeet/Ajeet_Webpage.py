import requests
import sys
from urllib.parse import urlparse, urljoin

def get_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            start = data.find("<title")
            end = data.find("</title>")
            value = [data[i] for i in range(start + 7, end)]
            return ''.join(value)
        else:
            print("Error: ", response.status_code)

    except Exception as e:
        print("Error: ", e)

def clean(data):
    start = data.find("<body")
    end = data.find("</body>")
    value = []
    current = start + 5
    last = False

    while current < end:
        if data[current] == '<':
            while data[current] != '>':
                current += 1
        else:
            if data[current].isspace() and not last:
                value.append(' ')
                last = True
            elif not data[current].isspace():
                value.append(data[current])
                last = False
        current += 1

    return ''.join(value)

def get_body(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            return clean(data)
        else:
            print("Error: ", response.status_code)

    except Exception as e:
        print("Error: ", e)

def get_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            start = "https://"
            value = []
            index = data.find(start)
            
            while index != -1:
                next_space = data.find('"', index)
                link = data[index:next_space]
                value.append(link)
                index = data.find(start, next_space)

            return value

        else:
            print("Error: ", response.status_code)

    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    URL = sys.argv[1]

    # Check if the URL has a scheme (http or https), if not, add http as the default
    parsed_url = urlparse(URL)
    if not parsed_url.scheme:
        URL = urljoin('http://', URL)

    title = get_title(URL)
    body = get_body(URL)
    links = get_links(URL)

    print("Title: ", title, "\n")
    print("Body: ", body)
    if links:
        print("Extracted links are:")
        for link in links:
            print(link)
    else:
        print("No links extracted.")
