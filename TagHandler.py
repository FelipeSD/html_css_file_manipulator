class TagHandler:
    fullTag = ""
    tagName = ""
    tagAttributes = {}
    treePosition = 0

    def handleTag(self, tag):
        # for use in handleAttributes
        arrayProperty = []

        index_start = index_end = 0
        i = 0
        while tag.find("=\"", index_start) >= 0:
            index_start = tag.find("=\"", index_start)
            index_end = tag.find("\"", index_start+2)

            propertyAttr = tag[index_start+2:index_end]
            arrayProperty.append(propertyAttr)

            tag = tag[:index_start+1]+str(i)+tag[index_end+1:]
            index_start += 2 # +2 because of the search for =" group
            i += 1

        arrayTag = tag.split(" ")
        return self.handleAttributes(arrayTag, arrayProperty)

    def handleAttributes(self, arrayTag, arrayProperty):
        #the first position must always be the tag name
        self.tagAttributes = {}
        self.tagName = arrayTag[0]

        i = 1
        for tagProperty in arrayProperty:
            arrayTag[i] = arrayTag[i][:arrayTag[i].find("=")] #set attribute name
            self.tagAttributes[arrayTag[i]] = tagProperty.split(" ") # set properties to its attribute
            i += 1
