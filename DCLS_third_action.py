# coding=UTF-8
import sys
import random
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QApplication, QSizePolicy, QGridLayout
from DCLSUItest_third import Ui_Form as u3
import sys
import matplotlib as ply
# ply.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas # matplotlib对PyQt4的支持
import numpy as np


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=2, height=1, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = self.fig.add_subplot(241)
        self.axes2 = self.fig.add_subplot(242)
        self.axes3 = self.fig.add_subplot(243)
        self.axes4 = self.fig.add_subplot(244)
        self.axes5 = self.fig.add_subplot(245)
        self.axes6 = self.fig.add_subplot(246)
        self.axes7 = self.fig.add_subplot(247)
        self.axes8 = self.fig.add_subplot(248)
        # print(vars(self.fig.subplotpars))
        self.fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.7)
        super(MplCanvas, self).__init__(self.fig)


class ThirdWindow(QtGui.QMainWindow, u3):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        self.lineEdit_3RMS1.setEnabled(False)
        self.lineEdit_3RMS2.setEnabled(False)
        self.lineEdit_3RMS3.setEnabled(False)
        self.lineEdit_3RMS4.setEnabled(False)
        self.lineEdit_3VS1.setEnabled(False)
        self.lineEdit_3VS2.setEnabled(False)

        self.setWindowTitle("Chart Detail")
        # 创建 maptlotlib FigureCanvas 对象,
        # 绘制二维坐标轴.
        self.canvas = MplCanvas(self, width=2, height=1, dpi=100)
        self.setCentralWidget(self.canvas)
        # 在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.canvas)

        # caget 获取数据
        n_data = 50
        self.xdata1 = list(range(n_data))
        self.ydata1 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref1 = None

        self.xdata2 = list(range(n_data))
        self.ydata2 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref2 = None

        self.xdata3 = list(range(n_data))
        self.ydata3 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref3 = None

        self.xdata4= list(range(n_data))
        self.ydata4 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref4 = None

        self.xdata5 = list(range(n_data))
        self.ydata5 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref5 = None

        self.xdata6 = list(range(n_data))
        self.ydata6 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref6 = None

        self.xdata7 = list(range(n_data))
        self.ydata7 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref7 = None

        self.xdata8 = list(range(n_data))
        self.ydata8 = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref8 = None

        self.update_plot1()
        self.update_plot2()
        self.update_plot3()
        self.update_plot4()
        self.update_plot5()
        self.update_plot6()
        self.update_plot7()
        self.update_plot8()

        # 通过调用 update_plot 设置定时器进行定时重绘.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot1)
        self.timer.timeout.connect(self.update_plot2)
        self.timer.timeout.connect(self.update_plot3)
        self.timer.timeout.connect(self.update_plot4)
        self.timer.timeout.connect(self.update_plot5)
        self.timer.timeout.connect(self.update_plot6)
        self.timer.timeout.connect(self.update_plot7)
        self.timer.timeout.connect(self.update_plot8)
        self.timer.start()
    # def get_3VS_left(self):
    #     VS_left_set=int(self.lineEdit_3VS1.text())
    #     print(VS_left_set)
    #     #caput
    #     return
    # def get_3VS_right(self):
    #     VS_right_set=int(self.lineEdit_3VS2.text())
    #     print(VS_right_set)
    #     #caput
    #     return
    def update_plot1(self):
        # print(self.ydata1)
        # 移除y的一个数据, 添加一个新的数据.
        self.ydata1 = self.ydata1[1:] + [random.randint(0, 10)]
        # print(self.ydata1)
        # 注意: 不需要清除y的数据.
        if self._plot_ref1 is None:
            # 第一次进来self._plotref是None（即没有画线）
            # 然后画线并赋值给self._plot_refx
            # plot返回的是一个包含一个线条的列表
            # print(self.ydata1)
            plot_refs1 = self.canvas.axes1.plot(self.xdata1, self.ydata1, 'r')
            self._plot_ref1 = plot_refs1[0]
            # print(plot_refs1[0])
        else:
            # 通过设置更新Y self._plot_ref.set_ydata(self.ydata)
            self._plot_ref1.set_ydata(self.ydata1)
            # print(self.ydata1)
        self.canvas.axes1.set_title("IQ1")
        # print(self.ydata1)
        # 触发画布更新和重绘.
        self.canvas.draw()
    def update_plot2(self):
        self.ydata2 = self.ydata2[1:] + [random.randint(0, 10)]
        if self._plot_ref2 is None:
            plot_refs2 = self.canvas.axes2.plot(self.xdata2, self.ydata2, 'r')
            self._plot_ref2 = plot_refs2[0]
        else:
            self._plot_ref2.set_ydata(self.ydata2)
        self.canvas.axes2.set_title("IQ2")
        self.canvas.draw()
    def update_plot3(self):
        self.ydata3 = self.ydata3[1:] + [random.randint(0, 10)]
        if self._plot_ref3 is None:
            plot_refs3 = self.canvas.axes3.plot(self.xdata3, self.ydata3, 'r')
            self._plot_ref3 = plot_refs3[0]
        else:
            self._plot_ref3.set_ydata(self.ydata3)
        self.canvas.axes3.set_title("Amp")
        self.canvas.draw()
    def update_plot4(self):
        self.ydata4 = self.ydata3[1:] + [random.randint(0, 10)]
        if self._plot_ref4 is None:
            plot_refs4 = self.canvas.axes4.plot(self.xdata4, self.ydata4, 'r')
            self._plot_ref4 = plot_refs4[0]
        else:
            self._plot_ref4.set_ydata(self.ydata4)
        self.canvas.axes4.set_title("Phase")
        self.canvas.draw()
    def update_plot5(self):
        self.ydata5 = self.ydata5[1:] + [random.randint(0, 10)]
        if self._plot_ref5 is None:
            plot_refs5 = self.canvas.axes5.plot(self.xdata5, self.ydata5, 'r')
            self._plot_ref5 = plot_refs5[0]
        else:
            self._plot_ref5.set_ydata(self.ydata5)
        self.canvas.axes5.set_title("Vector Sum Amp")
        self.canvas.draw()
    def update_plot6(self):
        self.ydata6 = self.ydata6[1:] + [random.randint(0, 10)]
        if self._plot_ref6 is None:
            plot_refs6 = self.canvas.axes6.plot(self.xdata6, self.ydata6, 'r')
            self._plot_ref6 = plot_refs6[0]
        else:
            self._plot_ref6.set_ydata(self.ydata6)
        self.canvas.axes6.set_title("Vector Sum Phase")
        self.canvas.draw()
    def update_plot7(self):
        self.ydata7= self.ydata7[1:] + [random.randint(0, 10)]
        if self._plot_ref7 is None:
            plot_refs7 = self.canvas.axes7.plot(self.xdata7, self.ydata7, 'r')
            self._plot_ref7 = plot_refs7[0]
        else:
            self._plot_ref7.set_ydata(self.ydata7)
        self.canvas.axes7.set_title("Amp point")
        self.canvas.draw()
    def update_plot8(self):
        self.ydata8 = self.ydata8[1:] + [random.randint(0, 10)]
        if self._plot_ref8 is None:
            plot_refs8 = self.canvas.axes8.plot(self.xdata8, self.ydata8, 'r')
            self._plot_ref8 = plot_refs8[0]
        else:
            self._plot_ref8.set_ydata(self.ydata8)
        self.canvas.axes8.set_title("Phase point")
        self.canvas.draw()