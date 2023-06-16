from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QGridLayout, QPushButton, QApplication, QWidget, QLCDNumber, QVBoxLayout, QLineEdit
app = QApplication([])
main_win = QWidget()
main_win.setFixedSize(282, 443)
main_win.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
main_win.setWindowTitle('Calculator 3000')
my_grid_LT = QWidget()
my_grid_LT.setGeometry(QRect(10, 95, 260, 340))
my_grid_LT.setObjectName('my_grid_LT')
grid_net = QGridLayout(my_grid_LT)
grid_net.setContentsMargins(0, 0, 0, 0)
grid_net.setObjectName('grid_net')
display = QLineEdit()
display.setGeometry(10, 10, 260, 75)

#=
main_layout = QVBoxLayout()
equal_btn = QPushButton('=')

def numbers():
    try:
        result = eval(display.text())
        display.setText(str(result))
    except:
        display.setText('Error')


def append_number(b):
    display.setText(display.text() + b)

positions = [(i, j, 1, 1) for i in range(4) for j in range(4)]
titles = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '.', 'C', '/'
]

for position, btn_name in zip(positions, titles):
    if btn_name == 'C':
        btn = QPushButton(btn_name)
        grid_net.addWidget(btn, *position)
        size = 60
        btn.setMaximumSize(size, size)
        btn.setMinimumSize(size, size)
        btn.clicked.connect(display.clear)
    else:
        btn = QPushButton(btn_name)
        btn.clicked.connect(lambda x, b=btn_name: append_number(b))
        grid_net.addWidget(btn, *position)
        size = 60
        btn.setMaximumSize(size, size)
        btn.setMinimumSize(size, size)
        grid_net.addWidget(btn, *position)
        btn.setText(btn_name)
equal_btn.clicked.connect(numbers)
main_layout.addWidget(display)
main_layout.addWidget(my_grid_LT)
main_layout.addWidget(equal_btn)
main_win.setLayout(main_layout)

main_win.show()
app.exec_()