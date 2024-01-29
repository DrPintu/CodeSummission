import requests

# Function to extract and print the title of a webpage
def title(url):
    # Make a GET request to the specified URL
    response = requests.get(url)
    
    # Get the raw HTML content of the response
    raw_content = response.text
    
    # Find the start and end index of the title tag
    title_start = raw_content.find("<title>") + len("<title>")
    title_end = raw_content.find("</title>")
    
    # Extract the title and print it
    title = raw_content[title_start:title_end]
    print("Title:", title)

# Function to extract and print the text content from the body of a webpage
def body(url):
    # Make a GET request to the specified URL
    response = requests.get(url)
    html_content = response.text

    texts = []
    start_index = html_content.find("<body")

    if start_index != -1:
        # Move to the start of the body content
        start_index = html_content.find(">", start_index) + 1

        while start_index != -1:
            # Find the end index of the current tag
            end_index = html_content.find("<", start_index)

            if end_index != -1:
                # Extract text content between tags
                text = html_content[start_index:end_index].strip()
                if text:
                    texts.append(text)
                # Move to the next tag
                start_index = html_content.find(">", end_index) + 1
            else:
                break

    # Print the extracted text content
    for t in texts:
        print("Text:", t)

# Function to extract and print links from a webpage
def links(url):
    # Make a GET request to the specified URL
    response = requests.get(url)
    raw_content = response.text

    body_raw_content = raw_content

    link = []
    while len(body_raw_content) > 1:
        # Find the start and end index of a link
        s = body_raw_content.find("http")
        e = body_raw_content[s:].find('"')
        
        # Extract the link and append to the list
        link.append(body_raw_content[s :s + e])
        
        # Move to the next occurrence of a link
        body_raw_content = body_raw_content[s + e + 1:]

    # Print the extracted links
    for j in link:
        print("Link:", j)

# Main function to execute the program
def main():
    # Get user input for the URL
    url = input("Enter your Url with https: ")
    
    # Execute the title, body, and links functions
    title(url)
    body(url)
    links(url)

# Entry point of the program
if __name__ == "__main__":
    main()
