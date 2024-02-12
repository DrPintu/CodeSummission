import requests

def print_page_title(url):
    
    # Send a GET request to the specified URL and store the response
    response = requests.get(url)
    
    # Extract the text content of the webpage from the response
    webpage_content = response.text
    
    # Find the start and end indices of the title tag in the webpage content
    title_begin = webpage_content.find("<title>") + len("<title>")
    title_finish = webpage_content.find("</title>")
    
    # Extract the title text from the webpage content using the start and end indices
    title = webpage_content[title_begin:title_finish]
    
    # Print the extracted title
    print(title)


def print_webpage_text(url):
    # This function prints the content of the body of a webpage.

    # Send a GET request to the specified URL and store the response
    response = requests.get(url)
    html_content = response.text
    
    # Initialize an empty list to store the extracted text
    texts = []
    
    # Find the start index of the body tag in the HTML content
    body_tag_index = html_content.find("<body")

    # If the body tag is found
    if body_tag_index != -1:
        # Find the start index of the first closing angle bracket '>' after the body tag
        tag_end = html_content.find(">", body_tag_index) + 1
        
        # Continue until no more text is found inside the body tag
        while tag_end != -1:
            # Find the end index of the next opening angle bracket '<' after the start index
            tag_start_next = html_content.find("<", tag_end)
            
            # If an opening angle bracket '<' is found
            if tag_start_next != -1:
                # Extract the text between the start and end indices and remove leading/trailing whitespace
                text = html_content[tag_end:tag_start_next].strip()
                
                # If the extracted text is not empty, add it to the list of texts
                if text:
                    texts.append(text)
                
                # Find the start index of the next closing angle bracket '>' after the end index
                tag_end = html_content.find(">", tag_start_next) + 1
            else:
                break

    # Filtering the texts based on certain criteria using list comprehension
    filtered_texts = [text for text in texts if text[0] not in ['.', ',','', ' ', '(', ')', '[', ']', '{', '}', '@', "'", '&', '#', '^'] and text[0:3] not in ['-->', 'htt', 'jQu']]

    # Joining the filtered texts into a single string
    result = ' '.join(filtered_texts)

    # Printing the result
    print(result)


def print_webpage_links(url):
    # This function prints the links found in the webpage.

    # Send a GET request to the specified URL and store the response
    response = requests.get(url)
    webpage_content = response.text

    # Copy the webpage content to a variable for processing
    body_content = webpage_content

    # Initialize an empty list to store the extracted links
    links = []

    # Continue extracting links until no more text is found in the body content
    while len(body_content) > 1:
        # Find the start index of "https://" in the body content
        url_start = body_content.find("https://")
        
        # Find the end index of the next '"' after the start index
        url_end = body_content[url_start:].find('"')
        
        # Extract the link between the start and end indices and append it to the list of links
        links.append(body_content[url_start:url_start + url_end])
        
        # Remove the processed part of the body content
        body_content = body_content[url_start + url_end + 1:]
    
    # Print each extracted link
    for link in links:
        print(link)

def main():
    url = input("Enter your URL with https://: ")
    print()
    print("Page Title:")
    print_page_title(url) 
    print()

    print("Page Body:")
    print_webpage_text(url)
    print()

    print("All the URLs:")
    print_webpage_links(url)

main()

