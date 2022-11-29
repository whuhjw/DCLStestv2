# coding=UTF-8
import sys
# from PyQt4.QtGui import QApplication, QMainWindow, QMessageBox
from PyQt4.QtCore import Qt, QCoreApplication, pyqtSignal
# from epics import caget, caput, cainfo
# m1 = caget('XXX:m1.VAL')

from PyQt4 import QtGui
from PyQt4.QtGui import QApplication

# from DCLSUItest import Ui_MainWindow as u1
# from DCLS_second_action import SecondWindow as window2
# from DCLS_third_action import ThirdWindow as window3
# from DCLS_forth_action import ForthWindow as window4

from DCLS_action import MyMainWindow
import qtawesome as qta

if __name__ == '__main__':
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_NativeWindows)
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#pyqt5
    # QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);#QT5
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    myWin.setWindowIcon(qta.icon('fa5s.store', color='grey'))
    # 将UI对话框对应声明的窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 当点击窗口的x时，退出程序
