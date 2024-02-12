import requests
def remove_html_tags(text):
    while True:
        script1 = text.find("<script")
        script2 = text.find("</script>")
        if script1 == -1 or script2 == -1:
            break
        text = text[:script1] + text[script2 + len("</script>"):]
    while True:
        style1 = text.find("<style")
        style2 = text.find("</style>")
        if style1 == -1 or style2 == -1:
            break
        text = text[:style1] + text[style2 + len("</style>"):]

    #Remove HTML entities like &#xxx;
    while "&#" in text:
        start_index = text.find("&#")
        end_index = text.find(";", start_index)
        if start_index != -1 and end_index != -1:
            text = text[:start_index] + text[end_index + 1:]
        else:
            break

    inside_tag = False
    result = ""

    # iterate over text
    for i in text:
        # if it is <,then we can see that it is opening tag of html so assign itto true.
        if i == "<":
            inside_tag = True

        # if it is >, closing tag so, assign itto false.
        elif i == ">":
            inside_tag = False

        # if it is not inside any tag, then add it to empty string result.
        elif not inside_tag:
            result += i
    result = result.split("\n")
    body = ""
    for line in result:
        if line.strip()=="":
            body += line.strip()
        else:
            body += "\n"+line.strip()      
    return body

def scrap(html_content):
    title_index = html_content.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html_content.find("</title>")
    title = html_content[start_index:end_index]
    body = remove_html_tags(html_content)

    links = []
    start_i = 0
    # loop will iterate till the number of href=\" appeared
    for i in range(html_content.count("href=\"")): 

        #in this, it will take index of href, starting from start_i
        #because if we didn't do that, then same link will be printed multiple(no. of href appeared) times.
        start_i = html_content.find("href=\"", start_i)

        #if there is no link after that, then loop will break
        if start_i == -1:
            break
        
        start_i += len("href=\"")
        #it's finding index of end of the link.
        end_i = html_content.find("\"", start_i)

        # now, extracting the link using string slicing
        link = html_content[start_i:end_i]

        #Now,I will add a condn so that the link starts with https should print.
        # Initialize the prefix to check
        prefix = "https://"

        # Check if the link starts with the prefix
        if link[:len(prefix)] == prefix:
        # If it does, append it to the accumulator
            links.append(link)

        # updating the value of start_i, so that it will start again after end of the link.
        start_i = end_i + 1

    # returning title, body and links
    return title, body, links

def main():
    url = input("enter the url:  ")
    response = requests.get(url)
    html_content = response.text
    title, body, links = scrap(html_content)
    print("Title:", title)
    print("\nPage Body:", body)
    print("\nLinks found on the webpage:")
    for link in links:
        print(link)

if __name__== "__main__":
    main()