from os import listdir

def getFiles():
    files = listdir()
    img = []
    for file in files:
        extension = ""
        endOfFile = False
        for i in file:
            if i == ".":
                endOfFile = True
            elif endOfFile == True:
                extension += i.lower()
        if extension == "png" or extension == "jpg":
            img.append(file)
    return img

def buildImgTags(images):
    htmlArray = []
    for i in images:
        htmlArray.append('<img src="' + i + '">')
    return htmlArray

def buildHTML(htmlTags):
    html = open('index.html', "w+")
    for i in htmlTags:
        html.write(i + "\r")
    html.close()

def main():
    images = getFiles()
    htmlArray = buildImgTags(images)
    buildHTML(htmlArray)
    print(htmlArray)

main()