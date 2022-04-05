import sys
from typing import Union, Optional
from PySide6.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow
from operator import add, sub, mul, truediv

operations = {
    '+': add,
    '-': sub,
    'x': mul,
    '/': truediv
}

op=('=','+','-','x','/')

class Calculator(QMainWindow):

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # digits
        self.ui.b0.clicked.connect(self.add_digit)
        self.ui.b1.clicked.connect(self.add_digit)
        self.ui.b2.clicked.connect(self.add_digit)
        self.ui.b3.clicked.connect(self.add_digit)
        self.ui.b4.clicked.connect(self.add_digit)
        self.ui.b5.clicked.connect(self.add_digit)
        self.ui.b6.clicked.connect(self.add_digit)
        self.ui.b7.clicked.connect(self.add_digit)
        self.ui.b8.clicked.connect(self.add_digit)
        self.ui.b9.clicked.connect(self.add_digit)

        self.ui.equal.clicked.connect(self.calculate)
        self.ui.point.clicked.connect(self.add_point)
        self.ui.plus.clicked.connect(self.math_operation)
        self.ui.minus.clicked.connect(self.math_operation)
        self.ui.multiply.clicked.connect(self.math_operation)
        self.ui.divide.clicked.connect(self.math_operation)
        self.ui.pushButton_6.clicked.connect(self.change_sign)

        # actions
        self.ui.backspace.clicked.connect(self.clear_one)
        self.ui.bC.clicked.connect(self.clear_all)
        self.ui.bCE.clicked.connect(self.clear_entry)

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.line.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def change_sign(self):
        if self.ui.line.text()[0]=='-':
            self.ui.line.setText(self.ui.line.text()[1:])
        elif self.ui.line.text()!='0':
            self.ui.line.setText('-'+self.ui.line.text())

        if self.ui.label.text()[-1:] == '=':
            if self.ui.line.text()[0]!='-':
                self.ui.label.setText('-'+self.ui.line.text())
            else:
                self.ui.label.setText(self.ui.line.text()[1:])

    def clear_one(self):
        if self.ui.label.text()[-1:] == '=':
            self.ui.label.setText(self.ui.line.text())
        if self.ui.line.text().__len__()>1:
            self.ui.line.setText(self.ui.line.text()[0:-1])
        elif self.ui.line.text():
            self.ui.line.setText('0')

    def math_operation(self) -> None:
        temp = self.ui.label.text()
        btn = self.sender()

        if not temp and self.get_math_sign() not in op:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                elif self.get_math_sign() not in op:
                    self.ui.label.setText(temp + f' {btn.text()} ')
                else:
                    self.ui.label.setText(temp[:-3] + f' {btn.text()} ')
            else:
                self.ui.label.setText(self.calculate() + f' {btn.text()} ')

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.line.text())


        if not self.ui.label.text() or self.get_math_sign() in op:
            self.ui.label.setText(entry + f' {btn.text()} ')
            self.ui.line.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_point(self) -> None:
        if '.' not in self.ui.line.text():
            self.ui.line.setText(self.ui.line.text() + '.')

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.label.text():
            temp = self.ui.label.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def add_digit(self):
        btn = self.sender()

        digit_buttons = ('b0', 'b1', 'b2', 'b3', 'b4',
                         'b5', 'b6', 'b7', 'b8', 'b9')

        if btn.objectName() in digit_buttons:
            if self.ui.label.text()[-1:]=='=':
                self.ui.label.setText(self.ui.line.text())
            if self.ui.line.text() == '0':
                self.ui.line.setText(btn.text())
            else:
                self.ui.line.setText(self.ui.line.text() + btn.text())



    def calculate(self) -> Optional[str]:
        entry = self.ui.line.text()
        temp = self.ui.label.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num())))
            self.ui.label.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.line.setText(result)
            return result

    def clear_all(self) -> None:
        self.ui.line.setText('0')
        self.ui.label.clear()

    def clear_entry(self) -> None:
        self.ui.line.setText('0')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())