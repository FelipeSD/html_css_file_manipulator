import sys
sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\css")
sys.path.insert(0, "c:\\Projetos\\html_css_file_manipulator\\html")
print(sys.path)
import CSSFileHandler as cssfh
import HTMLFileHandler as htmlfh

htmlfh.HTMLFileHandler.getHTMLFromFile("c:\\Projetos\\html_css_file_manipulator\\files\\HTML.HTML")
class Manipulator:
    def __init__(self):
        pass