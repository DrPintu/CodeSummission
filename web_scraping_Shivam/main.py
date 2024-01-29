from webpage import *

def main():
    # Prompt the user to enter a URL
    url = input("Enter your URL with https://:")
    
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
