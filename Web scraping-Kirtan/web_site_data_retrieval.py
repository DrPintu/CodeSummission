import sys
import requests
import os
import time

def file_loader(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open('data.txt', 'w', encoding='utf-32') as f:
                f.write(response.text)
        else:
            return None

    except Exception as e:
        print(e)
        return None
    
    with open('data.txt', 'r', encoding='utf-32') as f:
        data = f.read()
    time.sleep(5)
    os.remove('data.txt')
    
    return data

def readingLines(file):
    flag = False
    spaceFlag = True
    text = ''

    while True:
        startScript = file.find('<script')
        endScript = file.find('</script>')
        startStyle = file.find('<style')
        endStyle = file.find('</style>')
        
        if startScript == -1 and startStyle == -1:
            break

        if startScript != -1 and (startScript < startStyle or startStyle == -1):
            file = file[ : startScript] + file[endScript + 9 : ]

        elif startStyle != -1 and (startStyle < startScript or startScript == -1):
            file = file[ : startStyle] + file[endStyle + 8 : ]

    for i in file:
        if i == '<':
            flag = False

        if i == '>':
            flag = True

        elif flag:
            if i.isspace() and spaceFlag:
                text += i
                spaceFlag = False

            else:
                if not i.isspace():
                    text += i
                    spaceFlag = True
                    
    text = specialCharacterDecoder(text)

    return text


def linkfinder(file):

    linkIndex = file.find('https://')
    endOfLink = file.find('"', linkIndex + 1)

    for _ in range(len(file)):

        if linkIndex == -1:
            break
        
        linkIndex = file.find('https://', endOfLink + 1)
        endOfLink = file.find('"', linkIndex + 1)

        link = file[linkIndex : endOfLink]
        print(link)


def specialCharacterDecoder(text):

    characters = {
    "&lt;": "<",
    "&gt;": ">",
    "&amp;": "&",
    "&quot;": "\"",
    "&#39;": "'",
    "&#34;": "\"",
    "&#38;": "&",
    "&#60;": "<",
    "&#62;": ">",
    "&#160;": " ",
    "&#161;": "¡",
    "&#162;": "¢",
    "&#163;": "£",
    "&#164;": "¤",
    "&#165;": "¥",
    "&#166;": "¦",
    "&#167;": "§",
    "&#168;": "¨",
    "&#169;": "©",
    "&#170;": "ª",
    "&#171;": "«",
    "&#172;": "¬",
    "&#173;": "­",
    "&#174;": "®",
    "&#175;": "¯",
    "&#176;": "°",
    "&#177;": "±",
    "&#178;": "²",
    "&#179;": "³",
    "&#180;": "´",
    "&#181;": "µ",
    "&#182;": "¶",
    "&#183;": "·",
    "&#184;": "¸",
    "&#185;": "¹",
    "&#186;": "º",
    "&#187;": "»",
    "&#188;": "¼",
    "&#189;": "½",
    "&#190;": "¾",
    "&#191;": "¿",
    "&#192;": "À",
    "&#193;": "Á",
    "&#194;": "Â",
    "&#195;": "Ã",
    "&#196;": "Ä",
    "&#197;": "Å",
    "&#198;": "Æ",
    "&#199;": "Ç",
    "&#200;": "È",
    "&#201;": "É",
    "&#202;": "Ê",
    "&#203;": "Ë",
    "&#204;": "Ì",
    "&#205;": "Í",
    "&#206;": "Î",
    "&#207;": "Ï",
    "&#208;": "Ð",
    "&#209;": "Ñ",
    "&#210;": "Ò",
    "&#211;": "Ó",
    "&#212;": "Ô",
    "&#213;": "Õ",
    "&#214;": "Ö",
    "&#215;": "×",
    "&#216;": "Ø",
    "&#217;": "Ù",
    "&#218;": "Ú",
    "&#219;": "Û",
    "&#220;": "Ü",
    "&#221;": "Ý",
    "&#222;": "Þ",
    "&#223;": "ß",
    "&#224;": "à",
    "&#225;": "á",
    "&#226;": "â",
    "&#227;": "ã",
    "&#228;": "ä",
    "&#229;": "å",
    "&#230;": "æ",
    "&#231;": "ç",
    "&#232;": "è",
    "&#233;": "é",
    "&#234;": "ê",
    "&#235;": "ë",
    "&#236;": "ì",
    "&#237;": "í",
    "&#238;": "î",
    "&#239;": "ï",
    "&#240;": "ð",
    "&#241;": "ñ",
    "&#242;": "ò",
    "&#243;": "ó",
    "&#244;": "ô",
    "&#245;": "õ",
    "&#246;": "ö",
    "&#247;": "÷",
    "&#248;": "ø",
    "&#249;": "ù",
    "&#250;": "ú",
    "&#251;": "û",
    "&#252;": "ü",
    "&#253;": "ý",
    "&#254;": "þ",
    "&#255;": "ÿ",
}


    for code, char in characters.items():
        text = text.replace(code, char)

    return text

if __name__=="__main__":
    path = sys.argv[1]
    print(readingLines(file_loader(path)))
    linkfinder(file_loader(path))
