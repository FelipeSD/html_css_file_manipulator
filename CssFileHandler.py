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
        "+": "next sibling"
    }

    FullCSSFile = []
    Styles = [
        {"selectors": "", "properties": ""}
    ]

    mediaQueries = []

    animation = []

    def getCSSFile(self, CSSFilePath):
        CSSFile = open(CSSFilePath, "r")
        ALLFile = CSSFile.read().split()
        print("".join(ALLFile))
        self.handleCSSFile(CSSFile)
        CSSFile.close()
    
    def handleCSSFile(self, CSSFile):
        for line in CSSFile:
            self.FullCSSFile.append(line)
            # for each line, index position should start from beginning again
            # so it is possible to match both minified and non minified CSS code
            position_start = position_end = 0

            # print(len(line))
            if(len(line)>0):
                if(line.find("{", position_start) > 0):                    
                    position_start = line.find("{", position_start)

                    selector = line[:position_start]
                    position_start += 1
                    # print(selector)
                else:
                    if(line.find("}", position_start) > 0):
                        pass
            


myCss = CSSFileHandler()
myCss.getCSSFile("style.css")