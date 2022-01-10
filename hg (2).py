import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber, QComboBox, QDialog

from PyQt5.QtGui import *

from PyQt5.QtCore import *

import sqlite3


cords = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
cords += [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

translit = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo", " ": " "}
spt = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
      'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
      'o': '---', 'p':
          '.--.', 'q': '--.-',
      'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
      'y': '-.--', 'z': '--..',
      ' ': ',', '-': '-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
      '5': '.....',
      '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
       'а': '.-', 'б': '-...', 'в': '-.-.', 'г': '-..', 'д': '.', 'е': '..-.',
       'ж': '--.', 'з': '....', 'и': '..', 'к': '.---', 'л': '-.-', 'м': '.-..', 'н': '--',
       'о': '---', 'п':
           '.--.', 'р': '--.-',
       'с': '.-.', 'т': '...', 'у': '-', 'ф': '..-', 'х': '...-', 'ц': '.--', 'ч': '-..-',
       'ш': '-.--', 'щ': '--..',
       'ъ': ' ', 'ы': '-', 'ь': '.----', 'э': '..---', 'ю': '...--', 'я': '....-', 'ё': '.....'}


def decode_from_morse(code):
    global spt
    vuv = ''
    code = code.split(' ')
    for i in code:
        for buk, cod in spt.items():
            if cod == i:
                vuv += buk
                break
    return vuv


def trans(text):
    global translit
    text = list(text.lower())
    tp = ''
    for i in text:
        tp += translit[i]
    return tp


def encode_to_morse(text):
    global spt
    text = list(text.lower())
    tp = ''
    for i in text:
        tp += spt[i] + ' '
    return tp


w = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
        'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
        'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
ee = 0

def encrypt_caesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x) % len(llst)
            ret += llst[(ind + shift) % len(llst)]
        elif x in blst:
            ind = blst.index(x) % len(llst)
            ret += blst[(ind + shift) % len(llst)]
        else:
            ret += x
    return ret


def decrypt_caesar(msg, shift=3):
    ret = ""
    while shift > 32:
        shift -= 32
    while shift < -32:
        shift += 32
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            v = ind - shift
            if ind - shift >= 32:
                v -= 32
            ret += llst[v]
        elif x in blst:
            ind = blst.index(x)
            v = ind - shift
            if ind - shift >= 32:
                v -= 32
            ret += blst[v]
        else:
            ret += x
    return ret


class Gaed(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 320, 300)
        self.setWindowTitle('Фокус со словами')
        but = QPushButton(self)
        but.move(0, 0)
        but.setIcon(QIcon('obues.png'))
        but.setIconSize(QSize(320, 300))


class Zabor(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('Фокус со словами')
        self.zab = QPushButton('Зашифровать', self)
        self.zab.setGeometry(100, 130, 100, 20)
        self.zab.clicked.connect(self.tra)

        self.pole = QLineEdit(self)
        self.pole.setText('')
        self.pole.setGeometry(20, 110, 240, 20)

        self.pole_ = QLineEdit(self)
        self.pole_.setText('')
        self.pole_.setGeometry(20, 150, 240, 20)

    def tra(self):
        g = ''
        y = 0
        for i in list(self.pole.text()):
            if y % 2 == 0:
                g += i.upper()
            else:
                g += i.lower()
            y += 1

        self.pole_.setText(g)


class Cheture(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('Фокус со словами')
        self.zab = QPushButton('Зашифровать', self)
        self.zab.setGeometry(100, 130, 100, 20)
        self.zab.clicked.connect(self.tra)

        self.pole = QLineEdit(self)
        self.pole.setText('')
        self.pole.setGeometry(20, 110, 240, 20)

        self.pole_ = QLineEdit(self)
        self.pole_.setText('')
        self.pole_.setGeometry(20, 150, 240, 20)

    def tra(self):
        g = []
        y = True
        for i in self.pole.text().split():
            i = list(i)
            while y:
                if 'ч' in i:
                    i[i.index('ч')] = '4'
                    continue
                elif 'i' in i:
                    i[i.index('i')] = '1'
                    continue
                y = False
            print(123)
            i = ''.join(i)
            g.append(i)
        self.pole_.setText(' '.join(g))



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('Фокус со словами')
        p = 50
        buter = QPushButton(self)
        buter.move(-10, -80)
        buter.setIcon(QIcon('yep.jpg'))
        buter.setIconSize(QSize(580, 440))

        but = QPushButton(self)
        but.move(290, 272)
        but.setIcon(QIcon('Без имени-1.png'))
        but.setIconSize(QSize(20, 20))
        but.clicked.connect(self.obs)


        self.combo = QComboBox(self)
        self.combo.addItem('МОРЗЕ')
        self.combo.addItem('ЦЕЗАРЬ RUS')
        self.combo.addItem('ЦЕЗАРЬ ENG')
        self.combo.addItem('ТРанслитерация')
        self.combo.setGeometry(10, 10, 100, 20)
        self.combo.setStyleSheet("color: #ffffff;""background-color: #004725;"
                                 "selection-color: #00000;""selection-background-color: #004725;")

        self.pol3e_vvoda = QLineEdit(self)
        self.pol3e_vvoda.setText('')
        self.pol3e_vvoda.setGeometry(20, 110, 240, 20)

        self.CEqZ = QLineEdit(self)
        self.CEqZ.setText('')
        self.CEqZ.setGeometry(280, 110, 20, 20)
        self.CEqZ.hide()

        self.perecl = QPushButton('переключить', self)
        self.perecl.setGeometry(10, 30, 100, 20)
        self.perecl.clicked.connect(self.pereclfunc)

        for y in range(26):
            self.btn = QPushButton(w[y], self)
            self.btn.setGeometry(cords[y], p, 20, 20)
            if y == 12:
                p = 70
            self.btn.clicked.connect(self.hello)
            self.btn.setStyleSheet("color: #ffffff;""background-color: #004725;"
                                 "selection-color: #ffffff;""selection-background-color: #004725;")

        self.mor = QPushButton('Зашифровать', self)
        self.mor.setGeometry(100, 130, 100, 20)
        self.mor.clicked.connect(self.shifmorze)
        self.mordecod = QPushButton('Deшифровать', self)
        self.mordecod.setGeometry(200, 130, 100, 20)
        self.mordecod.clicked.connect(self.deshifmorze)
        self.chiz = QPushButton('Зашифровать', self)
        self.chiz.setGeometry(100, 130, 100, 20)
        self.chiz.clicked.connect(self.rus)
        self.chiz.hide()
        self.chizdecod = QPushButton('Deшифровать', self)
        self.chizdecod.setGeometry(200, 130, 100, 20)
        self.chizdecod.clicked.connect(self.deshifchiz)
        self.chizdecod.hide()
        self.AUD = QPushButton('Зашифровать', self)
        self.AUD.setGeometry(100, 130, 100, 20)
        self.AUD.clicked.connect(self.eng)
        self.AUD.hide()
        self.AUDdecod = QPushButton('Deшифровать', self)
        self.AUDdecod.setGeometry(200, 130, 100, 20)
        self.AUDdecod.clicked.connect(self.deshifchie)
        self.AUDdecod.hide()
        self.tranc = QPushButton('Зашифровать', self)
        self.tranc.setGeometry(100, 130, 100, 20)
        self.tranc.clicked.connect(self.tranclit)
        self.tranc.hide()

        self.pole_vvoda = QLineEdit(self)
        self.pole_vvoda.setText('')
        self.pole_vvoda.setGeometry(20, 110, 240, 20)

        self.CEZ = QLineEdit(self)
        self.CEZ.setText('')
        self.CEZ.setGeometry(280, 110, 20, 20)
        self.CEZ.hide()

        self.pole_vuvoda = QLineEdit(self)
        self.pole_vuvoda.setText('')
        self.pole_vuvoda.setGeometry(20, 150, 240, 20)
        self.opis = QLabel()
        self.opis.setGeometry(20, 180, 240, 30)
        self.opis.setText('В Верхнее поле вводить текст который нужно зашифровать')

    def hello(self):
        self.pole_vvoda.setText(str(self.pole_vvoda.text()) + str(self.btn.sender().text()))

    def pashalki(self):
        con = sqlite3.connect('pas.db')

        # Создание курсора
        cur = con.cursor()
        vvedeno = self.pole_vvoda.text()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("SELECT nujnuyCod FROM RodoRolaaa WHERE soob=?", (str(vvedeno), )).fetchall()
        print(vvedeno)
        if bool(result):
            print(1)
            if result[0][0] == 1:
                di = Zabor()
                di.exec_()
            elif result[0][0] == 2:
                dial = Cheture()
                dial.exec_()
            else:
                self.pole_vuvoda.setText(result[0][0])


    def obs(self):
        dialog = Gaed()
        dialog.exec_()

    def shifmorze(self):
        self.pole_vuvoda.setText(encode_to_morse(self.pole_vvoda.text()))
        self.pashalki()

    def deshifmorze(self):
        self.pole_vuvoda.setText(decode_from_morse(self.pole_vvoda.text()))

    def rus(self):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        msg = list(self.pole_vvoda.text().lower())
        if self.CEZ.text() != '':
            shift = int(self.CEZ.text())
        else:
            shift = 3
        ret = ""
        for x in msg:
            if x in llst:
                ind = llst.index(x) % len(llst)
                ret += llst[(ind + shift) % len(llst)]
            elif x in blst:
                ind = blst.index(x) % len(llst)
                ret += blst[(ind + shift) % len(llst)]
            else:
                ret += x
        self.pole_vuvoda.setText(ret)
        self.pashalki()

    def deshifchiz(self):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        msg = list(self.pole_vvoda.text().lower())
        if self.CEZ.text() != '':
            shift = int(self.CEZ.text()) * -1
        else:
            shift = -3
        ret = ""
        print(1)
        for x in msg:
            if x in llst:
                ind = llst.index(x) % len(llst)
                ret += llst[(ind + shift) % len(llst)]
            elif x in blst:
                ind = blst.index(x) % len(llst)
                ret += blst[(ind + shift) % len(llst)]
            else:
                ret += x
        self.pole_vuvoda.setText(ret)

    def eng(self):
        llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        blst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        msg = list(self.pole_vvoda.text().lower())
        if self.CEZ.text() != '':
            shift = int(self.CEZ.text())
        else:
            shift = 3
        ret = ""
        for x in msg:
            if x in llst:
                ind = llst.index(x) % len(llst)
                ret += llst[(ind + shift) % len(llst)]
            elif x in blst:
                ind = blst.index(x) % len(llst)
                ret += blst[(ind + shift) % len(llst)]
            else:
                ret += x
        self.pole_vuvoda.setText(ret)
        self.pashalki()

    def deshifchie(self):
        llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        blst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        msg = list(self.pole_vvoda.text().lower())
        if self.CEZ.text() != '':
            shift = -int(self.CEZ.text())
        else:
            shift = -3
        ret = ""
        for x in msg:
            if x in llst:
                ind = llst.index(x) % len(llst)
                ret += llst[(ind + shift) % len(llst)]
            elif x in blst:
                ind = blst.index(x) % len(llst)
                ret += blst[(ind + shift) % len(llst)]
            else:
                ret += x
        self.pole_vuvoda.setText(ret)

    def tranclit(self):
        self.pole_vuvoda.setText(trans(self.pole_vvoda.text()))
        self.pashalki()

    def pereclfunc(self):
        if self.combo.currentText() == 'МОРЗЕ':
            self.CEZ.hide()
            self.mor.show()
            self.chiz.hide()
            self.AUD.hide()
            self.mordecod.show()
            self.chizdecod.hide()
            self.AUDdecod.hide()
            self.tranc.hide()
        elif self.combo.currentText() == 'ЦЕЗАРЬ RUS':
            self.CEZ.show()
            self.mor.hide()
            self.chiz.show()
            self.AUD.hide()
            self.mordecod.hide()
            self.chizdecod.show()
            self.AUDdecod.hide()
            self.tranc.hide()
        elif self.combo.currentText() == 'ЦЕЗАРЬ ENG':
            self.CEZ.show()
            self.mor.hide()
            self.chiz.hide()
            self.AUD.show()
            self.mordecod.hide()
            self.chizdecod.hide()
            self.AUDdecod.show()
            self.tranc.hide()
        else:
            self.CEZ.hide()
            self.mor.hide()
            self.chiz.hide()
            self.AUD.show()
            self.mordecod.hide()
            self.chizdecod.hide()
            self.AUDdecod.hide()
            self.tranc.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())