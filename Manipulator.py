# import sys
# sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\css")
# sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\htmlP")
# print(sys.path)
from cssController.CSSFileHandler import CSSFileHandler
from htmlController.HTMLFileHandler import HTMLFileHandler

class Manipulator:

    def generateNewCssFile(self, arrayHtmlFiles, arrayCssFiles):
        print("Aqui")
        for html in arrayHtmlFiles:
            for tag in html.DOMElements:
                print(tag.tagName)
        
        for css in arrayCssFiles:
            for style in css.Styles:
                print(style.selectors)

manipulator = Manipulator()
myHtml = HTMLFileHandler()
myHtml.getHTMLFromFile("files/html.html")
myCss = CSSFileHandler()
myCss.getCSSFile("files/style.css")
manipulator.generateNewCssFile([myHtml], [myCss])