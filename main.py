
import re, codecs #regex

def handleAttributes(tag, arrayIndex, arrayProperty):
    tagAttributes = {"tagName": "", "class": "", "id":""}
    for i in range(0, len(arrayIndex)):
        print(i+" "+arrayProperty[i])
        while tag.find("=\"") >= 0:
            index_start = tag.find("=\"")
            index_end = tag.find("\"")
            tag[index_start+1:index_end] = i

    # print("-"*10+"HANDLE Attributes"+"-"*10+"\n")
    # print("TAG HTML ORIGINAL: "+tag)
    # for i in range(0, len(arrayIndex)):
    #     print(arrayIndex[i], arrayProperty[i])
    #     print("final: "+str(arrayIndex[i][1]))
    #     print("propriedades: "+ tag[arrayIndex[i][0]+2:arrayIndex[i][1]])
    #
    #     newTag = tag.replace(
    #         tag[arrayIndex[i][0]+2:arrayIndex[i][1]],
    #         "{}".format(int(i))
    #     )
    #
    #     #reduce next attribute indexes related to current indexes
    #     if((i+1) <= (len(arrayIndex)-1)):
    #         subtract = arrayIndex[i][1] - arrayIndex[i][0]
    #         arrayIndex[i+1][0] = arrayIndex[i+1][0] - subtract
    #         arrayIndex[i+1][1] = arrayIndex[i+1][1] - subtract
    #
    #
    # print("\nTAG FINAL: "+ tag+"\n")
    # print("Nova tag"+newTag)
    # print("-"*10+"FIM HANDLE Attributes"+"-"*10)

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

        index_start +=2

    #returns tag informations
    return handleAttributes(tag, indexAtributes, arrayProperty)

def handleHTMLFile(HTMLFile):
    DOMElements = []

    for line in HTMLFile:
        # for each line, index position should start from beginning again
        # so you can match both minified and non minified HTML code
        position_start = position_end = 0

        while line.find("<", position_start) >= 0: #go through in search for opening tags
            position_start = line.find("<", position_start)
            position_end = line.find(">", position_end)

            if(line[position_start+1] != '/'): #don't take closing tags because they don't have any attributes
                tag = line[position_start+1:position_end]
                DOMElements.append(handleTag(tag))

            position_start += 1
            position_end += 1



def main(HTMLFilePath, CSSFilePath=None):
    HTMLFile = open(HTMLFilePath, "r")
    handleHTMLFile(HTMLFile)
    HTMLFile.close()

main("html.html")
