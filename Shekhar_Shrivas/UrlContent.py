import requests
import sys

def getUrlContent(url):
	page = requests.get(url)
	lines = page.text.splitlines()
	links = []
	bodyArray = []
	bodyCheck = False
	
	for line in lines:
		line = line.strip()
		if line.find("<title>") != -1:
			print("Title :- ",line[line.find("<title>")+7: line.find("</title>")]+"\n")

		if line.find("https") != -1:
			idxOf_https = line.find("https")
			links.append(line[line.find('https') : line.find('"', line.find('"', idxOf_https))])
		########################################################################################
		if line.find("<style") != -1 or line.find("<footer>") != -1 or line.find("</body>") != -1:
			break
		if line.find("<body>") != -1:
			bodyCheck = True
			continue
		if bodyCheck:
			firstidx = line.find(">")
			if line.count(">") == 2 and line[line.find(">")+1:line.find("<",line.find(">"))] != "&nbsp;":
				bodyArray.append(line[line.find(">")+1:line.find("<", line.find(">"))])
				continue
			if line.count(">") > 2:
				bodyArray.append(line[line.find(">", firstidx+1) +1: line.find("<", firstidx + 2)])
				subline = line[line.find(">", firstidx+1)+1: line.find("<", firstidx + 2)]
				indx = line.find(subline) + len(subline)
				idx1 = line.find("<", indx)
				if idx1 == -1:
					idx1 = len(line)
				if line[line.find(":", indx) + 1:].find("<") == -1:
					bodyArray.append((line[line.find(":", indx) + 1:].strip()))
			if line.find(">") == -1:
				bodyArray.append(line)
	print("links of web:-\n")
	for link in links:
		print(link)
	print("end of links:\n")
	print("web body:-\n")
	for row in bodyArray:
		print(row)
	print("body end")

			
		
	


url = sys.argv[1]
getUrlContent(url)
