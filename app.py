import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class ChronioBoxApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChronioBox - Escritorio")
        self.resize(1280, 720)
        
        # Inicializar el motor web embebido
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://chroniobox.duckdns.org/"))
        
        # Establecer la vista web como el componente principal de la ventana
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChronioBoxApp()
    window.show()
    sys.exit(app.exec_())