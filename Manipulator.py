# import sys
# sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\css")
# sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\htmlP")
# print(sys.path)
from cssController.CSSFileHandler import CSSFileHandler
from htmlController.HTMLFileHandler import HTMLFileHandler

HTMLFileHandler().getHTMLFromFile("files/html.html")
CSSFileHandler().getCSSFile("files/style.css")

class Manipulator:
    def __init__(self):
        pass