# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(10, 380, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 430, 801, 211))
        self.graphWidget.setObjectName("graphWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 391, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.multi_up_Button = QtWidgets.QPushButton(self.tab)
        self.multi_up_Button.setGeometry(QtCore.QRect(180, 80, 51, 41))
        self.multi_up_Button.setObjectName("multi_up_Button")
        self.multi_down_Button = QtWidgets.QPushButton(self.tab)
        self.multi_down_Button.setGeometry(QtCore.QRect(300, 80, 51, 41))
        self.multi_down_Button.setObjectName("multi_down_Button")
        self.stopButton = QtWidgets.QPushButton(self.tab)
        self.stopButton.setGeometry(QtCore.QRect(240, 80, 51, 101))
        self.stopButton.setObjectName("stopButton")
        self.multistep_numberBox = QtWidgets.QDoubleSpinBox(self.tab)
        self.multistep_numberBox.setGeometry(QtCore.QRect(90, 90, 71, 26))
        self.multistep_numberBox.setProperty("value", 30.0)
        self.multistep_numberBox.setObjectName("multistep_numberBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_2.setObjectName("label_2")
        self.perm_down_Button = QtWidgets.QPushButton(self.tab)
        self.perm_down_Button.setGeometry(QtCore.QRect(300, 140, 51, 41))
        self.perm_down_Button.setObjectName("perm_down_Button")
        self.perm_up_Button = QtWidgets.QPushButton(self.tab)
        self.perm_up_Button.setGeometry(QtCore.QRect(180, 140, 51, 41))
        self.perm_up_Button.setObjectName("perm_up_Button")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 17, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.rpmSlider = QtWidgets.QSlider(self.tab)
        self.rpmSlider.setGeometry(QtCore.QRect(29, 250, 321, 20))
        self.rpmSlider.setMinimum(-120)
        self.rpmSlider.setMaximum(120)
        self.rpmSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rpmSlider.setObjectName("rpmSlider")
        self.rpmBox = QtWidgets.QDoubleSpinBox(self.tab)
        self.rpmBox.setGeometry(QtCore.QRect(200, 210, 81, 31))
        self.rpmBox.setDecimals(4)
        self.rpmBox.setObjectName("rpmBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(300, 220, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(180, 30, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(300, 30, 81, 21))
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_4.setObjectName("label_4")
        self.update_rpm_button = QtWidgets.QPushButton(self.tab)
        self.update_rpm_button.setGeometry(QtCore.QRect(70, 210, 71, 28))
        self.update_rpm_button.setObjectName("update_rpm_button")
        self.pushB_close_valve = QtWidgets.QPushButton(self.tab)
        self.pushB_close_valve.setGeometry(QtCore.QRect(20, 280, 131, 41))
        self.pushB_close_valve.setObjectName("pushB_close_valve")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(180, 50, 81, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(300, 50, 81, 21))
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.driveprofile_pushB = QtWidgets.QPushButton(self.tab_2)
        self.driveprofile_pushB.setGeometry(QtCore.QRect(70, 80, 101, 41))
        self.driveprofile_pushB.setObjectName("driveprofile_pushB")
        self.stopprofile_pushB = QtWidgets.QPushButton(self.tab_2)
        self.stopprofile_pushB.setGeometry(QtCore.QRect(220, 80, 101, 41))
        self.stopprofile_pushB.setObjectName("stopprofile_pushB")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(140, 180, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.maxvel_spinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.maxvel_spinBox.setGeometry(QtCore.QRect(60, 240, 71, 31))
        self.maxvel_spinBox.setDecimals(4)
        self.maxvel_spinBox.setMaximum(120.0)
        self.maxvel_spinBox.setProperty("value", 60.0)
        self.maxvel_spinBox.setObjectName("maxvel_spinBox")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(140, 250, 81, 16))
        self.label_7.setObjectName("label_7")
        self.sigma1_SP_spinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.sigma1_SP_spinBox.setGeometry(QtCore.QRect(70, 170, 61, 31))
        self.sigma1_SP_spinBox.setDecimals(4)
        self.sigma1_SP_spinBox.setMaximum(15000.0)
        self.sigma1_SP_spinBox.setObjectName("sigma1_SP_spinBox")
        self.pushB_update_const = QtWidgets.QPushButton(self.tab_2)
        self.pushB_update_const.setGeometry(QtCore.QRect(240, 200, 91, 31))
        self.pushB_update_const.setObjectName("pushB_update_const")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.stopprofile_pushB_2 = QtWidgets.QPushButton(self.tab_3)
        self.stopprofile_pushB_2.setGeometry(QtCore.QRect(220, 80, 101, 41))
        self.stopprofile_pushB_2.setObjectName("stopprofile_pushB_2")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.dsigma_SP_spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.dsigma_SP_spinBox.setGeometry(QtCore.QRect(40, 260, 61, 31))
        self.dsigma_SP_spinBox.setMaximum(600)
        self.dsigma_SP_spinBox.setProperty("value", 200)
        self.dsigma_SP_spinBox.setObjectName("dsigma_SP_spinBox")
        self.quench_start_pushB = QtWidgets.QPushButton(self.tab_3)
        self.quench_start_pushB.setGeometry(QtCore.QRect(70, 80, 101, 41))
        self.quench_start_pushB.setObjectName("quench_start_pushB")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(110, 260, 111, 31))
        self.label_6.setObjectName("label_6")
        self.rpmBox_prequench = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.rpmBox_prequench.setGeometry(QtCore.QRect(70, 170, 62, 22))
        self.rpmBox_prequench.setDecimals(3)
        self.rpmBox_prequench.setProperty("value", 0.5)
        self.rpmBox_prequench.setObjectName("rpmBox_prequench")
        self.rpmBox_quench = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.rpmBox_quench.setGeometry(QtCore.QRect(220, 170, 62, 22))
        self.rpmBox_quench.setDecimals(3)
        self.rpmBox_quench.setProperty("value", 0.005)
        self.rpmBox_quench.setObjectName("rpmBox_quench")
        self.prequenchrpm = QtWidgets.QLabel(self.tab_3)
        self.prequenchrpm.setGeometry(QtCore.QRect(70, 200, 141, 21))
        self.prequenchrpm.setObjectName("prequenchrpm")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(220, 200, 121, 21))
        self.label_15.setObjectName("label_15")
        self.pushB_update_quench = QtWidgets.QPushButton(self.tab_3)
        self.pushB_update_quench.setGeometry(QtCore.QRect(220, 260, 91, 31))
        self.pushB_update_quench.setObjectName("pushB_update_quench")
        self.tabWidget.addTab(self.tab_3, "")
        self.invert_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.invert_checkBox.setGeometry(QtCore.QRect(130, 390, 191, 21))
        self.invert_checkBox.setObjectName("invert_checkBox")
        self.lcd_actvel_s1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_actvel_s1.setGeometry(QtCore.QRect(640, 120, 64, 23))
        self.lcd_actvel_s1.setSmallDecimalPoint(False)
        self.lcd_actvel_s1.setObjectName("lcd_actvel_s1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(640, 90, 111, 21))
        self.label_13.setObjectName("label_13")
        self.initADC_s1 = QtWidgets.QCheckBox(self.centralwidget)
        self.initADC_s1.setGeometry(QtCore.QRect(410, 30, 151, 21))
        self.initADC_s1.setObjectName("initADC_s1")
        self.initADC_s3 = QtWidgets.QCheckBox(self.centralwidget)
        self.initADC_s3.setGeometry(QtCore.QRect(410, 60, 151, 21))
        self.initADC_s3.setObjectName("initADC_s3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 190, 421, 231))
        self.label.setObjectName("label")
        self.checkB_motor_s1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkB_motor_s1.setGeometry(QtCore.QRect(410, 120, 111, 21))
        self.checkB_motor_s1.setChecked(True)
        self.checkB_motor_s1.setObjectName("checkB_motor_s1")
        self.checkB_motor_s3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkB_motor_s3.setGeometry(QtCore.QRect(410, 160, 121, 21))
        self.checkB_motor_s3.setObjectName("checkB_motor_s3")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(650, 0, 181, 101))
        self.label_16.setObjectName("label_16")
        self.lcd_actvel_s3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_actvel_s3.setGeometry(QtCore.QRect(640, 160, 64, 23))
        self.lcd_actvel_s3.setObjectName("lcd_actvel_s3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.label_9.setText(_translate("MainWindow", "constant rotation"))
        self.multi_up_Button.setText(_translate("MainWindow", "up"))
        self.multi_down_Button.setText(_translate("MainWindow", "down"))
        self.stopButton.setText(_translate("MainWindow", "stop"))
        self.label_2.setText(_translate("MainWindow", "multi step"))
        self.perm_down_Button.setText(_translate("MainWindow", "down"))
        self.perm_up_Button.setText(_translate("MainWindow", "up"))
        self.label_10.setText(_translate("MainWindow", "Manual Mode"))
        self.label_3.setText(_translate("MainWindow", "RPM"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>retract </p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>shorten </p><p><br/></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "in deg"))
        self.update_rpm_button.setText(_translate("MainWindow", "Update"))
        self.pushB_close_valve.setText(_translate("MainWindow", "close oil valve"))
        self.label_17.setText(_translate("MainWindow", "pistion"))
        self.label_18.setText(_translate("MainWindow", "sample"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manual"))
        self.driveprofile_pushB.setText(_translate("MainWindow", "START"))
        self.stopprofile_pushB.setText(_translate("MainWindow", "STOP"))
        self.label_5.setText(_translate("MainWindow", "sigma1 setpoint"))
        self.label_11.setText(_translate("MainWindow", "Const Stress Mode"))
        self.label_7.setText(_translate("MainWindow", "max. velocity"))
        self.pushB_update_const.setText(_translate("MainWindow", "Update "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Const Stress"))
        self.stopprofile_pushB_2.setText(_translate("MainWindow", "STOP"))
        self.label_14.setText(_translate("MainWindow", "Quenching Mode"))
        self.quench_start_pushB.setText(_translate("MainWindow", "START"))
        self.label_6.setText(_translate("MainWindow", "dsigma setpoint"))
        self.prequenchrpm.setText(_translate("MainWindow", "prequench rpm"))
        self.label_15.setText(_translate("MainWindow", "quench rpm"))
        self.pushB_update_quench.setText(_translate("MainWindow", "Update "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Quenching"))
        self.invert_checkBox.setText(_translate("MainWindow", "invert direction: pos 2 / 4"))
        self.label_13.setText(_translate("MainWindow", "actual velocity"))
        self.initADC_s1.setText(_translate("MainWindow", "read ADC: sigma1"))
        self.initADC_s3.setText(_translate("MainWindow", "read ADC: sigma3"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">For Quenching: </span></p><p>- prequench rpm: to open valve until </p><p>oilpressure changes (fast)</p><p>- quench rpm: to open the valve all the way open (slow)</p><p>(target position := valve all the way opened)</p><p>- dsigma setpoint is the const. diff. stress [Mpa] </p><p>s1 establishes via PID as a passive reaction on s3 action</p><p><br/></p></body></html>"))
        self.checkB_motor_s1.setText(_translate("MainWindow", "motor s1"))
        self.checkB_motor_s3.setText(_translate("MainWindow", "motor s3"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">close</span> app<span style=\" font-weight:600;\"> only </span></p><p align=\"center\">via the <span style=\" font-weight:600;\">QUIT-button!</span></p></body></html>"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
