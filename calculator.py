from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication,
QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton) 
#создание приложения и главного окна
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Калькулятор') 
main_window.resize(800, 800)

#кнопки
plus_button = QPushButton('+')
minus_button = QPushButton('-')
umnoz_button = QPushButton('*')
del_button = QPushButton('/')
ravn_button = QPushButton('=')
zap_button = QPushButton(',')
backspace_button = QPushButton('<-')
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
button6 = QPushButton('6')
button7 = QPushButton('7')
button8 = QPushButton('8')
button9 = QPushButton('9')
button0 = QPushButton('0')
#layouts
hor_layout_for_buttons1 = QHBoxLayout()
hor_layout_for_buttons2 = QHBoxLayout()
hor_layout_for_buttons3 = QHBoxLayout()
hor_layout_for_buttons4 = QHBoxLayout()
hor_layout_for_buttons5 = QHBoxLayout()

vert_layout_for_buttons1 = QVBoxLayout()
vert_layout_for_buttons2 = QVBoxLayout()
vert_layout_for_buttons3 = QVBoxLayout()
main_vert_layout = QVBoxLayout()


hor_layout_for_buttons1.addWidget(backspace_button)
hor_layout_for_buttons1.addWidget(del_button)

hor_layout_for_buttons2.addWidget(button1)
hor_layout_for_buttons2.addWidget(button2)
hor_layout_for_buttons2.addWidget(button3)
hor_layout_for_buttons2.addWidget(umnoz_button)

hor_layout_for_buttons3.addWidget(button4)
hor_layout_for_buttons3.addWidget(button5)
hor_layout_for_buttons3.addWidget(button6)
hor_layout_for_buttons3.addWidget(plus_button)

hor_layout_for_buttons4.addWidget(button7)
hor_layout_for_buttons4.addWidget(button8)
hor_layout_for_buttons4.addWidget(button9)
hor_layout_for_buttons4.addWidget(minus_button)

hor_layout_for_buttons5.addWidget(button0)
hor_layout_for_buttons5.addWidget(ravn_button)

vert_layout_for_buttons1.addLayout(hor_layout_for_buttons2)
vert_layout_for_buttons1.addLayout(hor_layout_for_buttons3)
vert_layout_for_buttons2.addLayout(hor_layout_for_buttons4)
vert_layout_for_buttons2.addLayout(hor_layout_for_buttons5)

vert_layout_for_buttons3.addLayout(hor_layout_for_buttons5)
vert_layout_for_buttons3.addLayout(hor_layout_for_buttons1)

main_vert_layout.addLayout(vert_layout_for_buttons1)
main_vert_layout.addLayout(vert_layout_for_buttons2)
main_vert_layout.addLayout(vert_layout_for_buttons3)
main_hor_layout = QHBoxLayout()
main_hor_layout.addLayout(main_vert_layout)
main_window.setLayout(main_hor_layout)

main_window.show()
app.exec()
