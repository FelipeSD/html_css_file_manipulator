from TagHandler import TagHandler

class HTMLFileHandler:
    #object properties
    DOMElements = []
    fullHTMLFile = []

    Statistics = {
        "tagNameQuantity": [{"tagName": ""}],
        "tagClassQuantity": [{"className": ""}],
    }

    def getHTMLFromFile(self, HTMLFilePath):
        HTMLDocument = open(HTMLFilePath, "r")
        self.handleHTMLFile(HTMLDocument) #It calls inside method to handle the file
        HTMLDocument.close()

    def getHTMLFromInput(self):
        HTMLText = input("HTML: ")
        print(HTMLText)

    #most important class method
    def handleHTMLFile(self, HTMLFile):
        treePosition = 0

        for line in HTMLFile:
            self.fullHTMLFile.append(line)
            # for each line, index position should start from beginning again
            # so it is possible to match both minified and non minified HTML code
            position_start = position_end = 0

            while line.find("<", position_start) >= 0:  # go through line in search for opening tags
                position_start = line.find("<", position_start)
                position_end = line.find(">", position_end)

                # don't take closing tags because they don't have any attributes
                if(line[position_start+1] != '/'):
                    tag = TagHandler()
                    tag.fullTag = line[position_start:position_end+1]
                    tag.treePosition = treePosition
                    tag.handleTag(line[position_start+1:position_end])
                    # print(tag.tagAttributes)
                    self.DOMElements.append(tag)
                    treePosition += 1
                else:
                    treePosition -= 1

                position_start += 1
                position_end += 1


myHTML = HTMLFileHandler()
myHTML.getHTMLFromFile("HTML.HTML")