import requests

def get_title_from_html(html_text):
    title_start_index = html_text.find("<title>") + 7
    title_end_index = html_text.find("</title>")
    return html_text[title_start_index:title_end_index] if title_start_index != -1 and title_end_index != -1 else None

def extract_body_content(html_text):
    body_start_index = html_text.find("<body")
    body_end_index = html_text.find("</body>")
    
    if body_start_index == -1 or body_end_index == -1:
        return ""

    # Find the start of the content within <body> tags
    content_start_index = html_text.find(">", body_start_index)
    if content_start_index == -1:
        return ""

    # Extract content until the end of </body> tags
    body_content = ""
    while content_start_index < body_end_index:
        content_end_index = html_text.find("<", content_start_index + 1)
        if content_end_index == -1:
            break

        content = html_text[content_start_index + 1:content_end_index].strip()

        # Exclude content containing "jQuery"
        if "jQuery" not in content:
            body_content += content + " "

        # Move the index to the next position
        content_start_index = html_text.find(">", content_end_index + 1)
        if content_start_index == -1:
            break

    # Remove extra spaces and unwanted characters
    cleaned_body_content = ' '.join(body_content.split())

    return cleaned_body_content.strip()

def extract_links(html_text):
    link_start_index = html_text.find("<a")
    links_lst = []

    while link_start_index != -1 and link_start_index < len(html_text):
        href_start_index = html_text.find("href=", link_start_index)
        
        if href_start_index == -1:
            break

        quote_start_index = html_text.find('"', href_start_index)
        quote_end_index = html_text.find('"', quote_start_index + 1)
        
        if quote_start_index != -1 and quote_end_index != -1:
            link = html_text[quote_start_index + 1:quote_end_index]
            links_lst.append(link)
        
        link_start_index = html_text.find("<a", quote_end_index)

    total_links = [link for link in links_lst if link.startswith("http")]
    return total_links


# Taking input of URL from the user
url = input("Enter URL: ")

# Fetching HTML code of the URL
html_text = requests.get(url).text

# Extracting and printing the title
title = get_title_from_html(html_text)
print(f"\nTitle of the site {url} is: {title}\n")

# Extracting and printing the body content
body_content = extract_body_content(html_text)
print("Body content:", body_content.strip())
print("\n")

# Extracting and printing the actual links
all_links = extract_links(html_text)
print("All links:", all_links)
