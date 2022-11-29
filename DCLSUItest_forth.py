# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DCLSUItest_forth.ui'
#
# Created: Wed Nov 23 22:33:01 2022
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
        Form.resize(745, 518)
        self.label_20 = QtGui.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(350, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "Amp", None, QtGui.QApplication.UnicodeUTF8))

