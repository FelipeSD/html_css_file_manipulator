
import re
import codecs  # regex


def handleAttributes(tag, arrayProperty):
    tagAttributes = {"tagName": "", "class": "", "id": ""}
    index_start = index_end = 0

    # this block is to get the tag prepared to be splitted as an array
    # and extract the attributes from the property to put them into a dictionary properly
    i = 0
    while tag.find("=\"", index_start) >= 0:
        index_start = tag.find("=\"", index_start)
        index_end = tag.find("\"", index_start+2)
        tag = tag[:index_start+1]+str(i)+tag[index_end+1:]
        print(tag)
        i += 1
        index_start += 2

    tagInfo = tag.split(" ")
    print(tagInfo)

    return tagAttributes


def handleTag(tag):
    # for use in handleAttributes
    indexAtributes = []
    arrayProperty = []

    index_start = index_end = 0
    while tag.find("=\"", index_start) >= 0:
        index_start = tag.find("=\"", index_start)
        index_end = tag.find("\"", index_start+2)

        propertyAttr = tag[index_start+2:index_end]

        arrayProperty.append(propertyAttr)
        indexAtributes.append([index_start, index_end])

        index_start += 2

    # returns tag informations
    return handleAttributes(tag, arrayProperty)


def handleHTMLFile(HTMLFile):
    DOMElements = []

    for line in HTMLFile:
        # for each line, index position should start from beginning again
        # so you can match both minified and non minified HTML code
        position_start = position_end = 0

        while line.find("<", position_start) >= 0:  # go through in search for opening tags
            position_start = line.find("<", position_start)
            position_end = line.find(">", position_end)

            # don't take closing tags because they don't have any attributes
            if(line[position_start+1] != '/'):
                tag = line[position_start+1:position_end]
                DOMElements.append(handleTag(tag))

            position_start += 1
            position_end += 1


def main(HTMLFilePath, CSSFilePath=None):
    HTMLFile = open(HTMLFilePath, "r")
    handleHTMLFile(HTMLFile)
    HTMLFile.close()


main("html.html")
