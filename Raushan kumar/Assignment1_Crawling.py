import requests
import re

def page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None
    title_match = re.search(r'<title>(.*?)<\/title>', response.text, re.DOTALL | re.IGNORECASE)
    if title_match:
        title = title_match.group(1)
    else:
        title = "Title not found"
    return title.strip()


def removetags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def page_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

    links = re.findall(r'href=["\'](https?://[^"\']+)["\']', response.text)

    return links

def page_body(url, tag):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    tag_content = re.findall(f'<{tag}.*?>(.*?)<\/{tag}>', response.text, re.DOTALL | re.IGNORECASE)

    cleaned_content = [removetags(content) for content in tag_content]

    return cleaned_content

def main():
    url = "https://www.dakshana.org/"
    
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'https://' + url

    title = page_title(url)
    links = page_links(url)

    if title is not None:
        print(f"\nPage Title for {url}:\n{title}")

    tags_to_display = ['p', 'a', 'h[1-6]', 'span', 'img']

    for tag in tags_to_display:
        tag_content = page_body(url, tag)
        if tag_content:
            print(f"\nText from <{tag}> tag for {url}:\n")
            for i, content in enumerate(tag_content, 1):
                print(f"{content.strip()}")
        else:
            print(f"\nNo content found for <{tag}> tag on {url}")

    if links:
        print(f"\nLinks in {url}:")

        for i, link in enumerate(links, 1):
            print(f"{i}. {link}")

if __name__ == "__main__":
    main()
