import random

from PyQt5.QtWidgets import  *
app = QApplication([])

window = QWidget()
window.resize(500,500)

lbl = QLabel("Вікторина")
numberlbl= QLabel ("Номер переможця")
star8th = QPushButton("Дізнатися переможця")


main_line = QHBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(numberlbl)
main_line.addWidget(star8th)

window.setLayout(main_line)

def bannana():
    a = random.randint (1,10)
    numberlbl.setText(str(a))

star8th.clicked.connect(bannana)
window.show()
app.exec()


