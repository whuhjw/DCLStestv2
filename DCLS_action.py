# coding=UTF-8
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication
from DCLSUItest import Ui_MainWindow as u1
from DCLS_second_action import SecondWindow as window2
from DCLS_second_actionv2 import SecondWindowv2 as window2v2
from DCLS_third_action import ThirdWindow as window3
from DCLS_forth_action import ForthWindow as window4
import qtawesome as qta
from algorithm import Algorithm_result
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MyMainWindow(QtGui.QMainWindow, u1):
    def __init__(self, parent=None):
        # 初始化父类
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        self.result1 = Algorithm_result()
        Feed_forward_status = 0
        Oddeven_status = 0
        self.llrf_status = 0
        self.trigger_status = 0
        self.Oddeven_status = 0
        self.Feed_forward_status = 0
        # 设置偶法禁止编辑
        self.lineEdit_amp2set.setEnabled(False)
        self.lineEdit_amp2act.setEnabled(False)
        self.lineEdit_pha2set.setEnabled(False)
        self.lineEdit_pha2act.setEnabled(False)
        self.lineEdit_vm_pw2.setEnabled(False)
        self.lineEdit_vm_pha2.setEnabled(False)
        self.lineEdit_ssa_pw2.setEnabled(False)
        self.lineEdit_ssa_pha2.setEnabled(False)
        self.lineEdit_kly_pw2.setEnabled(False)
        self.lineEdit_kly_pha2.setEnabled(False)
        self.lineEdit_defl_pw2.setEnabled(False)
        self.lineEdit_defl_pha2.setEnabled(False)
        self.lineEdit_load_pw2.setEnabled(False)
        self.lineEdit_load_pha2.setEnabled(False)
        self.lineEdit_amp1act.setEnabled(False)
        self.lineEdit_pha1act.setEnabled(False)
        self.lineEdit_pha2set.setEnabled(False)
        self.lineEdit_refl_pwlimitact.setEnabled(False)
        self.lineEdit_ref_pw.setEnabled(False)
        self.lineEdit_ref_pha.setEnabled(False)
        self.lineEdit_vm_pw1.setEnabled(False)
        self.lineEdit_vm_pha1.setEnabled(False)
        self.lineEdit_ssa_pw1.setEnabled(False)
        self.lineEdit_ssa_pha1.setEnabled(False)
        self.lineEdit_kly_pw1.setEnabled(False)
        self.lineEdit_kly_pha1.setEnabled(False)
        self.lineEdit_defl_pw1.setEnabled(False)
        self.lineEdit_defl_pha1.setEnabled(False)
        self.lineEdit_refl_pw.setEnabled(False)
        self.lineEdit_load_pw1.setEnabled(False)
        self.lineEdit_load_pha1.setEnabled(False)

    # 显示第二窗口的函数(与DCLSUItest_second.py 中自动生成的相应的main函数中的内容一致)
    def popWindow2(self):
        if(self.lineEdit_amp1act.text()=="" or self.lineEdit_pha1act.text()=="" or self.lineEdit_refl_pwlimitact.text()==""):
            box = QtGui.QMessageBox()
            box.warning(self, "ERROR", "Please Input Amp, Phase And Limit Parameters!")
        else:
            self.myWin2.show()

        return
    def popWindow2v2(self):
        if (
                self.lineEdit_amp1act.text() == "" or self.lineEdit_pha1act.text() == "" or self.lineEdit_refl_pwlimitact.text() == ""):
            box = QtGui.QMessageBox()
            box.warning(self, "ERROR", "Please Input Amp, Phase And Limit Parameters!")
        else:

            self.myWin2v2.show()
        return
    def popWindow3(self):
        self.myWin3 = window3()
        self.myWin3.setWindowIcon(qta.icon('fa.picture-o', color='grey'))
        self.myWin3.show()
        return
    def popWindow4(self):
        self.myWin4 = window4()
        self.myWin4.setWindowIcon(qta.icon('fa.file-picture-o', color='grey'))
        self.myWin4.show()
        return

    #数据交互处理逻辑函数
    def get_Amp1(self):
        amp1_set = float(self.lineEdit_amp1set.text())  # 获取lineedit中的值
        # caput
        # 回读值显示
        # caget
        amp1_actual = amp1_set
        self.lineEdit_amp1act.setText(str(amp1_actual))
        # IQ_WP = self.lineEdit_amp1act.text()
        # self.myWin2 = window2(IQ_WP)
        return
    def get_Amp2(self):
        amp2_set = float(self.lineEdit_amp2set.text())  # 获取lineedit中的值
        # caput
        # 回读值显示
        # caget
        amp2_actual = amp2_set
        self.lineEdit_amp2act.setText(str(amp2_actual))
        return
    def get_Pha1(self):
        pha1_set = float(self.lineEdit_pha1set.text())  # 获取lineedit中的值
        # caput
        # 回读值显示
        # caget
        pha1_actual = pha1_set
        self.lineEdit_pha1act.setText(str(pha1_actual))
        SP_Phase1=self.lineEdit_pha1act.text()
        IQ_WP = self.lineEdit_amp1act.text()
        self.myWin2 = window2(IQ_WP,SP_Phase1)
        self.myWin2v2 = window2v2(IQ_WP,SP_Phase1)
        self.myWin2v2.setWindowIcon(qta.icon('fa.comment-o', color='grey'))
        return
    def get_Pha2(self):
        pha2_set = float(self.lineEdit_pha2set.text())  # 获取lineedit中的值
        # caput
        # 回读值显示
        # caget
        pha2_actual = pha2_set
        self.lineEdit_pha2act.setText(str(pha2_actual))
        return
    def get_Refl_pwlimit(self):
        refl_pwlimit_set = float(self.lineEdit_refl_pwlimitset.text())  # 获取lineedit中的值
        # caput
        # 回读值显示
        # caget
        refl_pwlimit_actual = refl_pwlimit_set
        self.lineEdit_refl_pwlimitact.setText(str(refl_pwlimit_actual))
        return
    def llrf_start(self):
        if(self.llrf_status==0):
            self.llrf_status = 1

            self.label_start.setStyleSheet(_fromUtf8("background-color: rgb(35, 255, 0);\n"
                                                 "min-width:     16px;\n"
                                                 "min-height:    16px;    \n"
                                                 "max-width:     16px;    \n"
                                                 "max-height:    16px;    \n"
                                                 "border-radius: 8px;    "))
        else:
            self.llrf_status = 0

            self.label_start.setStyleSheet(_fromUtf8("background-color: rgb(181, 181, 181);\n"
                                                     "min-width:     16px;\n"
                                                     "min-height:    16px;    \n"
                                                     "max-width:     16px;    \n"
                                                     "max-height:    16px;    \n"
                                                     "border-radius: 8px;    "))
        # caput self.llrf_status
        return
    def trigger_start(self):
        if(self.llrf_status == 1):
            if (self.trigger_status == 0):
                self.trigger_status = 1
                self.label_enable.setStyleSheet(_fromUtf8("background-color: rgb(35, 255, 0);\n"
                                                          "min-width:     16px;\n"
                                                          "min-height:    16px;    \n"
                                                          "max-width:     16px;    \n"
                                                          "max-height:    16px;    \n"
                                                          "border-radius: 8px;    "))
                # ADC读数显示
                # 初始化
                list_ampnumber = np.arange(7, dtype='f')
                list_ampnumber[0] = float(self.myWin2v2.lineEdit_AC_VMact.text())
                list_ampnumber[1] = float(self.myWin2v2.lineEdit_AC_Refact.text())
                list_ampnumber[2] = float(self.myWin2v2.lineEdit_AC_SSAact.text())
                list_ampnumber[3] = float(self.myWin2v2.lineEdit_AC_Klyact.text())
                list_ampnumber[4] = float(self.myWin2v2.lineEdit_AC_Deflact.text())
                list_ampnumber[5] = float(self.myWin2v2.lineEdit_AC_loadact.text())
                list_ampnumber[6] = float(self.myWin2v2.lineEdit_AC_Klyreact.text())
                amp_list=self.result1.Amp_display(list_ampnumber)

                list_phanumber = np.arange(6, dtype='f')
                list_phanumber[0] = float(self.myWin2v2.lineEdit_PC_VMact.text())
                list_phanumber[1] = float(self.myWin2v2.lineEdit_PC_Refact.text())
                list_phanumber[2] = float(self.myWin2v2.lineEdit_PC_SSAact.text())
                list_phanumber[3] = float(self.myWin2v2.lineEdit_PC_Klyact.text())
                list_phanumber[4] = float(self.myWin2v2.lineEdit_PC_Deflact.text())
                list_phanumber[5] = float(self.myWin2v2.lineEdit_PC_loadact.text())
                pha_list = self.result1.Pha_display(list_phanumber)
                # 一级界面回读值显示
                # caget
                ref_pw = amp_list[1]
                self.lineEdit_ref_pw.setText(str(ref_pw))
                # caget
                ref_pha = pha_list[1]
                self.lineEdit_ref_pha.setText(str(ref_pha))
                # vm输出
                vm_pw1 = amp_list[0]
                self.lineEdit_vm_pw1.setText(str(vm_pw1))
                vm_pw2 = amp_list[7]
                self.lineEdit_vm_pw2.setText(str(vm_pw2))
                vm_pha1 = pha_list[0]
                self.lineEdit_vm_pha1.setText(str(vm_pha1))
                vm_pha2 = pha_list[6]
                self.lineEdit_vm_pha2.setText(str(vm_pha2))
                # SSA输出
                ssa_pw1 = amp_list[2]
                self.lineEdit_ssa_pw1.setText(str(ssa_pw1))
                ssa_pw2 = amp_list[8]
                self.lineEdit_ssa_pw2.setText(str(ssa_pw2))
                ssa_pha1 = pha_list[2]
                self.lineEdit_ssa_pha1.setText(str(ssa_pha1))
                ssa_pha2 = pha_list[7]
                self.lineEdit_ssa_pha2.setText(str(ssa_pha2))
                # KLY输出
                kly_pw1 = amp_list[3]
                self.lineEdit_kly_pw1.setText(str(kly_pw1))
                kly_pw2 = amp_list[9]
                self.lineEdit_kly_pw2.setText(str(kly_pw2))
                kly_pha1 = pha_list[3]
                self.lineEdit_kly_pha1.setText(str(kly_pha1))
                kly_pha2 = pha_list[8]
                self.lineEdit_kly_pha2.setText(str(kly_pha2))
                # 腔前向输入defl
                defl_pw1 = amp_list[4]
                self.lineEdit_defl_pw1.setText(str(defl_pw1))
                defl_pw2 = amp_list[10]
                self.lineEdit_defl_pw2.setText(str(defl_pw2))
                defl_pha1 = pha_list[4]
                self.lineEdit_defl_pha1.setText(str(defl_pha1))
                defl_pha2 = pha_list[9]
                self.lineEdit_defl_pha2.setText(str(defl_pha2))
                # 负载load
                # caget
                load_pw1 = amp_list[5]
                self.lineEdit_load_pw1.setText(str(load_pw1))
                load_pw2 = amp_list[11]
                self.lineEdit_load_pw2.setText(str(load_pw2))
                load_pha1 = pha_list[5]
                self.lineEdit_load_pha1.setText(str(load_pha1))
                load_pha2 = pha_list[10]
                self.lineEdit_load_pha2.setText(str(load_pha2))

                # 反射refl
                refl_pw1 = amp_list[6]
                self.lineEdit_refl_pw.setText(str(refl_pw1))
            else:
                self.trigger_status = 0
                self.label_enable.setStyleSheet(_fromUtf8("background-color: rgb(181, 181, 181);\n"
                                                          "min-width:     16px;\n"
                                                          "min-height:    16px;    \n"
                                                          "max-width:     16px;    \n"
                                                          "max-height:    16px;    \n"
                                                          "border-radius: 8px;    "))
                # 一级界面回读值显示
                # caget
                self.lineEdit_ref_pw.setText('')
                # caget
                self.lineEdit_ref_pha.setText('')
                # vm输出
                # caget
                self.lineEdit_vm_pw1.setText('')
                # caget
                self.lineEdit_vm_pw2.setText('')
                # caget
                self.lineEdit_vm_pha1.setText('')
                # caget
                self.lineEdit_vm_pha2.setText('')
                # SSA输出
                # caget
                self.lineEdit_ssa_pw1.setText('')
                # caget
                self.lineEdit_ssa_pw2.setText('')
                # caget
                self.lineEdit_ssa_pha1.setText('')
                # caget
                self.lineEdit_ssa_pha2.setText('')
                # KLY输出
                # caget
                self.lineEdit_kly_pw1.setText('')
                # caget
                self.lineEdit_kly_pw2.setText('')
                # caget
                self.lineEdit_kly_pha1.setText('')
                # caget
                self.lineEdit_kly_pha2.setText('')
                # 腔前向输入defl
                # caget
                self.lineEdit_defl_pw1.setText('')
                # caget
                self.lineEdit_defl_pw2.setText('')
                # caget
                self.lineEdit_defl_pha1.setText('')
                # caget
                self.lineEdit_defl_pha2.setText('')
                # 负载load
                # caget
                self.lineEdit_load_pw1.setText('')
                # caget
                self.lineEdit_load_pw2.setText('')
                # caget
                self.lineEdit_load_pha1.setText('')
                # caget
                self.lineEdit_load_pha2.setText('')
                # 反射refl
                # caget
                self.lineEdit_refl_pw.setText('')
            # caput self.trigger_status
        else:
            box = QtGui.QMessageBox()
            box.warning(self, "ERROR", "Please Click Start First!")
        return
    def Oddeven(self):
        if (self.Oddeven_status == 0):
            self.Oddeven_status = 1
            self.label_oddeven.setStyleSheet(_fromUtf8("background-color: rgb(35, 255, 0);\n"
                                                      "min-width:     16px;\n"
                                                      "min-height:    16px;    \n"
                                                      "max-width:     16px;    \n"
                                                      "max-height:    16px;    \n"
                                                      "border-radius: 8px;    "))
            self.lineEdit_amp2set.setEnabled(True)
            self.lineEdit_pha2set.setEnabled(True)
            self.lineEdit_amp2set.setStyleSheet(_fromUtf8(""))
            self.lineEdit_pha2set.setStyleSheet(_fromUtf8(""))
        else:
            self.Oddeven_status = 0
            self.label_oddeven.setStyleSheet(_fromUtf8("background-color: rgb(181, 181, 181);\n"
                                                      "min-width:     16px;\n"
                                                      "min-height:    16px;    \n"
                                                      "max-width:     16px;    \n"
                                                      "max-height:    16px;    \n"
                                                      "border-radius: 8px;    "))
            self.lineEdit_amp2set.setEnabled(False)
            self.lineEdit_pha2set.setEnabled(False)
            self.lineEdit_amp2set.setStyleSheet(_fromUtf8("background-color: rgb(217, 217, 217);\n"))
            self.lineEdit_pha2set.setStyleSheet(_fromUtf8("background-color: rgb(217, 217, 217);\n"))
            # caput self.Oddeven_status
        return
    def Feed_forward(self):
        if (self.Feed_forward_status == 0):
            self.Feed_forward_status = 1
            self.label_feed.setStyleSheet(_fromUtf8("background-color: rgb(35, 255, 0);\n"
                                                       "min-width:     16px;\n"
                                                       "min-height:    16px;    \n"
                                                       "max-width:     16px;    \n"
                                                       "max-height:    16px;    \n"
                                                       "border-radius: 8px;    "))
        else:
            self.Feed_forward_status = 0
            self.label_feed.setStyleSheet(_fromUtf8("background-color: rgb(181, 181, 181);\n"
                                                       "min-width:     16px;\n"
                                                       "min-height:    16px;    \n"
                                                       "max-width:     16px;    \n"
                                                       "max-height:    16px;    \n"
                                                       "border-radius: 8px;    "))
            # caput self.Feed_forward_status
        return