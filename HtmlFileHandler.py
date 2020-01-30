from TagHandler import TagHandler

class HtmlFileHandler:
    #object properties
    DOMElements = []
    HTMLDocument = None

    Statistics = {
        "TagNameQuantity": [{"tagName": ""}],
        "TagClassQuantity": [{"className": ""}],
    }

    def getHtmlFromFile(self, HTMLFilePath):
        self.HTMLDocument = open(HTMLFilePath, "r")
        self.handleHTMLFile(self.HTMLDocument) #It calls inside method to handle the file
        self.HTMLDocument.close()

    def getHtmlFromInput(self):
        HTMLText = input("HTML: ")
        print(HTMLText)

    #most important class method
    def handleHTMLFile(self, HTMLFile):
        treePosition = 0

        for line in HTMLFile:
            # for each line, index position should start from beginning again
            # so it is possible to match both minified and non minified HTML code
            position_start = position_end = 0

            while line.find("<", position_start) >= 0:  # go through in search for opening tags
                position_start = line.find("<", position_start)
                position_end = line.find(">", position_end)

                # don't take closing tags because they don't have any attributes
                if(line[position_start+1] != '/'):

                    tag = TagHandler()
                    tag.fullTag = line[position_start+1:position_end]
                    tag.treePosition = treePosition
                    tag.handleTag(tag.fullTag)
                    print(tag.fullTag)
                    self.DOMElements.append(tag)
                    treePosition += 1
                    # DOMElements.append(handleTag(tag))
                else:
                    treePosition -= 1

                position_start += 1
                position_end += 1

myHtml = HtmlFileHandler()
myHtml.getHtmlFromFile("html.html")
print(myHtml.DOMElements)
