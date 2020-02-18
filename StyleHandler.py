import re

class StyleHandler:
    pseudoClassList = (
        ":link", ":vistited", ":active", ":hover",
        ":focus", ":first-child", ":last-child", 
        ":nth-child", ":nth-last-child", ":nth-of-type", 
        ":first-of-type", ":last-of-type", ":empty", ":target",
        ":checked", ":enabled", ":disabled"
    )

    relationshipSelectors = [
        " ", 
        ">",
        "+",
        "~",
        "*"
    ]

    def __init__(self):
        self.selectors = {
            "fullLine": "",
            "classesUsed": [],
            "idsUsed": [],
            "tagsUsed": [],
            "attributesUsed": [],
            "pseudoClassesUsed": []
        }

        self.properties = {
            "fullLine": "",
            "propetiesArray": []
        }

        self.statistics = {
            "selectorsType": {            
                "tagSelectorsAmount": 0, # when a tag is use to set a style, like 'div', 'a'...
                "tagAttributeSelectorsAmount": 0, # when an tag attribute is used. Defined between [ ] -> ex: [type="text"]
                "classSelectorsAmount": 0, # when a class is selected to set a style with a dot '.'
                "idSelectorsAmount": 0 # when an id tag is used to set the style with a '#'
            },

            "specialPropertiesUsed": [] # @media or @keyframe queries names 
        }

    def handleSelectors(self):
        # self.selectors["classesUsed"] = [],
        # self.selectors["idsUsed"] = [],
        # self.selectors["tagsUsed"] = [],
        # self.selectors["attributesUsed"] = [],
        # self.selectors["pseudoClassesUsed"] = []
        
        selectors = self.selectors["fullLine"].replace(r"\t", "") # removing possible existing tabs

        selectors = selectors.split(",")
        # print(selectors)

        for selector in selectors:

            #removing pseudo classes
            for pseudoClass in self.pseudoClassList:
                match = re.search(pseudoClass, selector)
                if(match):
                    self.selectors["pseudoClassesUsed"].append(pseudoClass)
                    selector = selector[:match.start()]+selector[match.end():]
            
            #removing relationship selectors
            newSelectorArray = selector.split() #removing descendent selector " " or \s
            newSelectorArray = [s for s in newSelectorArray if s not in self.relationshipSelectors] #filtering another relationship selectors

            #separating selectors -> ex: .className.anotherClassName
            for s in newSelectorArray:
                next_position = 0
                indexSelector = []
                while True:
                    match = re.search(r"\.|\#|\[", s[next_position:])
                    if(match):
                        indexSelector.append(match.start())
                        next_position = match.start()+1
                    else:
                        break

                print(indexSelector)

                i=0
                if(len(indexSelector) != 0 and indexSelector[i] != 0):
                    print("Primeiro seletor é uma tag")
                    self.selectors["tagsUsed"].append(s[:indexSelector[i]])

                for i in range(len(indexSelector)):
                    index = indexSelector[i]

                    if i+1 <= len(indexSelector):
                        if(s[index] == "."):
                            print("Class")
                            self.selectors["classesUsed"].append(s[index:])
                        elif(s[index] == "#"):
                            print("ID")
                            self.selectors["idsUsed"].append(s[index:])
                        elif(s[index] == "["):
                            print("ATTRIBUTE")
                            self.selectors["attributesUsed"].append(s[index:])
                        else:
                            print("TAG")
                            self.selectors["tagsUsed"].append(s[index:])

    def handleProperties(self):
        propertiesArray = self.properties["fullLine"].split()
        # print(propertiesArray)
