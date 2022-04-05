import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow
from typing import Union, Optional
from operator import truediv,sub,add,mul

operations={
    '+':add,
    '-':sub,
    'x':mul,
    '/':truediv
}

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #digits
        self.ui.b0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.b1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.b2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.b3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.b4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.b5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.b6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.b7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.b8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.b9.clicked.connect(lambda: self.add_digit('9'))

        #actions
        self.ui.bC.clicked.connect(self.clear_all)
        self.ui.bCE.clicked.connect(self.clear_entry)
        self.ui.point.clicked.connect(self.add_point)

        #math
        self.ui.plus.clicked.connect(lambda:self.add_temp('+'))
        self.ui.divide.clicked.connect(lambda: self.add_temp('/'))
        self.ui.minus.clicked.connect(lambda: self.add_temp('-'))
        self.ui.multiply.clicked.connect(lambda: self.add_temp('x'))
        self.ui.equal.clicked.connect(self.calculate)


    def add_digit(self,btn_text: str)->None:
        if self.ui.line.text()=='0':
            self.ui.line.setText(btn_text)
        else:
            self.ui.line.setText(self.ui.line.text()+btn_text)

    def add_point(self)->None:
        if '.' not in self.ui.line.text():
            self.ui.line.setText(self.ui.line.text()+'.')

    def add_temp(self,math_sign:str)->None:
        if not self.ui.label.text() or self.get_math_sign()=='=':
            self.ui.label.setText(self.remove_trailing_zeros(self.ui.line.text())+f' {math_sign} ')
            self.ui.line.setText('0')

    def get_entry_num(self)->Union[int,float]:
        entry=self.ui.line.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self)->Union[int,float,None]:
        if self.ui.label.text():
            temp=self.ui.label.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self)->Optional[str]:
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def clear_all(self)->None:
        self.ui.line.setText('0')
        self.ui.label.clear()

    def calculate(self)->Optional[str]:
        entry=self.ui.line.text()
        temp=self.ui.label.text()
        if temp:
            result=self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(),self.get_entry_num()))
            )
            self.ui.label.setText(temp+self.remove_trailing_zeros(entry)+'=')
            self.ui.line.setText(result)
            return result

    def math_operation(self,math_sign:str):
        temp=self.ui.label.text()
        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign()!=math_sign:
                if self.get_math_sign()=='=':
                    self.add_temp(math_sign)
                else:
                    self.ui.label.setText(temp[:2]+f'{math_sign} ')
            else:
                self.ui.label.setText(self.calculate()+f' {math_sign}')

    def clear_entry(self)->None:
        self.ui.line.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str)->str:
        n=str(float(num))
        return n[:-2] if n[-2:]=='.0' else n

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Calculator()
    window.show()
    sys.exit(app.exec())

