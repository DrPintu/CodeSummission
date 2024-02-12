import requests

def get_title_from_html(html_text):
    title_start_index = html_text.find("<title>") + 7
    title_end_index = html_text.find("</title>")
    return html_text[title_start_index:title_end_index].strip() if title_start_index != -1 and title_end_index != -1 else None

def extract_body_content(html_text):
    start_index = html_text.find("<body>") + len("<body>")
    end_index = html_text.find("</body>")
    body_html = html_text[start_index:end_index].strip()

    # Removing all script tag and content
    start_ind = body_html.find("<script")
    while start_ind != -1:
        end_ind = body_html.find("</script>")
        body_html = body_html[:start_ind] + body_html[end_ind + 8:]
        start_ind = body_html.find("<script")

    # Removing all style tags and content
    start_ind = body_html.find("<style")
    while start_ind != -1:
        end_ind = body_html.find("</style>")
        body_html = body_html[:start_ind] + body_html[end_ind + 8:]
        start_ind = body_html.find("<style")

    content_without_tags = ""
    inside_tag = False
    index = 0
    while index < len(body_html):
        if body_html[index] == '>':
            inside_tag = True
        elif body_html[index] == '<':
            inside_tag = False
        elif inside_tag:
            content_without_tags += body_html[index]
        index += 1

    cleaned_content = ""
    previous_line = "-1"
    lines = content_without_tags.split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.strip() == "&nbsp;":
            index += 1
            continue
        if previous_line == "" and line.strip() == "":
            previous_line = line.strip()
            index += 1
            continue
        else:
            cleaned_content += "\n" + line.strip()
            previous_line = line.strip()
        index += 1

    # Replace HTML entities with their respective characters
    html_entities = {
        "&lt;": "<",
        "&gt;": ">",
        "&amp;": "&",
        "&quot;": '"',
        "&#39;": "'",
        "&nbsp;": " "
    }

    for entity, char in html_entities.items():
        cleaned_content = cleaned_content.replace(entity, char)

    return cleaned_content  # Return cleaned content instead of printing it

def extract_links(html_text):
    links = []
    index = 0
    while index != -1:
        # Find the next occurrence of 'href="'
        href_start = html_text.find('href="', index)
        if href_start == -1:
            break
        
        # Find the end of the URL
        url_start = href_start + len('href="')
        url_end = html_text.find('"', url_start)
        if url_end == -1:
            break
        
        # Extract the URL
        link = html_text[url_start:url_end]
        
        # Check if the extracted text starts with "http://" or "https://"
        if link.startswith("http://") or link.startswith("https://"):
            links.append(link)
        
        # Move the index to the end of the URL
        index = url_end
    
    return links

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
print("All links:")
for link in all_links:
    print(link)
