"""
This script is meant to parse the content of a website and extract content from it.

This script takes Command line argument while executing this give a link a website 
with http as command line argument.

Author: Sahil Kumar
Date: 10 January 2024
"""
import requests
import sys


def get_title(html_content):
    """Extracts the title of the website from the HTML content.
    
    Args:
        html_content (str): HTML content of the website.
        
    Returns:
        str: Title of the website.
    """
    try:
        start_index = html_content.find("<title>") + len("<title>")
        end_index = html_content.find("</title>")
        title = html_content[start_index:end_index].strip()
        return title
    except:
        return "Title is not found"


def get_body(html_content):
    """Extracts the body content of the website from the HTML content.
    
    Args:
        html_content (str): HTML content of the website.
        
    Returns:
        str: Body content of the website.
    """
    try:
        start_index = html_content.find("<body>") + len("<body>")
        end_index = html_content.find("</body>")
        body_html = html_content[start_index:end_index].strip()
        
        # Remove script tags and content
        start_index = body_html.find("<script")
        while start_index != -1:
            end_index = body_html.find("</script>", start_index)
            if end_index != -1:
                body_html = body_html[:start_index] + body_html[end_index + len("</script>"):]
            start_index = body_html.find("<script")
        
        # Remove style tags and content
        start_index = body_html.find("<style")
        while start_index != -1:
            end_index = body_html.find("</style>", start_index)
            if end_index != -1:
                body_html = body_html[:start_index] + body_html[end_index + len("</style>"):]
            start_index = body_html.find("<style")
        
        # Remove other HTML tags
        content_without_tags = ""
        tag_open = False
        for char in body_html:
            if char == '>':
                tag_open = True
            elif char == '<':
                tag_open = False
            elif tag_open:
                content_without_tags += char
        
        # Remove special characters and entities
        cleaned_content = ""
        for line in content_without_tags.split("\n"):
            if line.strip() != "&nbsp;":
                cleaned_content += "\n" + line.strip()
        
        # Try to remove any Wikipedia-specific content
        try:
            cleaned_content = cleaned_content[cleaned_content.index("From Wikipedia, the free encyclopedia"):]
        except:
            pass
        
        return cleaned_content
    except:
        return "body content not found!"


def get_urls(html_content):
    """Extracts all the URLs from the website HTML content.
    
    Args:
        html_content (str): HTML content of the website.
        
    Returns:
        list: List of URLs found in the website HTML content.
    """
    urls = []
    for line in html_content.split():
        if "http" in line or "www" in line:
            if '"' in line:
                url_start = line.find('="') + 2
                url_end = line.find('"', url_start)
                url = line[url_start:url_end]
            elif "'" in line:
                url_start = line.find("='") + 2
                url_end = line.find("'", url_start)
                url = line[url_start:url_end]
            else:
                start_url = line.find("http")
                url = line[start_url:].strip()
            if url.startswith(("http", "www")):
                urls.append(url)
    return list(set(urls))


def main():
    if len(sys.argv) != 2:
        print("Usage: python filename.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        content = requests.get(url=url).text
    except Exception as e:
        print("Failed to load the content. Please try again.")
        print("Error:", e)
        sys.exit(1)
    
    title = get_title(content)
    body = get_body(content)
    urls = get_urls(content)
    
    print("Title:\n", title.strip())
    print("\nBody:\n", body)
    print("\nURLs:\n")
    for url in urls:
        print(url)


if __name__ == "__main__":
    main()