from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
# This is a simple web browser using PyQt5 and PyQtWebEngine.
# It creates a main window with a web view and a menu bar with a "New Tab" option.
# The web view loads the Google homepage by default.
# The "New Tab" option opens a new web view with the Google homepage.

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.urlbar = QLineEdit()
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.navtbar = QToolBar("Navigation")
        self.addToolBar(self.navtbar)
#back button         
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        self.navtbar.addAction(back_btn)
#forward button        
        next_btn = QAction("forward", self)
        next_btn.triggered.connect(self.browser.forward)
        self.navtbar.addAction(next_btn)
#reload button        
        reload_btn = QAction("reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        self.navtbar.addAction(reload_btn)
#home button
        home_btn = QAction("home", self)
        home_btn.triggered.connect(self.navigate_home)
        self.navtbar.addAction(home_btn)

#stop button
        stop_btn = QAction("stop", self)
        stop_btn.triggered.connect(self.browser.stop)
        self.navtbar.addAction(stop_btn)
        
        self.navtbar.addWidget(self.urlbar)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        self.navtbar.addSeparator()
        self.urlbar.returnPressed.connect(self.navigate_to_url) 
        
        
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        if q.scheme() == "http" or q.scheme() == "https":
            self.browser.setUrl(q)
        else:
            QMessageBox.critical(self, "Error", "Invalid URL")
            return      
        
        
        
        self.create_menu()
#urlbar updation
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
        
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - Web Browser")
    
    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        new_tab_action = QAction('New Tab', self)
        new_tab_action.triggered.connect(self.new_tab)
        file_menu.addAction(new_tab_action)

    def new_tab(self):
        new_browser = QWebEngineView()
        new_browser.setUrl(QUrl("https://www.google.com"))
        new_browser.show()  
        
app = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
window = MainWindow()
app.exec_()
window.show()