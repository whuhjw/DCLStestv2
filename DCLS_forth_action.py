# coding=UTF-8
import sys
import random
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QApplication, QSizePolicy
from DCLSUItest_forth import Ui_Form as u4
import sys
import matplotlib
# matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas # matplotlib对PyQt4的支持
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)# add_subplot添加一个绘图区作为子图排列的一部分，网格“111”表示“1x1 网格，第一个子图
        super(MplCanvas, self).__init__(fig)

class ForthWindow(QtGui.QMainWindow, u4):
    def __init__(self):
        super(ForthWindow, self).__init__()
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        # 创建 maptlotlib FigureCanvas 对象,
        # 绘制二维坐标轴.
        self.canvas = MplCanvas(self, width=4, height=3, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self._plot_ref = None
        self.update_plot()
        self.show()

        # 通过调用 update_plot 设置定时器进行定时重绘.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # 移除y的一个数据, 添加一个新的数据.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        # 注意: 不需要清除y的数据.
        if self._plot_ref is None:
            # 第一次进来self._plotref是None（即没有画线）
            # 然后画线并赋值给self._plot_refx
            # plot返回的是一个包含一个线条的列表
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'r')
            self._plot_ref = plot_refs[0]
        else:
            # 通过设置更新Y self._plot_ref.set_ydata(self.ydata)
            self._plot_ref.set_ydata(self.ydata)
        # self.canvas.axes.cla()  # Clear the canvas.
        # self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas.axes.set_xlabel("Time")
        self.canvas.axes.set_ylabel("Amp")
        # 触发画布更新和重绘.
        self.canvas.draw()







