from PyQt5 . QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit





menu_btn2 = QPushButton('Меню')



question2 = QLabel('для вопроса')

otvet = QLineEdit()
otvet.setPlaceholderText('Відповідь тут')

okey2_btn = QPushButton('Відповісти')



layout1 = QVBoxLayout()
#layout1.addWidget(picture2)
layout1.addWidget(question2, alignment = Qt.AlignCenter)
layout1.addWidget(otvet)

layout1.addWidget(okey2_btn)

