
################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 500)
        MainWindow.setMinimumSize(QSize(338, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/outline_calculate_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 20pt;\n"
"	font-weight: 600;\n"
"	border:none;\n"
"}\n"
"\n"
"QGridLayout {\n"
"	background-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: #888")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.line = QLineEdit(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setCursor(QCursor(Qt.ForbiddenCursor))
        self.line.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.line.setMaxLength(100)
        self.line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line.setReadOnly(True)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.point = QPushButton(self.centralwidget)
        self.point.setObjectName(u"point")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy2)
        self.point.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.point, 4, 2, 1, 1)

        self.bC = QPushButton(self.centralwidget)
        self.bC.setObjectName(u"bC")
        sizePolicy2.setHeightForWidth(self.bC.sizePolicy().hasHeightForWidth())
        self.bC.setSizePolicy(sizePolicy2)
        self.bC.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.bC, 0, 0, 1, 1)

        self.backspace = QPushButton(self.centralwidget)
        self.backspace.setObjectName(u"backspace")
        sizePolicy2.setHeightForWidth(self.backspace.sizePolicy().hasHeightForWidth())
        self.backspace.setSizePolicy(sizePolicy2)
        self.backspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/outline_backspace_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backspace.setIcon(icon1)
        self.backspace.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.backspace, 0, 2, 1, 1)

        self.b8 = QPushButton(self.centralwidget)
        self.b8.setObjectName(u"b8")
        sizePolicy2.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy2)
        self.b8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b8, 3, 1, 1, 1)

        self.b0 = QPushButton(self.centralwidget)
        self.b0.setObjectName(u"b0")
        sizePolicy2.setHeightForWidth(self.b0.sizePolicy().hasHeightForWidth())
        self.b0.setSizePolicy(sizePolicy2)
        self.b0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b0, 4, 1, 1, 1)

        self.bCE = QPushButton(self.centralwidget)
        self.bCE.setObjectName(u"bCE")
        sizePolicy2.setHeightForWidth(self.bCE.sizePolicy().hasHeightForWidth())
        self.bCE.setSizePolicy(sizePolicy2)
        self.bCE.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.bCE, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 1)

        self.b9 = QPushButton(self.centralwidget)
        self.b9.setObjectName(u"b9")
        sizePolicy2.setHeightForWidth(self.b9.sizePolicy().hasHeightForWidth())
        self.b9.setSizePolicy(sizePolicy2)
        self.b9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b9, 3, 2, 1, 1)

        self.b3 = QPushButton(self.centralwidget)
        self.b3.setObjectName(u"b3")
        sizePolicy2.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy2)
        self.b3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b3, 1, 2, 1, 1)

        self.b4 = QPushButton(self.centralwidget)
        self.b4.setObjectName(u"b4")
        sizePolicy2.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy2)
        self.b4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b4, 2, 0, 1, 1)

        self.b1 = QPushButton(self.centralwidget)
        self.b1.setObjectName(u"b1")
        sizePolicy2.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy2)
        self.b1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b1, 1, 0, 1, 1)

        self.b6 = QPushButton(self.centralwidget)
        self.b6.setObjectName(u"b6")
        sizePolicy2.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy2)
        self.b6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b6, 2, 2, 1, 1)

        self.b2 = QPushButton(self.centralwidget)
        self.b2.setObjectName(u"b2")
        sizePolicy2.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy2)
        self.b2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b2, 1, 1, 1, 1)

        self.b5 = QPushButton(self.centralwidget)
        self.b5.setObjectName(u"b5")
        sizePolicy2.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy2)
        self.b5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b5, 2, 1, 1, 1)

        self.b7 = QPushButton(self.centralwidget)
        self.b7.setObjectName(u"b7")
        sizePolicy2.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy2)
        self.b7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.b7, 3, 0, 1, 1)

        self.divide = QPushButton(self.centralwidget)
        self.divide.setObjectName(u"divide")
        sizePolicy2.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy2)
        self.divide.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.divide, 0, 3, 1, 1)

        self.multiply = QPushButton(self.centralwidget)
        self.multiply.setObjectName(u"multiply")
        sizePolicy2.setHeightForWidth(self.multiply.sizePolicy().hasHeightForWidth())
        self.multiply.setSizePolicy(sizePolicy2)
        self.multiply.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.multiply, 1, 3, 1, 1)

        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        sizePolicy2.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy2)
        self.minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.minus, 2, 3, 1, 1)

        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        sizePolicy2.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy2)
        self.plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.plus, 3, 3, 1, 1)

        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        sizePolicy2.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy2)
        self.equal.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.equal, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Calculator", None))
        self.label.setText("")
        self.line.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.bC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.backspace.setText("")
#if QT_CONFIG(shortcut)
        self.backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.b8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.b0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.bCE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.bCE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.b9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.b3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.b4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.b1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.b6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.b2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.b7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.multiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.equal.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

