from cssController.StyleHandler import StyleHandler

class CSSFileHandler:
    teste = "CSS"
    FullCSSFile = ""
    Styles = [
        # {"selectors": "", "properties": ""}
    ]

    mediaQueries = []

    animation = []

    statistics = {
        "mostUsedSelector": "",
        "mostUsedProperty": ""
    }

    def getCSSFile(self, CSSFilePath):
        print("CSS rodando")
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
            
            if(CSSFile[position_end] == "}"):
                style.selectors["fullLine"] = CSSFile[position_end+1:position_start] #extracting selectors             
            else:
                style.selectors["fullLine"] = CSSFile[position_end:position_start] #extracting selectors 

            position_end = CSSFile.find("}", position_start)
            style.properties["fullLine"] = CSSFile[position_start+1:position_end] # extracting properties

            style.handleSelectors()
            # style.handleProperties()
            self.Styles.append(style)
            position_start += 1