
import re
import codecs  # regex


def handleAttributes(arrayTag, arrayProperty):
    tagAttributes = {"tagName": "", "tagAttributes": {}}
    tagAttributes["tagName"] = arrayTag[0]

    i = 1
    print(arrayTag)
    for tagProperty in arrayProperty:
        arrayTag[i] = arrayTag[i][:arrayTag[i].find("=")]
        tagAttributes["tagAttributes"][arrayTag[i]] = tagProperty.split(" ")
        i += 1

    # print(tagAttributes)
    return tagAttributes


def handleTag(tag):
    # for use in handleAttributes
    arrayProperty = []

    index_start = index_end = 0
    i = 0
    while tag.find("=\"", index_start) >= 0:
        index_start = tag.find("=\"", index_start)
        index_end = tag.find("\"", index_start+2)

        propertyAttr = tag[index_start+2:index_end]
        # print(propertyAttr)
        arrayProperty.append(propertyAttr)

        tag = tag[:index_start+1]+str(i)+tag[index_end+1:]

        index_start += 2
        i += 1

    arrayTag = tag.split(" ")
    return handleAttributes(arrayTag, arrayProperty)


def handleHTMLFile(HTMLFile):
    DOMElements = []
    # handle with DOM tree
    DOMGeneration = []
    treePosition = 0

    for line in HTMLFile:
        # for each line, index position should start from beginning again
        # so you can match both minified and non minified HTML code
        position_start = position_end = 0

        while line.find("<", position_start) >= 0:  # go through in search for opening tags
            position_start = line.find("<", position_start)
            position_end = line.find(">", position_end)

            # don't take closing tags because they don't have any attributes
            if(line[position_start+1] != '/'):
                treePosition += 1
                tag = line[position_start+1:position_end]
                DOMElements.append(handleTag(tag))
            else:
                treePosition -= 1


            position_start += 1
            position_end += 1

    print(DOMElements)


def main(HTMLFilePath, CSSFilePath=None):
    HTMLFile = open(HTMLFilePath, "r")
    handleHTMLFile(HTMLFile)
    HTMLFile.close()


main("html.html")
