# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DCLSUItest_third.ui'
#
# Created: Fri Nov 25 17:43:16 2022
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(819, 504)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(110, 420, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_3RMS1 = QtGui.QLineEdit(Form)
        self.lineEdit_3RMS1.setGeometry(QtCore.QRect(160, 420, 51, 20))
        self.lineEdit_3RMS1.setObjectName(_fromUtf8("lineEdit_3RMS1"))
        self.lineEdit_3RMS2 = QtGui.QLineEdit(Form)
        self.lineEdit_3RMS2.setGeometry(QtCore.QRect(320, 419, 51, 20))
        self.lineEdit_3RMS2.setObjectName(_fromUtf8("lineEdit_3RMS2"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(270, 419, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_3RMS4 = QtGui.QLineEdit(Form)
        self.lineEdit_3RMS4.setGeometry(QtCore.QRect(650, 419, 51, 20))
        self.lineEdit_3RMS4.setObjectName(_fromUtf8("lineEdit_3RMS4"))
        self.lineEdit_3RMS3 = QtGui.QLineEdit(Form)
        self.lineEdit_3RMS3.setGeometry(QtCore.QRect(480, 419, 51, 20))
        self.lineEdit_3RMS3.setObjectName(_fromUtf8("lineEdit_3RMS3"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(430, 419, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(600, 419, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_3VS1 = QtGui.QLineEdit(Form)
        self.lineEdit_3VS1.setGeometry(QtCore.QRect(200, 450, 51, 20))
        self.lineEdit_3VS1.setText(_fromUtf8(""))
        self.lineEdit_3VS1.setObjectName(_fromUtf8("lineEdit_3VS1"))
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(110, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(260, 450, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_3VS2 = QtGui.QLineEdit(Form)
        self.lineEdit_3VS2.setGeometry(QtCore.QRect(280, 450, 51, 20))
        self.lineEdit_3VS2.setText(_fromUtf8(""))
        self.lineEdit_3VS2.setObjectName(_fromUtf8("lineEdit_3VS2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 781, 391))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "RMS(%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "RMS(%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "RMS(%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "RMS(%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "V.Sum block", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "~", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Charts", None, QtGui.QApplication.UnicodeUTF8))

