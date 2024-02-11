import requests
import re
import html

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
    clean_text = re.sub(r'<style.*?>.*?<\/style>|<.*?>', '', text, flags=re.DOTALL)
    clean_text = html.unescape(clean_text)  # Decode HTML entities
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

def page_body(url, tag, exclude_link):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    tag_content = re.findall(f'<{tag}[^>]*>(.*?)<\/{tag}>', response.text, re.DOTALL | re.IGNORECASE)
    cleaned_content = []

    for content in tag_content:
        cleaned_text = removetags(content)

        cleaned_text = re.sub(exclude_link, '', cleaned_text)

        cleaned_content.append(cleaned_text)

    return cleaned_content

def main():
    # url = "https://en.wikipedia.org/wiki/Hanging_Stone"
    # url = "https://en.wikipedia.org/wiki/Main_Page"
    url = "https://docs.python.org/3/library/html.parser.html"
    
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'https://' + url

    title = page_title(url)
    links = page_links(url)

    if title is not None:
        print(f"\nPage Title for:\n{title}")

    tags_to_display = ['p', 'a', 'h[1-6]', 'span', 'img']
    exclude_link = re.escape('<a href="https://commons.wikimedia.org/wiki/Category:Hanging_stone_(Ergaki)" class="extiw" title="commons:Category:Hanging stone (Ergaki)" previewlistener="true"></a>')
    for tag in tags_to_display:
        tag_content = page_body(url, tag,exclude_link)
        if tag_content:
            for i, content in enumerate(tag_content, 1):
                print(f"{removetags(content).strip()}")

    if links:

        for i, link in enumerate(links, 1):
            print(f"{i}. {link}")

if __name__ == "__main__":
    main()
