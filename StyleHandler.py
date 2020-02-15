import re

class StyleHandler:
    selectors = {
        "fullLine": "",
        "classesUsed": [],
        "idsUsed": [],
        "pseudoClassesUsed": []
    }

    properties = {
        "fullLine": "",
        "propetiesArray": []
    }

    Statistics = {
        "selectorsType": {            
            "tagSelectorsAmount": 0, # when a tag is use to set a style, like 'div', 'a'...
            "tagAttributeSelectorsAmount": 0, # when an tag attribute is used. Defined between [ ] -> ex: [type="text"]
            "classSelectorsAmount": 0, # when a class is selected to set a style with a dot '.'
            "idSelectorsAmount": 0 # when an id tag is used to set the style with a '#'
        },
        "pseudoClassesUsed": [], # all pseudo classes commonly used is defined in CssFileHandler
        "specialPropertiesUsed": [] # @media or @keyframe queries names 
    }

    def handleSelectors(self):
        selectors = self.selectors["fullLine"].replace("\t", "") # removing possible existing tabs
        print(selectors)

        i = 0
        while i < len(selectors):
            print(re.search("(?:.|#|~|+|>|*)", selectors))                


    def handleProperties(self):
        propertiesArray = self.properties["fullLine"].split()
        print(propertiesArray)
