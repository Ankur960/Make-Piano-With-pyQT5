import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, ,QLabel ,QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QHideEvent, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, QObject, QSize,Qt
import pygame






class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CL Piano '        self.left = 620        self.top =250        self.width = 900        self.height = 600        self.initUI()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Q:
            self.b1()
        elif e.key() == Qt.Key_W: \
                self.b2()
        elif e.key() == Qt.Key_E:
            self.b3()

        elif e.key() == Qt.Key_R:
            self.b4()

        elif e.key() == Qt.Key_T:
            self.b5()
        elif e.key() == Qt.Key_Y:
            self.b6()
        elif e.key() == Qt.Key_U:
           self.b7()
        elif e.key() == Qt.Key_I:
          self.b8()

        elif e.key() == Qt.Key_A:
            self.bb1()
        elif e.key() == Qt.Key_S:
            self.bb2()
        elif e.key() == Qt.Key_D:
            self.bb3()
        elif e.key() == Qt.Key_F:
            self.bb4()
        elif e.key() == Qt.Key_G:
            self.bb5()
        elif e.key() == Qt.Key_H:
            self.bb6()
        elif e.key() == Qt.Key_J:
            self.bb7()
      
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setStyleSheet("background-color:white")
        self.setWindowIcon(QIcon('img.png'))

        # Create a button in the window        self.button1 = QPushButton('s', self)
        self.button1.move(10, 340)
        self.button1.setFont(QFont('Arial', 14))
        self.button1.resize(100,250)
        self.button1.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button2 = QPushButton('s', self)
        self.button2.move(120, 340)
        self.button2.setFont(QFont('Arial', 14))
        self.button2.resize(100, 250)
        self.button2.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button3 = QPushButton('s', self)
        self.button3.move(230, 340)
        self.button3.setFont(QFont('Arial', 14))
        self.button3.resize(100, 250)
        self.button3.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button4 = QPushButton('s', self)
        self.button4.move(340, 340)
        self.button4.setFont(QFont('Arial', 14))
        self.button4.resize(100, 250)
        self.button4.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button5 = QPushButton('s', self)
        self.button5.move(450, 340)
        self.button5.setFont(QFont('Arial', 14))
        self.button5.resize(100, 250)
        self.button5.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button6 = QPushButton('s', self)
        self.button6.move(560, 340)
        self.button6.setFont(QFont('Arial', 14))
        self.button6.resize(100, 250)
        self.button6.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button7 = QPushButton('s', self)
        self.button7.move(670, 340)
        self.button7.setFont(QFont('Arial', 14))
        self.button7.resize(100, 250)
        self.button7.setStyleSheet("background-color:white; border: 9px solid grey;")

        self.button8 = QPushButton('s', self)
        self.button8.move(780, 340)
        self.button8.setFont(QFont('Arial', 14))
        self.button8.resize(100, 250)
        self.button8.setStyleSheet("background-color:white; border: 9px solid grey;")

        #BLACK BUTTON SHADOW EFFECT        self.shadow1=QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(9)
        self.shadow1.setXOffset(6)
        self.shadow1.setYOffset(2)

        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(9)
        self.shadow2.setXOffset(6)
        self.shadow2.setYOffset(2)

        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow3.setBlurRadius(9)
        self.shadow3.setXOffset(6)
        self.shadow3.setYOffset(2)

        self.shadow4 = QGraphicsDropShadowEffect()
        self.shadow4.setBlurRadius(9)
        self.shadow4.setXOffset(6)
        self.shadow4.setYOffset(2)

        self.shadow5 = QGraphicsDropShadowEffect()
        self.shadow5.setBlurRadius(9)
        self.shadow5.setXOffset(6)
        self.shadow5.setYOffset(2)

        self.shadow6 = QGraphicsDropShadowEffect()
        self.shadow6.setBlurRadius(9)
        self.shadow6.setXOffset(6)
        self.shadow6.setYOffset(2)

        self.shadow7 = QGraphicsDropShadowEffect()
        self.shadow7.setBlurRadius(9)
        self.shadow7.setXOffset(6)
        self.shadow7.setYOffset(2)

        #black buttons        self.bbutton1 = QPushButton('s', self)
        self.bbutton1.move(90, 340)
        self.bbutton1.setFont(QFont('Arial', 14))
        self.bbutton1.setGraphicsEffect(self.shadow1)
        self.bbutton1.resize(40, 250)
        self.bbutton1.setStyleSheet("background-color:black;")

        self.bbutton2 = QPushButton('s', self)
        self.bbutton2.move(200, 340)
        self.bbutton2.setFont(QFont('Arial', 14))
        self.bbutton2.resize(40, 250)
        self.bbutton2.setGraphicsEffect(self.shadow2)
        self.bbutton2.setStyleSheet("background-color:black;")

        self.bbutton3 = QPushButton('s', self)
        self.bbutton3.move(310, 340)
        self.bbutton3.setFont(QFont('Arial', 14))
        self.bbutton3.resize(40, 250)
        self.bbutton3.setGraphicsEffect(self.shadow3)
        self.bbutton3.setStyleSheet("background-color:black;")

        self.bbutton4 = QPushButton('s', self)
        self.bbutton4.move(420, 340)
        self.bbutton4.setFont(QFont('Arial', 14))
        self.bbutton4.resize(40, 250)
        self.bbutton4.setGraphicsEffect(self.shadow4)
        self.bbutton4.setStyleSheet("background-color:black;")

        self.bbutton5 = QPushButton('s', self)
        self.bbutton5.move(530, 340)
        self.bbutton5.setFont(QFont('Arial', 14))
        self.bbutton5.resize(40, 250)
        self.bbutton5.setGraphicsEffect(self.shadow5)
        self.bbutton5.setStyleSheet("background-color:black;")

        self.bbutton6 = QPushButton('s', self)
        self.bbutton6.move(640, 340)
        self.bbutton6.setFont(QFont('Arial', 14))
        self.bbutton6.resize(40, 250)
        self.bbutton6.setGraphicsEffect(self.shadow6)
        self.bbutton6.setStyleSheet("background-color:black;")

        self.bbutton7 = QPushButton('s', self)
        self.bbutton7.move(750, 340)
        self.bbutton7.setFont(QFont('Arial', 14))
        self.bbutton7.resize(40, 250)
        self.bbutton7.setGraphicsEffect(self.shadow7)
        self.bbutton7.setStyleSheet("background-color:black;")

        #CONNECT THE WHITE BUTTON        self.button1.clicked.connect(self.b1)
        self.button2.clicked.connect(self.b2)
        self.button3.clicked.connect(self.b3)
        self.button4.clicked.connect(self.b4)
        self.button5.clicked.connect(self.b5)
        self.button6.clicked.connect(self.b6)
        self.button7.clicked.connect(self.b7)
        self.button8.clicked.connect(self.b8)

        #CONNECT THE BLACK BUTTONS        self.bbutton1.clicked.connect(self.bb1)
        self.bbutton2.clicked.connect(self.bb2)
        self.bbutton3.clicked.connect(self.bb3)
        self.bbutton4.clicked.connect(self.bb4)
        self.bbutton5.clicked.connect(self.bb5)
        self.bbutton6.clicked.connect(self.bb6)
        self.bbutton7.clicked.connect(self.bb7)



        self.show()

    @pyqtSlot()
    def b1(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/A.wav')
        pygame.mixer.music.play()

    def b2(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/B.wav')
        pygame.mixer.music.play()

    def b3(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/C.wav')
        pygame.mixer.music.play()


    def b4(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/D.wav')
        pygame.mixer.music.play()

    def b5(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/E.wav')
        pygame.mixer.music.play()

    def b6(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/F.wav')
        pygame.mixer.music.play()

    def b7(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/G.wav')
        pygame.mixer.music.play()

    def b8(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/A.wav')
        pygame.mixer.music.play()

    def bb1(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/Bb.wav')
        pygame.mixer.music.play()

    def bb2(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/C1.wav')
        pygame.mixer.music.play()


    def bb3(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/C_s.wav')
        pygame.mixer.music.play()

    def bb4(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/C_s1.wav')
        pygame.mixer.music.play()

    def bb5(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/D1.wav')
        pygame.mixer.music.play()

    def bb6(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/D_s.wav')
        pygame.mixer.music.play()


    def bb7(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C:/Users/ankur/PycharmProjects/envention/Music_Notes/D_s1.wav')
        pygame.mixer.music.play()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())