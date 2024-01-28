# importing the required module
import requests

def fetch_html_content(url):
    # Make an HTTP request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: Failed to retrieve content. Status code: {response.status_code}")
        return None
    

def extract_title(html_content):
    # Find the start and end indices of the title tag in the HTMclosing_tag
    opening_tag = html_content.find("<title>") + len("<title>")
    closing_tag = html_content.find("</title>")
    
    # Extract the title text if the title tag is found
    return html_content[opening_tag:closing_tag] if opening_tag != -1 and closing_tag != -1 else "Title not found"

def extract_texts(html_content):
    texts = []
    opening_tag_index = html_content.find("<body")
    
    # Check if the <body> tag is found in the HTML content
    if opening_tag_index != -1:
        opening_tag_index = html_content.find(">", opening_tag_index) + 1

        # Extract text between tags while traversing the HTML content
        while opening_tag_index != -1:
            closing_tag_index = html_content.find("<", opening_tag_index)

            if closing_tag_index != -1:
                text = html_content[opening_tag_index:closing_tag_index].strip()
                if text:
                    texts.append(text)
                opening_tag_index = html_content.find(">", closing_tag_index) + 1
            else:
                break

    # Return the extracted texts or a default message if no texts are found
    return texts if texts else ["Body not found"]

def extract_links(html_content):
    body_content = html_content
    links = []

    # Extract links by finding occurrences of "http" and adjacent double quotes
    while len(body_content) > 1:
        a = body_content.find("http")
        b = body_content[a:].find('"')
        links.append(body_content[a:a + b])
        body_content = body_content[a + b + 1:]

    return links

def main():
    # Prompt the user to enter a URL
    url = input("Enter your URL with https://: ")

    # Retrieve HTML content from the provided URL
    html_content = fetch_html_content(url)
    
    # Process and display information based on the retrieved HTML content
    if html_content is not None:
        print("Title:")
        print(extract_title(html_content))

        print("\nTexts:")
        for text in extract_texts(html_content):
            print(text)

        print("\nLinks:")
        for link in extract_links(html_content):
            print(link)
            

if __name__ == "__main__":
    main()
