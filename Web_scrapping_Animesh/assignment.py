import requests
import sys

class WebScraper:
    
    def __init__(self, url):
        self.url = url
        self.html = self.get_html()
        
    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def get_title(self):
        start = self.html.find('<title>') + len('<title>')
        end = self.html.find('</title>')
        title = self.html[start:end]
        return title

    def get_body(self):
        start = self.html.find('<body')
        end = self.html.find('</body>')
        body = self.html[start:end]
        text = self.remove_html_tags(body)
        return text

    def remove_html_tags(self, html):
        result = ''
        stack = []
        ignore_content = True
        for i in range(len(html)):
            if html[i:i+7] == '<footer':
                ignore_content = True
            if html[i:i+2] == '<a':
                ignore_content = True
            elif html[i:i+4] == '</a>':
                ignore_content = False
            if html[i:i+7] == '<header':
                ignore_content = True
            elif html[i:i+9] == '</header>':
                ignore_content = False
            if html[i:i+6] == '<style':
                ignore_content = True
            elif html[i:i+8] == '</style>':
                ignore_content = False
            if html[i:i+7] == '<script':
                ignore_content = True
            elif html[i:i+9] == '</script>':
                ignore_content = False
            if not ignore_content:
                if html[i] == '<':
                    stack.append('<')
                elif html[i] == '&':
                    stack.append('&')
                elif html[i] == '>':
                    if stack and stack[-1] == '<':
                        stack.pop()
                elif html[i] == ';':
                    if stack and stack[-1] == '&':
                        stack.pop()
                elif not stack and html[i] not in {',', '.', '^', '!', '|', '\\', '/', '"', "'", "?", ':'}:
                    result += html[i]
        result = ' '.join(result.split())
        return result

    def extract_links(self):
        lst = self.html.split()
        for element in lst:
            if 'href="' in element:
                start = element.find('href="') + len('href="')
                end = element.find('">', start)
                if end != -1:
                    link = element[start:end]
                    if "http" in link:
                        print(link)

if __name__ == "__main__":
    url = sys.argv[1]
    scraper = WebScraper(url)
    print("\nTitle:\n", scraper.get_title())
    print("\nBody:\n", scraper.get_body())
    print("\nLinks:\n")
    scraper.extract_links()