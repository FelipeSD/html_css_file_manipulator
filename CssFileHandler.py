from StyleHandler import StyleHandler

class CSSFileHandler:
    pseudoClassList = (
        ":link", ":vistited", ":active", ":hover",
        ":focus", ":first-child", ":last-child", 
        ":nth-child", ":nth-last-child", ":nth-of-type", 
        ":first-of-type", ":last-of-type", ":empty", ":target",
        ":checked", ":enabled", ":disabled"
    )

    relationshipSelectors = {
        " ": "descendent", 
        ">": "child",
        "+": "next sibling",
        "~": "general sibling",
        "*": "all"
    }

    FullCSSFile = ""
    Styles = [
        {"selectors": "", "properties": ""}
    ]

    mediaQueries = []

    animation = []

    Statistics = {
        "mostUsedSelector": "",
        "mostUsedProperty": ""
    }

    def getCSSFile(self, CSSFilePath):
        CSSFile = open(CSSFilePath, "r")
        self.FullCSSFile = CSSFile.read()

        ALLFile = self.FullCSSFile.split("\n")
        ALLFile = "".join(ALLFile) #making the file minified

        self.handleCSSFile(ALLFile)

        CSSFile.close()

    # CSS Files are only handled in minified mode
    def handleCSSFile(self, CSSFile):
        position_start = position_end = 0

        while CSSFile.find("{", position_start) > 0 :
            style = StyleHandler()
            position_start = CSSFile.find("{", position_start)

            if(position_end < position_start):
                style.selectors["fullLine"] = CSSFile[position_end+1:position_start] #extracting selectors             
            else: 
                style.selectors["fullLine"] = CSSFile[:position_start] #extracting selectors

            position_end = CSSFile.find("}", position_start)
            style.properties["fullLine"] = CSSFile[position_start+1:position_end] # extracting properties

            style.handleSelectors()
            style.handleProperties()

            position_start += 1

myCss = CSSFileHandler()
myCss.getCSSFile("style.css")