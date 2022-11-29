# coding=UTF-8
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication
from DCLSUItest_second import Ui_Form as u2


class SecondWindow(QtGui.QMainWindow, u2):
    def __init__(self, parent1, parent2):
        super(SecondWindow, self).__init__()  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        self.parent1 = parent1
        self.parent2 = parent2
        # print(self.parent)
        self.lineEdit_IQ_WP.setText(str(self.parent1))
        self.lineEdit_SP_Amp1.setText(str(self.parent1))
        self.lineEdit_SP_Phase1.setText(str(self.parent2))

        # 二级界面actual不可更改
        # Trigger Setting
        self.lineEdit_TS_SWHZact.setEnabled(False)
        self.lineEdit_TS_PLact.setEnabled(False)
        # V.Sum block
        self.lineEdit_VS_VMactO1.setEnabled(False)
        self.lineEdit_VS_VMactO2.setEnabled(False)
        self.lineEdit_VS_VMactE1.setEnabled(False)
        self.lineEdit_VS_VMactE2.setEnabled(False)
        self.lineEdit_VS_RefactO1.setEnabled(False)
        self.lineEdit_VS_RefactO2.setEnabled(False)
        self.lineEdit_VS_RefactE1.setEnabled(False)
        self.lineEdit_VS_RefactE2.setEnabled(False)
        self.lineEdit_VS_SSAactO1.setEnabled(False)
        self.lineEdit_VS_SSAactO2.setEnabled(False)
        self.lineEdit_VS_SSAactE1.setEnabled(False)
        self.lineEdit_VS_SSAactE2.setEnabled(False)
        self.lineEdit_VS_klyactO1.setEnabled(False)
        self.lineEdit_VS_klyactO2.setEnabled(False)
        self.lineEdit_VS_klyactE1.setEnabled(False)
        self.lineEdit_VS_klyactE2.setEnabled(False)
        self.lineEdit_VS_DeflactO1.setEnabled(False)
        self.lineEdit_VS_DeflactO2.setEnabled(False)
        self.lineEdit_VS_DeflactE1.setEnabled(False)
        self.lineEdit_VS_DeflactE2.setEnabled(False)
        self.lineEdit_VS_loadactO1.setEnabled(False)
        self.lineEdit_VS_loadactO2.setEnabled(False)
        self.lineEdit_VS_loadactE1.setEnabled(False)
        self.lineEdit_VS_loadactE2.setEnabled(False)
        self.lineEdit_VS_RMSact.setEnabled(False)
        # Sampling
        self.lineEdit_SP_PGact.setEnabled(False)
        self.lineEdit_SP_RCact.setEnabled(False)
        self.lineEdit_SP_RWact.setEnabled(False)
        # Attentunation(Amp)(input 1-64)
        self.lineEdit_AA_VMact.setEnabled(False)
        self.lineEdit_AA_Refact.setEnabled(False)
        self.lineEdit_AA_SSAact.setEnabled(False)
        self.lineEdit_AA_Klyact.setEnabled(False)
        self.lineEdit_AA_Deflact.setEnabled(False)
        self.lineEdit_AA_loadact.setEnabled(False)
        # Delay(1~1024)
        self.lineEdit_DL_VMact.setEnabled(False)
        self.lineEdit_DL_Refact.setEnabled(False)
        self.lineEdit_DL_SSAact.setEnabled(False)
        self.lineEdit_DL_Klyact.setEnabled(False)
        self.lineEdit_DL_Deflact.setEnabled(False)
        self.lineEdit_DL_loadact.setEnabled(False)
        self.lineEdit_DL_Klyreact.setEnabled(False)
        self.lineEdit_DL_KlyHVact.setEnabled(False)
        # Amp compension
        self.lineEdit_AC_VMact.setEnabled(False)
        self.lineEdit_AC_Refact.setEnabled(False)
        self.lineEdit_AC_SSAact.setEnabled(False)
        self.lineEdit_AC_Klyact.setEnabled(False)
        self.lineEdit_AC_Deflact.setEnabled(False)
        self.lineEdit_AC_loadact.setEnabled(False)
        self.lineEdit_AC_Klyreact.setEnabled(False)
        # Phase compension(-180°~180°)
        self.lineEdit_PC_VMact.setEnabled(False)
        self.lineEdit_PC_Refact.setEnabled(False)
        self.lineEdit_PC_SSAact.setEnabled(False)
        self.lineEdit_PC_Klyact.setEnabled(False)
        self.lineEdit_PC_Deflact.setEnabled(False)
        self.lineEdit_PC_loadact.setEnabled(False)
        # VM correct
        self.lineEdit_VM_A.setEnabled(False)
        self.lineEdit_VM_B.setEnabled(False)
        self.lineEdit_VM_C.setEnabled(False)
        self.lineEdit_VM_D.setEnabled(False)
        self.lineEdit_VM_X.setEnabled(False)
        self.lineEdit_VM_Y.setEnabled(False)
        # IQ correct
        self.lineEdit_IQ_WP.setEnabled(False)
        self.lineEdit_IQ_A.setEnabled(False)
        self.lineEdit_IQ_B.setEnabled(False)
        self.lineEdit_IQ_C.setEnabled(False)
        self.lineEdit_IQ_D.setEnabled(False)
        self.lineEdit_IQ_S.setEnabled(False)
        self.lineEdit_IQ_T.setEnabled(False)
        self.lineEdit_IQ_K.setEnabled(False)
        # Steps pattern
        self.lineEdit_SP_Amp1.setEnabled(False)
        self.lineEdit_SP_Phase1.setEnabled(False)

    # 二级集面逻辑交互 回读显示Trigger Setting
    def get_TS_SWHZ(self):
        TS_SWHZ_set = float(self.lineEdit_TS_SWHZset.text())  # 获取lineedit中的值
        print(float(TS_SWHZ_set))
        # caput
        # 回读值显示
        # caget
        TS_SWHZ_actual = TS_SWHZ_set
        self.lineEdit_TS_SWHZact.setText(str(TS_SWHZ_actual))
        return

    def get_TS_PL(self):
        TS_PL_set = float(self.lineEdit_TS_PLset.text())  # 获取lineedit中的值
        print(float(TS_PL_set))
        # caput
        # 回读值显示
        # caget
        TS_PL_actual = TS_PL_set
        self.lineEdit_TS_PLact.setText(str(TS_PL_actual))
        return

    # V.Sum block
    def get_VS_VMO1(self):
        VS_VM01_set = float(self.lineEdit_VS_VMsetO1.text())  # 获取lineedit中的值
        print(float(VS_VM01_set))
        # caput
        # 回读值显示
        # caget
        VS_VM01_actual = VS_VM01_set
        self.lineEdit_VS_VMactO1.setText(str(VS_VM01_actual))
        return

    def get_VS_VMO2(self):
        VS_VM02_set = float(self.lineEdit_VS_VMsetO2.text())  # 获取lineedit中的值
        print(float(VS_VM02_set))
        # caput
        # 回读值显示
        # caget
        VS_VM02_actual = VS_VM02_set
        self.lineEdit_VS_VMactO2.setText(str(VS_VM02_actual))
        return

    def get_VS_VME1(self):
        VS_VME1_set = float(self.lineEdit_VS_VMsetE1.text())  # 获取lineedit中的值
        print(float(VS_VME1_set))
        # caput
        # 回读值显示
        # caget
        VS_VME1_actual = VS_VME1_set
        self.lineEdit_VS_VMactE1.setText(str(VS_VME1_actual))
        return

    def get_VS_VME2(self):
        VS_VME2_set = float(self.lineEdit_VS_VMsetE2.text())  # 获取lineedit中的值
        print(float(VS_VME2_set))
        # caput
        # 回读值显示
        # caget
        VS_VME2_actual = VS_VME2_set
        self.lineEdit_VS_VMactE2.setText(str(VS_VME2_actual))
        return

    def get_VS_RefO1(self):
        VS_Ref01_set = float(self.lineEdit_VS_RefsetO1.text())  # 获取lineedit中的值
        print(float(VS_Ref01_set))
        # caput
        # 回读值显示
        # caget
        VS_Ref01_actual = VS_Ref01_set
        self.lineEdit_VS_RefactO1.setText(str(VS_Ref01_actual))
        return

    def get_VS_RefO2(self):
        VS_Ref02_set = float(self.lineEdit_VS_RefsetO2.text())  # 获取lineedit中的值
        print(float(VS_Ref02_set))
        # caput
        # 回读值显示
        # caget
        VS_Ref02_actual = VS_Ref02_set
        self.lineEdit_VS_RefactO2.setText(str(VS_Ref02_actual))
        return

    def get_VS_RefE1(self):
        VS_RefE1_set = float(self.lineEdit_VS_RefsetE1.text())  # 获取lineedit中的值
        print(float(VS_RefE1_set))
        # caput
        # 回读值显示
        # caget
        VS_RefE1_actual = VS_RefE1_set
        self.lineEdit_VS_RefactE1.setText(str(VS_RefE1_actual))
        return

    def get_VS_RefE2(self):
        VS_RefE2_set = float(self.lineEdit_VS_RefsetE2.text())  # 获取lineedit中的值
        print(float(VS_RefE2_set))
        # caput
        # 回读值显示
        # caget
        VS_RefE2_actual = VS_RefE2_set
        self.lineEdit_VS_RefactE2.setText(str(VS_RefE2_actual))
        return

    def get_VS_SSAO1(self):
        VS_SSA01_set = float(self.lineEdit_VS_SSAsetO1.text())  # 获取lineedit中的值
        print(float(VS_SSA01_set))
        # caput
        # 回读值显示
        # caget
        VS_SSA01_actual = VS_SSA01_set
        self.lineEdit_VS_SSAactO1.setText(str(VS_SSA01_actual))
        return

    def get_VS_SSAO2(self):
        VS_SSA02_set = float(self.lineEdit_VS_SSAsetO2.text())  # 获取lineedit中的值
        print(float(VS_SSA02_set))
        # caput
        # 回读值显示
        # caget
        VS_SSA02_actual = VS_SSA02_set
        self.lineEdit_VS_SSAactO2.setText(str(VS_SSA02_actual))
        return

    def get_VS_SSAE1(self):
        VS_SSAE1_set = float(self.lineEdit_VS_SSAsetE1.text())  # 获取lineedit中的值
        print(float(VS_SSAE1_set))
        # caput
        # 回读值显示
        # caget
        VS_SSAE1_actual = VS_SSAE1_set
        self.lineEdit_VS_SSAactE1.setText(str(VS_SSAE1_actual))
        return

    def get_VS_SSAE2(self):
        VS_SSAE2_set = float(self.lineEdit_VS_SSAsetE2.text())  # 获取lineedit中的值
        print(float(VS_SSAE2_set))
        # caput
        # 回读值显示
        # caget
        VS_SSAE2_actual = VS_SSAE2_set
        self.lineEdit_VS_SSAactE2.setText(str(VS_SSAE2_actual))
        return

    def get_VS_KlyO1(self):
        VS_KlyO1_set = float(self.lineEdit_VS_klysetO1.text())  # 获取lineedit中的值
        print(float(VS_KlyO1_set))
        # caput
        # 回读值显示
        # caget
        VS_KlyO1_actual = VS_KlyO1_set
        self.lineEdit_VS_klyactO1.setText(str(VS_KlyO1_actual))
        return

    def get_VS_KlyO2(self):
        VS_KlyO2_set = float(self.lineEdit_VS_klysetO2.text())  # 获取lineedit中的值
        print(float(VS_KlyO2_set))
        # caput
        # 回读值显示
        # caget
        VS_KlyO2_actual = VS_KlyO2_set
        self.lineEdit_VS_klyactO2.setText(str(VS_KlyO2_actual))
        return

    def get_VS_KlyE1(self):
        VS_KlyE1_set = float(self.lineEdit_VS_klysetE1.text())  # 获取lineedit中的值
        print(float(VS_KlyE1_set))
        # caput
        # 回读值显示
        # caget
        VS_KlyE1_actual = VS_KlyE1_set
        self.lineEdit_VS_klyactE1.setText(str(VS_KlyE1_actual))
        return

    def get_VS_KlyE2(self):
        VS_KlyE2_set = float(self.lineEdit_VS_klysetE2.text())  # 获取lineedit中的值
        print(float(VS_KlyE2_set))
        # caput
        # 回读值显示
        # caget
        VS_KlyE2_actual = VS_KlyE2_set
        self.lineEdit_VS_klyactE2.setText(str(VS_KlyE2_actual))
        return

    def get_VS_DeflO1(self):
        VS_DeflO1_set = float(self.lineEdit_VS_DeflsetO1.text())  # 获取lineedit中的值
        print(float(VS_DeflO1_set))
        # caput
        # 回读值显示
        # caget
        VS_DeflO1_actual = VS_DeflO1_set
        self.lineEdit_VS_DeflactO1.setText(str(VS_DeflO1_actual))
        return

    def get_VS_DeflO2(self):
        VS_Defl02_set = float(self.lineEdit_VS_DeflsetO2.text())  # 获取lineedit中的值
        print(float(VS_Defl02_set))
        # caput
        # 回读值显示
        # caget
        VS_Defl02_actual = VS_Defl02_set
        self.lineEdit_VS_DeflactO2.setText(str(VS_Defl02_actual))
        return

    def get_VS_DeflE1(self):
        VS_DeflE1_set = float(self.lineEdit_VS_DeflsetE1.text())  # 获取lineedit中的值
        print(float(VS_DeflE1_set))
        # caput
        # 回读值显示
        # caget
        VS_DeflE1_actual = VS_DeflE1_set
        self.lineEdit_VS_DeflactE1.setText(str(VS_DeflE1_actual))
        return

    def get_VS_DeflE2(self):
        VS_DeflE2_set = float(self.lineEdit_VS_DeflsetE2.text())  # 获取lineedit中的值
        print(float(VS_DeflE2_set))
        # caput
        # 回读值显示
        # caget
        VS_Defl2_actual = VS_DeflE2_set
        self.lineEdit_VS_DeflactE2.setText(str(VS_Defl2_actual))
        return

    def get_VS_loadO1(self):
        VS_load01_set = float(self.lineEdit_VS_loadsetO1.text())  # 获取lineedit中的值
        print(float(VS_load01_set))
        # caput
        # 回读值显示
        # caget
        VS_load01_actual = VS_load01_set
        self.lineEdit_VS_loadactO1.setText(str(VS_load01_actual))
        return

    def get_VS_loadO2(self):
        VS_load02_set = float(self.lineEdit_VS_loadsetO2.text())  # 获取lineedit中的值
        print(float(VS_load02_set))
        # caput
        # 回读值显示
        # caget
        VS_load02_actual = VS_load02_set
        self.lineEdit_VS_loadactO2.setText(str(VS_load02_actual))
        return

    def get_VS_loadE1(self):
        VS_loadE1_set = float(self.lineEdit_VS_loadsetE1.text())  # 获取lineedit中的值
        print(float(VS_loadE1_set))
        # caput
        # 回读值显示
        # caget
        VS_loadE1_actual = VS_loadE1_set
        self.lineEdit_VS_loadactE1.setText(str(VS_loadE1_actual))
        return

    def get_VS_loadE2(self):
        VS_loadE2_set = float(self.lineEdit_VS_loadsetE2.text())  # 获取lineedit中的值
        print(float(VS_loadE2_set))
        # caput
        # 回读值显示
        # caget
        VS_load2_actual = VS_loadE2_set
        self.lineEdit_VS_loadactE2.setText(str(VS_load2_actual))
        return

    def get_VS_RMS(self):
        VS_RMS_set = float(self.lineEdit_VS_RMSset.text())  # 获取lineedit中的值
        print(float(VS_RMS_set))
        # caput
        # 回读值显示
        # caget
        VS_RMS_actual = VS_RMS_set
        self.lineEdit_VS_RMSact.setText(str(VS_RMS_actual))
        return

    # Sampling
    def get_SP_PG(self):
        SP_PG_set = float(self.lineEdit_SP_PGset.text())  # 获取lineedit中的值
        print(float(SP_PG_set))
        # caput
        # 回读值显示
        # caget
        SP_PG_actual = SP_PG_set
        self.lineEdit_SP_PGact.setText(str(SP_PG_actual))
        return

    def get_SP_RC(self):
        SP_RC_set = float(self.lineEdit_SP_RCset.text())  # 获取lineedit中的值
        print(float(SP_RC_set))
        # caput
        # 回读值显示
        # caget
        SP_RC_actual = SP_RC_set
        self.lineEdit_SP_RCact.setText(str(SP_RC_actual))
        return

    def get_SP_RW(self):
        SP_RW_set = float(self.lineEdit_SP_RWset.text())  # 获取lineedit中的值
        print(float(SP_RW_set))
        # caput
        # 回读值显示
        # caget
        SP_RW_actual = SP_RW_set
        self.lineEdit_SP_RWact.setText(str(SP_RW_actual))
        return

    # Attentunation(Amp)(input 1-64)
    def get_AA_VM(self):
        AA_VM_set = float(self.lineEdit_AA_VMset.text())  # 获取lineedit中的值
        print(float(AA_VM_set))
        # caput
        # 回读值显示
        # caget
        AA_VM_actual = AA_VM_set
        self.lineEdit_AA_VMact.setText(str(AA_VM_actual))
        return

    def get_AA_Ref(self):
        AA_Ref_set = float(self.lineEdit_AA_Refset.text())  # 获取lineedit中的值
        print(float(AA_Ref_set))
        # caput
        # 回读值显示
        # caget
        AA_Ref_actual = AA_Ref_set
        self.lineEdit_AA_Refact.setText(str(AA_Ref_actual))
        return

    def get_AA_SSA(self):
        AA_SSA_set = float(self.lineEdit_AA_SSAset.text())  # 获取lineedit中的值
        print(float(AA_SSA_set))
        # caput
        # 回读值显示
        # caget
        AA_SSA_actual = AA_SSA_set
        self.lineEdit_AA_SSAact.setText(str(AA_SSA_actual))
        return

    def get_AA_Kly(self):
        AA_Kly_set = float(self.lineEdit_AA_Klyset.text())  # 获取lineedit中的值
        print(float(AA_Kly_set))
        # caput
        # 回读值显示
        # caget
        AA_Kly_actual = AA_Kly_set
        self.lineEdit_AA_Klyact.setText(str(AA_Kly_actual))
        return

    def get_AA_Defl(self):
        AA_Defl_set = float(self.lineEdit_AA_Deflset.text())  # 获取lineedit中的值
        print(float(AA_Defl_set))
        # caput
        # 回读值显示
        # caget
        AA_Defl_actual = AA_Defl_set
        self.lineEdit_AA_Deflact.setText(str(AA_Defl_actual))
        return

    def get_AA_load(self):
        AA_load_set = float(self.lineEdit_AA_loadset.text())  # 获取lineedit中的值
        print(float(AA_load_set))
        # caput
        # 回读值显示
        # caget
        AA_load_actual = AA_load_set
        self.lineEdit_AA_loadact.setText(str(AA_load_actual))
        return

    # Delay(1~1024)
    def get_DL_VM(self):
        DL_VM_set = float(self.lineEdit_DL_VMset.text())  # 获取lineedit中的值
        print(float(DL_VM_set))
        # caput
        # 回读值显示
        # caget
        DL_VM_actual = DL_VM_set
        self.lineEdit_DL_VMact.setText(str(DL_VM_actual))
        return

    def get_DL_Ref(self):
        DL_Ref_set = float(self.lineEdit_DL_Refset.text())  # 获取lineedit中的值
        print(float(DL_Ref_set))
        # caput
        # 回读值显示
        # caget
        DL_Ref_actual = DL_Ref_set
        self.lineEdit_DL_Refact.setText(str(DL_Ref_actual))
        return

    def get_DL_SSA(self):
        DL_SSA_set = float(self.lineEdit_DL_SSAset.text())  # 获取lineedit中的值
        print(float(DL_SSA_set))
        # caput
        # 回读值显示
        # caget
        DL_SSA_actual = DL_SSA_set
        self.lineEdit_DL_SSAact.setText(str(DL_SSA_actual))
        return

    def get_DL_Kly(self):
        DL_Kly_set = float(self.lineEdit_DL_Klyset.text())  # 获取lineedit中的值
        print(float(DL_Kly_set))
        # caput
        # 回读值显示
        # caget
        DL_Kly_actual = DL_Kly_set
        self.lineEdit_DL_Klyact.setText(str(DL_Kly_actual))
        return

    def get_DL_Defl(self):
        DL_Defl_set = float(self.lineEdit_DL_Deflset.text())  # 获取lineedit中的值
        print(float(DL_Defl_set))
        # caput
        # 回读值显示
        # caget
        DL_Defl_actual = DL_Defl_set
        self.lineEdit_DL_Deflact.setText(str(DL_Defl_actual))
        return

    def get_DL_load(self):
        DL_load_set = float(self.lineEdit_DL_loadset.text())  # 获取lineedit中的值
        print(float(DL_load_set))
        # caput
        # 回读值显示
        # caget
        DL_load_actual = DL_load_set
        self.lineEdit_DL_loadact.setText(str(DL_load_actual))
        return

    def get_DL_Klyre(self):
        DL_Klyre_set = float(self.lineEdit_DL_Klyreset.text())  # 获取lineedit中的值
        print(float(DL_Klyre_set))
        # caput
        # 回读值显示
        # caget
        DL_Klyre_actual = DL_Klyre_set
        self.lineEdit_DL_Klyreact.setText(str(DL_Klyre_actual))
        return

    def get_DL_KlyHV(self):
        DL_KlyHV_set = float(self.lineEdit_DL_KlyHVset.text())  # 获取lineedit中的值
        print(float(DL_KlyHV_set))
        # caput
        # 回读值显示
        # caget
        DL_KlyHV_actual = DL_KlyHV_set
        self.lineEdit_DL_KlyHVact.setText(str(DL_KlyHV_actual))
        return

    # Amp compension
    def get_AC_VM(self):
        AC_VM_set = float(self.lineEdit_AC_VMset.text())  # 获取lineedit中的值
        print(float(AC_VM_set))
        # caput
        # 回读值显示
        # caget
        AC_VM_actual = AC_VM_set
        self.lineEdit_AC_VMact.setText(str(AC_VM_actual))
        return

    def get_AC_Ref(self):
        AC_Ref_set = float(self.lineEdit_AC_Refset.text())  # 获取lineedit中的值
        print(float(AC_Ref_set))
        # caput
        # 回读值显示
        # caget
        AC_Ref_actual = AC_Ref_set
        self.lineEdit_AC_Refact.setText(str(AC_Ref_actual))
        return

    def get_AC_SSA(self):
        AC_SSA_set = float(self.lineEdit_AC_SSAset.text())  # 获取lineedit中的值
        print(float(AC_SSA_set))
        # caput
        # 回读值显示
        # caget
        AC_SSA_actual = AC_SSA_set
        self.lineEdit_AC_SSAact.setText(str(AC_SSA_actual))
        return

    def get_AC_Kly(self):
        AC_Kly_set = float(self.lineEdit_AC_Klyset.text())  # 获取lineedit中的值
        print(float(AC_Kly_set))
        # caput
        # 回读值显示
        # caget
        AC_Kly_actual = AC_Kly_set
        self.lineEdit_AC_Klyact.setText(str(AC_Kly_actual))
        return

    def get_AC_Defl(self):
        AC_Defl_set = float(self.lineEdit_AC_Deflset.text())  # 获取lineedit中的值
        print(float(AC_Defl_set))
        # caput
        # 回读值显示
        # caget
        AC_Defl_actual = AC_Defl_set
        self.lineEdit_AC_Deflact.setText(str(AC_Defl_actual))
        return

    def get_AC_load(self):
        AC_load_set = float(self.lineEdit_AC_loadset.text())  # 获取lineedit中的值
        print(float(AC_load_set))
        # caput
        # 回读值显示
        # caget
        AC_load_actual = AC_load_set
        self.lineEdit_AC_loadact.setText(str(AC_load_actual))
        return

    def get_AC_Klyre(self):
        AC_Klyre_set = float(self.lineEdit_AC_Klyreset.text())  # 获取lineedit中的值
        print(float(AC_Klyre_set))
        # caput
        # 回读值显示
        # caget
        AC_Klyre_actual = AC_Klyre_set
        self.lineEdit_AC_Klyreact.setText(str(AC_Klyre_actual))
        return

    # Phase compension(-180°~180°)
    def get_PC_VM(self):
        PC_VM_set = float(self.lineEdit_PC_VMset.text())  # 获取lineedit中的值
        print(float(PC_VM_set))
        # caput
        # 回读值显示
        # caget
        PC_VM_actual = PC_VM_set
        self.lineEdit_PC_VMact.setText(str(PC_VM_actual))
        return

    def get_PC_Ref(self):
        PC_Ref_set = float(self.lineEdit_PC_Refset.text())  # 获取lineedit中的值
        print(float(PC_Ref_set))
        # caput
        # 回读值显示
        # caget
        PC_Ref_actual = PC_Ref_set
        self.lineEdit_PC_Refact.setText(str(PC_Ref_actual))
        return

    def get_PC_SSA(self):
        PC_SSA_set = float(self.lineEdit_PC_SSAset.text())  # 获取lineedit中的值
        print(float(PC_SSA_set))
        # caput
        # 回读值显示
        # caget
        PC_SSA_actual = PC_SSA_set
        self.lineEdit_PC_SSAact.setText(str(PC_SSA_actual))
        return

    def get_PC_Kly(self):
        PC_Kly_set = float(self.lineEdit_PC_Klyset.text())  # 获取lineedit中的值
        print(float(PC_Kly_set))
        # caput
        # 回读值显示
        # caget
        PC_Kly_actual = PC_Kly_set
        self.lineEdit_PC_Klyact.setText(str(PC_Kly_actual))
        return

    def get_PC_Defl(self):
        PC_Defl_set = float(self.lineEdit_PC_Deflset.text())  # 获取lineedit中的值
        print(float(PC_Defl_set))
        # caput
        # 回读值显示
        # caget
        PC_Defl_actual = PC_Defl_set
        self.lineEdit_PC_Deflact.setText(str(PC_Defl_actual))
        return

    def get_PC_load(self):
        PC_load_set = float(self.lineEdit_PC_loadset.text())  # 获取lineedit中的值
        print(float(PC_load_set))
        # caput
        # 回读值显示
        # caget
        PC_load_actual = PC_load_set
        self.lineEdit_PC_loadact.setText(str(PC_load_actual))
        return

    # VM correct
    def get_VMcorrect(self):
        VMcorrect_status = 1
        # caput
        VM_A = 1
        VM_B = 2
        VM_C = 3
        VM_D = 4
        VM_X = 5
        VM_Y = 6
        # caget
        self.lineEdit_VM_A.setText(str(VM_A))
        self.lineEdit_VM_B.setText(str(VM_B))
        self.lineEdit_VM_C.setText(str(VM_C))
        self.lineEdit_VM_D.setText(str(VM_D))
        self.lineEdit_VM_X.setText(str(VM_X))
        self.lineEdit_VM_Y.setText(str(VM_Y))
        return

    # IQ correct
    def get_IQcorrect(self):
        if (self.lineEdit_IQ_Range.text() == '' or self.lineEdit_IQ_Left.text() == '' or self.lineEdit_IQ_Right.text() == '' or self.lineEdit_IQ_Times.text() == '' or self.lineEdit_IQ_WP.text() == ''):
            box = QtGui.QMessageBox()
            box.warning(self, "ERROR", "Please Input IQ Correcting Parameters!")
        else:
            IQcorrect_status = 1
            # IQ_WP=float(self.lineEdit_IQ_WP.text())
            IQ_Range = float(self.lineEdit_IQ_Range.text())
            IQ_Left = float(self.lineEdit_IQ_Left.text())
            IQ_Right = float(self.lineEdit_IQ_Right.text())
            IQ_Times = float(self.lineEdit_IQ_Times.text())
            # caput
            IQ_A = 1
            IQ_B = 2
            IQ_C = 3
            IQ_D = 4
            IQ_S = 5
            IQ_T = 6
            IQ_K = 6
            # caget
            self.lineEdit_IQ_A.setText(str(IQ_A))
            self.lineEdit_IQ_B.setText(str(IQ_B))
            self.lineEdit_IQ_C.setText(str(IQ_C))
            self.lineEdit_IQ_D.setText(str(IQ_D))
            self.lineEdit_IQ_S.setText(str(IQ_S))
            self.lineEdit_IQ_T.setText(str(IQ_T))
            self.lineEdit_IQ_K.setText(str(IQ_K))
        return

    def get_Steps(self):
        if (
                self.lineEdit_SP_Amp1.text() == '' or self.lineEdit_SP_Phase1.text() == '' or self.lineEdit_SP_Amp2.text() == '' or self.lineEdit_SP_Phase2.text() == '' or self.lineEdit_SP_BW.text() == ''):
            box = QtGui.QMessageBox()
            box.warning(self, "ERROR", "Please Input IQ Steps Pattern Parameters!")
        else:
            Steps_status = 1
            SP_Amp1 = float(self.lineEdit_SP_Amp1.text())
            SP_Phase1 = float(self.lineEdit_SP_Phase1.text())
            SP_Amp2 = float(self.lineEdit_SP_Amp2.text())
            SP_Phase2 = float(self.lineEdit_SP_Phase2.text())
            SP_Phase2 = float(self.lineEdit_SP_BW.text())
            # caput
        return
    def get_TS_SW(self):
        box = QtGui.QMessageBox()
        box.warning(self, "Tips", "SW Is Already Checked!")
        TS_SW_status=1
        # caput
        self.lineEdit_TS_SWHZset.setEnabled(True)
        return
    def get_TS_EXT(self):
        box = QtGui.QMessageBox()
        box.warning(self, "Tips", "EXT Is Already Checked!")
        TS_EXT_status=1
        # caput
        self.lineEdit_TS_SWHZset.setEnabled(False)
        return
    def get_SP_full(self):
        if(self.radioButton_Full.isChecked()):
            box = QtGui.QMessageBox()
            box.warning(self, "Tips", "Full Pulse Is Checked!")
            SP_full_status = 1
            # caput
        else:
            box = QtGui.QMessageBox()
            box.warning(self, "Tips", "Full Pulse Is closed!")
            SP_full_status = 0
            # caput
        return