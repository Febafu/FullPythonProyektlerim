import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MusicPlayerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(200, 200, 300, 150)
        
        self.layout = QVBoxLayout()

        self.play_button = QPushButton('Play Music', self)
        self.play_button.clicked.connect(self.play_music)
        self.layout.addWidget(self.play_button)

        self.stop_button = QPushButton('Stop Music', self)
        self.stop_button.clicked.connect(self.stop_music)
        self.layout.addWidget(self.stop_button)

        self.setLayout(self.layout)
        self.player = QMediaPlayer(self)

    def play_music(self):
        url = QUrl.fromLocalFile('MahninizinMekani.mp3')
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def stop_music(self):
        self.player.stop()

def main():
    app = QApplication(sys.argv)
    window = MusicPlayerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
