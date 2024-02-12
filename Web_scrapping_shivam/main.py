from web import *
def main():
    url = input("Enter your Url with https: ")
    print('********************************************************************************')
    html_content = get_html_content(url)
    print("Title:")
    print(extract_title(html_content))
    print('********************************************************************************')
    print("Texts:")
    print(extract_body(html_content))
    print('*********************************************************************************')
    print("Links:")
    extract_links(html_content)

main()
