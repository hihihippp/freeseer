# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './forms/freeseer_configtool_ui.ui'
#
# Created: Thu Mar 10 19:13:59 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConfigureTool(object):
    def setupUi(self, ConfigureTool):
        ConfigureTool.setObjectName("ConfigureTool")
        ConfigureTool.resize(568, 493)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/freeseer/freeseer_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigureTool.setWindowIcon(icon)
        self.configureTab = QtGui.QTabWidget(ConfigureTool)
        self.configureTab.setEnabled(True)
        self.configureTab.setGeometry(QtCore.QRect(0, 0, 567, 441))
        self.configureTab.setCursor(QtCore.Qt.ArrowCursor)
        self.configureTab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.configureTab.setTabPosition(QtGui.QTabWidget.North)
        self.configureTab.setElideMode(QtCore.Qt.ElideNone)
        self.configureTab.setUsesScrollButtons(True)
        self.configureTab.setDocumentMode(False)
        self.configureTab.setTabsClosable(False)
        self.configureTab.setObjectName("configureTab")
        self.SourceSetting = QtGui.QWidget()
        self.SourceSetting.setObjectName("SourceSetting")
        self.groupBox_videoSource = QtGui.QGroupBox(self.SourceSetting)
        self.groupBox_videoSource.setGeometry(QtCore.QRect(14, 10, 531, 181))
        self.groupBox_videoSource.setFlat(False)
        self.groupBox_videoSource.setCheckable(True)
        self.groupBox_videoSource.setChecked(True)
        self.groupBox_videoSource.setObjectName("groupBox_videoSource")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_videoSource)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_videoSource = QtGui.QWidget(self.groupBox_videoSource)
        self.widget_videoSource.setObjectName("widget_videoSource")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.widget_videoSource)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.radioButton_localDesktop = QtGui.QRadioButton(self.widget_videoSource)
        self.radioButton_localDesktop.setEnabled(True)
        self.radioButton_localDesktop.setCheckable(True)
        self.radioButton_localDesktop.setChecked(True)
        self.radioButton_localDesktop.setObjectName("radioButton_localDesktop")
        self.verticalLayout_11.addWidget(self.radioButton_localDesktop)
        self.radioButton_hardware = QtGui.QRadioButton(self.widget_videoSource)
        self.radioButton_hardware.setEnabled(True)
        self.radioButton_hardware.setObjectName("radioButton_hardware")
        self.verticalLayout_11.addWidget(self.radioButton_hardware)
        self.horizontalLayout_2.addWidget(self.widget_videoSource)
        self.groupBox_localDesktopBox = QtGui.QGroupBox(self.groupBox_videoSource)
        self.groupBox_localDesktopBox.setEnabled(True)
        self.groupBox_localDesktopBox.setMinimumSize(QtCore.QSize(0, 138))
        self.groupBox_localDesktopBox.setObjectName("groupBox_localDesktopBox")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_localDesktopBox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.radioButton_recordLocalDesktop = QtGui.QRadioButton(self.groupBox_localDesktopBox)
        self.radioButton_recordLocalDesktop.setChecked(True)
        self.radioButton_recordLocalDesktop.setObjectName("radioButton_recordLocalDesktop")
        self.verticalLayout_12.addWidget(self.radioButton_recordLocalDesktop)
        self.radioButton_recordLocalArea = QtGui.QRadioButton(self.groupBox_localDesktopBox)
        self.radioButton_recordLocalArea.setEnabled(True)
        self.radioButton_recordLocalArea.setObjectName("radioButton_recordLocalArea")
        self.verticalLayout_12.addWidget(self.radioButton_recordLocalArea)
        self.radioButton_recordLocalWindow = QtGui.QRadioButton(self.groupBox_localDesktopBox)
        self.radioButton_recordLocalWindow.setEnabled(False)
        self.radioButton_recordLocalWindow.setObjectName("radioButton_recordLocalWindow")
        self.verticalLayout_12.addWidget(self.radioButton_recordLocalWindow)
        self.pushButton_setArea = QtGui.QPushButton(self.groupBox_localDesktopBox)
        self.pushButton_setArea.setEnabled(False)
        self.pushButton_setArea.setObjectName("pushButton_setArea")
        self.verticalLayout_12.addWidget(self.pushButton_setArea)
        self.horizontalLayout_2.addWidget(self.groupBox_localDesktopBox)
        self.groupBox_hardware = QtGui.QGroupBox(self.groupBox_videoSource)
        self.groupBox_hardware.setMinimumSize(QtCore.QSize(0, 138))
        self.groupBox_hardware.setFlat(False)
        self.groupBox_hardware.setCheckable(False)
        self.groupBox_hardware.setChecked(False)
        self.groupBox_hardware.setObjectName("groupBox_hardware")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_hardware)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.radioButton_USBsrc = QtGui.QRadioButton(self.groupBox_hardware)
        self.radioButton_USBsrc.setEnabled(False)
        self.radioButton_USBsrc.setChecked(True)
        self.radioButton_USBsrc.setObjectName("radioButton_USBsrc")
        self.verticalLayout_13.addWidget(self.radioButton_USBsrc)
        self.radioButton_firewiresrc = QtGui.QRadioButton(self.groupBox_hardware)
        self.radioButton_firewiresrc.setEnabled(False)
        self.radioButton_firewiresrc.setObjectName("radioButton_firewiresrc")
        self.verticalLayout_13.addWidget(self.radioButton_firewiresrc)
        self.comboBox_videoDeviceList = QtGui.QComboBox(self.groupBox_hardware)
        self.comboBox_videoDeviceList.setObjectName("comboBox_videoDeviceList")
        self.verticalLayout_13.addWidget(self.comboBox_videoDeviceList)
        self.horizontalLayout_2.addWidget(self.groupBox_hardware)
        self.groupBox_soundSource = QtGui.QGroupBox(self.SourceSetting)
        self.groupBox_soundSource.setGeometry(QtCore.QRect(10, 200, 521, 161))
        self.groupBox_soundSource.setCheckable(True)
        self.groupBox_soundSource.setObjectName("groupBox_soundSource")
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_soundSource)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_soundSource = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_soundSource.setObjectName("label_soundSource")
        self.horizontalLayout.addWidget(self.label_soundSource)
        self.comboBox_audioSourceList = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_audioSourceList.setObjectName("comboBox_audioSourceList")
        self.horizontalLayout.addWidget(self.comboBox_audioSourceList)
        self.configureTab.addTab(self.SourceSetting, "")
        self.Videosetting = QtGui.QWidget()
        self.Videosetting.setObjectName("Videosetting")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Videosetting)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_videoQuality = QtGui.QGroupBox(self.Videosetting)
        self.groupBox_videoQuality.setObjectName("groupBox_videoQuality")
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox_videoQuality)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 521, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_VideoQuality_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_VideoQuality_2.setObjectName("horizontalLayout_VideoQuality_2")
        self.label_videoQuality = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_videoQuality.setObjectName("label_videoQuality")
        self.horizontalLayout_VideoQuality_2.addWidget(self.label_videoQuality)
        self.comboBox_videoQualityList = QtGui.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_videoQualityList.setObjectName("comboBox_videoQualityList")
        self.comboBox_videoQualityList.addItem("")
        self.comboBox_videoQualityList.addItem("")
        self.comboBox_videoQualityList.addItem("")
        self.comboBox_videoQualityList.addItem("")
        self.comboBox_videoQualityList.addItem("")
        self.comboBox_videoQualityList.addItem("")
        self.horizontalLayout_VideoQuality_2.addWidget(self.comboBox_videoQualityList)
        self.pushButton_derectScreenResoltion = QtGui.QPushButton(self.groupBox_videoQuality)
        self.pushButton_derectScreenResoltion.setGeometry(QtCore.QRect(10, 340, 241, 28))
        self.pushButton_derectScreenResoltion.setObjectName("pushButton_derectScreenResoltion")
        self.tableWidget_screenResolution = QtGui.QTableWidget(self.groupBox_videoQuality)
        self.tableWidget_screenResolution.setGeometry(QtCore.QRect(10, 130, 521, 192))
        self.tableWidget_screenResolution.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_screenResolution.setObjectName("tableWidget_screenResolution")
        self.tableWidget_screenResolution.setColumnCount(1)
        self.tableWidget_screenResolution.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_screenResolution.setHorizontalHeaderItem(0, item)
        self.verticalLayout_2.addWidget(self.groupBox_videoQuality)
        self.configureTab.addTab(self.Videosetting, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_enableStreaming = QtGui.QGroupBox(self.tab)
        self.groupBox_enableStreaming.setEnabled(True)
        self.groupBox_enableStreaming.setGeometry(QtCore.QRect(10, 10, 531, 381))
        self.groupBox_enableStreaming.setCheckable(True)
        self.groupBox_enableStreaming.setChecked(False)
        self.groupBox_enableStreaming.setObjectName("groupBox_enableStreaming")
        self.layoutWidget_7 = QtGui.QWidget(self.groupBox_enableStreaming)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 40, 521, 181))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_EnableStreaming = QtGui.QGridLayout(self.layoutWidget_7)
        self.gridLayout_EnableStreaming.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_EnableStreaming.setObjectName("gridLayout_EnableStreaming")
        self.lineEdit_password = QtGui.QLineEdit(self.layoutWidget_7)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_EnableStreaming.addWidget(self.lineEdit_password, 3, 1, 1, 1)
        self.label_mountPointl = QtGui.QLabel(self.layoutWidget_7)
        self.label_mountPointl.setObjectName("label_mountPointl")
        self.gridLayout_EnableStreaming.addWidget(self.label_mountPointl, 2, 0, 1, 1)
        self.lineEdit_mountPoint = QtGui.QLineEdit(self.layoutWidget_7)
        self.lineEdit_mountPoint.setObjectName("lineEdit_mountPoint")
        self.gridLayout_EnableStreaming.addWidget(self.lineEdit_mountPoint, 2, 1, 1, 1)
        self.label_port = QtGui.QLabel(self.layoutWidget_7)
        self.label_port.setObjectName("label_port")
        self.gridLayout_EnableStreaming.addWidget(self.label_port, 1, 0, 1, 1)
        self.lineEdit_port = QtGui.QLineEdit(self.layoutWidget_7)
        self.lineEdit_port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.gridLayout_EnableStreaming.addWidget(self.lineEdit_port, 1, 1, 1, 1)
        self.label_URL_IP = QtGui.QLabel(self.layoutWidget_7)
        self.label_URL_IP.setObjectName("label_URL_IP")
        self.gridLayout_EnableStreaming.addWidget(self.label_URL_IP, 0, 0, 1, 1)
        self.label_password = QtGui.QLabel(self.layoutWidget_7)
        self.label_password.setObjectName("label_password")
        self.gridLayout_EnableStreaming.addWidget(self.label_password, 3, 0, 1, 1)
        self.label_check_4 = QtGui.QLabel(self.layoutWidget_7)
        self.label_check_4.setText("")
        self.label_check_4.setPixmap(QtGui.QPixmap(":/streamingCheck/unknow.png"))
        self.label_check_4.setObjectName("label_check_4")
        self.gridLayout_EnableStreaming.addWidget(self.label_check_4, 3, 2, 1, 1)
        self.label_check_3 = QtGui.QLabel(self.layoutWidget_7)
        self.label_check_3.setText("")
        self.label_check_3.setPixmap(QtGui.QPixmap(":/streamingCheck/unknow.png"))
        self.label_check_3.setScaledContents(False)
        self.label_check_3.setObjectName("label_check_3")
        self.gridLayout_EnableStreaming.addWidget(self.label_check_3, 2, 2, 1, 1)
        self.label_check_2 = QtGui.QLabel(self.layoutWidget_7)
        self.label_check_2.setText("")
        self.label_check_2.setPixmap(QtGui.QPixmap(":/streamingCheck/unknow.png"))
        self.label_check_2.setObjectName("label_check_2")
        self.gridLayout_EnableStreaming.addWidget(self.label_check_2, 1, 2, 1, 1)
        self.label_check_1 = QtGui.QLabel(self.layoutWidget_7)
        self.label_check_1.setText("")
        self.label_check_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_check_1.setPixmap(QtGui.QPixmap(":/streamingCheck/unknow.png"))
        self.label_check_1.setScaledContents(False)
        self.label_check_1.setObjectName("label_check_1")
        self.gridLayout_EnableStreaming.addWidget(self.label_check_1, 0, 2, 1, 1)
        self.lineEdit_URL_IP = QtGui.QLineEdit(self.layoutWidget_7)
        self.lineEdit_URL_IP.setText("")
        self.lineEdit_URL_IP.setObjectName("lineEdit_URL_IP")
        self.gridLayout_EnableStreaming.addWidget(self.lineEdit_URL_IP, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(32, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_EnableStreaming.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(1, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridLayout_EnableStreaming.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(1, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_EnableStreaming.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(1, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_EnableStreaming.addItem(spacerItem3, 2, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(1, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_EnableStreaming.addItem(spacerItem4, 3, 3, 1, 1)
        self.pushButton_testStreaming = QtGui.QPushButton(self.groupBox_enableStreaming)
        self.pushButton_testStreaming.setEnabled(False)
        self.pushButton_testStreaming.setGeometry(QtCore.QRect(430, 320, 96, 28))
        self.pushButton_testStreaming.setObjectName("pushButton_testStreaming")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox_enableStreaming)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 521, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_streamingQualityList = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_streamingQualityList.setObjectName("comboBox_streamingQualityList")
        self.comboBox_streamingQualityList.addItem("")
        self.comboBox_streamingQualityList.addItem("")
        self.comboBox_streamingQualityList.addItem("")
        self.comboBox_streamingQualityList.addItem("")
        self.comboBox_streamingQualityList.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_streamingQualityList)
        self.configureTab.addTab(self.tab, "")
        self.Extrasetting = QtGui.QWidget()
        self.Extrasetting.setObjectName("Extrasetting")
        self.groupBox_autoHide = QtGui.QGroupBox(self.Extrasetting)
        self.groupBox_autoHide.setGeometry(QtCore.QRect(20, 20, 511, 80))
        self.groupBox_autoHide.setObjectName("groupBox_autoHide")
        self.checkbox_autoHide = QtGui.QCheckBox(self.groupBox_autoHide)
        self.checkbox_autoHide.setGeometry(QtCore.QRect(10, 20, 491, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_autoHide.sizePolicy().hasHeightForWidth())
        self.checkbox_autoHide.setSizePolicy(sizePolicy)
        self.checkbox_autoHide.setMinimumSize(QtCore.QSize(0, 0))
        self.checkbox_autoHide.setMaximumSize(QtCore.QSize(16777215, 64))
        self.checkbox_autoHide.setChecked(True)
        self.checkbox_autoHide.setObjectName("checkbox_autoHide")
        self.groupBox_shortKeys = QtGui.QGroupBox(self.Extrasetting)
        self.groupBox_shortKeys.setGeometry(QtCore.QRect(20, 100, 511, 131))
        self.groupBox_shortKeys.setObjectName("groupBox_shortKeys")
        self.layoutWidget_4 = QtGui.QWidget(self.groupBox_shortKeys)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 30, 501, 101))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_Shorkeys = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_Shorkeys.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_Shorkeys.setObjectName("gridLayout_Shorkeys")
        self.label_record = QtGui.QLabel(self.layoutWidget_4)
        self.label_record.setIndent(15)
        self.label_record.setObjectName("label_record")
        self.gridLayout_Shorkeys.addWidget(self.label_record, 0, 0, 1, 1)
        self.label_stop = QtGui.QLabel(self.layoutWidget_4)
        self.label_stop.setIndent(15)
        self.label_stop.setObjectName("label_stop")
        self.gridLayout_Shorkeys.addWidget(self.label_stop, 1, 0, 1, 1)
        self.lineEdit_recordKey = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_recordKey.setObjectName("lineEdit_recordKey")
        self.gridLayout_Shorkeys.addWidget(self.lineEdit_recordKey, 0, 1, 1, 1)
        self.lineEdit_stopKey = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_stopKey.setObjectName("lineEdit_stopKey")
        self.gridLayout_Shorkeys.addWidget(self.lineEdit_stopKey, 1, 1, 1, 1)
        self.pushButton_recodrdKey = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButton_recodrdKey.setObjectName("pushButton_recodrdKey")
        self.gridLayout_Shorkeys.addWidget(self.pushButton_recodrdKey, 0, 2, 1, 1)
        self.pushButton_StopKey = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButton_StopKey.setObjectName("pushButton_StopKey")
        self.gridLayout_Shorkeys.addWidget(self.pushButton_StopKey, 1, 2, 1, 1)
        self.groupBox_location = QtGui.QGroupBox(self.Extrasetting)
        self.groupBox_location.setGeometry(QtCore.QRect(20, 250, 511, 141))
        self.groupBox_location.setObjectName("groupBox_location")
        self.layoutWidget_5 = QtGui.QWidget(self.groupBox_location)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 30, 501, 101))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_Location = QtGui.QGridLayout(self.layoutWidget_5)
        self.gridLayout_Location.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_Location.setObjectName("gridLayout_Location")
        self.pushButton_open = QtGui.QToolButton(self.layoutWidget_5)
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout_Location.addWidget(self.pushButton_open, 0, 2, 1, 1)
        self.label_videoDirectory = QtGui.QLabel(self.layoutWidget_5)
        self.label_videoDirectory.setIndent(15)
        self.label_videoDirectory.setObjectName("label_videoDirectory")
        self.gridLayout_Location.addWidget(self.label_videoDirectory, 0, 0, 1, 1)
        self.lineEdit_videoDirectory = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_videoDirectory.setObjectName("lineEdit_videoDirectory")
        self.gridLayout_Location.addWidget(self.lineEdit_videoDirectory, 0, 1, 1, 1)
        self.configureTab.addTab(self.Extrasetting, "")
        self.layoutWidget = QtGui.QWidget(ConfigureTool)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 450, 331, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_Apply_Reset = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_Apply_Reset.setObjectName("horizontalLayout_Apply_Reset")
        self.pushButton_reset = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_Apply_Reset.addWidget(self.pushButton_reset)
        self.pushButton_apply = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_apply.setMouseTracking(False)
        self.pushButton_apply.setDefault(False)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_Apply_Reset.addWidget(self.pushButton_apply)
        self.label_soundSource.setBuddy(self.comboBox_audioSourceList)
        self.label_videoQuality.setBuddy(self.comboBox_videoQualityList)
        self.label_mountPointl.setBuddy(self.lineEdit_mountPoint)
        self.label_port.setBuddy(self.lineEdit_port)
        self.label_URL_IP.setBuddy(self.lineEdit_URL_IP)
        self.label_password.setBuddy(self.lineEdit_password)
        self.label.setBuddy(self.comboBox_streamingQualityList)
        self.label_record.setBuddy(self.lineEdit_recordKey)
        self.label_stop.setBuddy(self.lineEdit_stopKey)
        self.label_videoDirectory.setBuddy(self.lineEdit_videoDirectory)

        self.retranslateUi(ConfigureTool)
        self.configureTab.setCurrentIndex(2)
        QtCore.QObject.connect(self.radioButton_recordLocalArea, QtCore.SIGNAL("toggled(bool)"), self.pushButton_setArea.setEnabled)
        QtCore.QObject.connect(self.radioButton_localDesktop, QtCore.SIGNAL("toggled(bool)"), self.groupBox_localDesktopBox.setVisible)
        QtCore.QObject.connect(self.radioButton_hardware, QtCore.SIGNAL("toggled(bool)"), self.groupBox_hardware.setVisible)
        QtCore.QObject.connect(self.groupBox_enableStreaming, QtCore.SIGNAL("toggled(bool)"), self.pushButton_testStreaming.setEnabled)
        QtCore.QObject.connect(self.lineEdit_URL_IP, QtCore.SIGNAL("textChanged(QString)"), self.label_check_1.show)
        QtCore.QObject.connect(self.lineEdit_port, QtCore.SIGNAL("textChanged(QString)"), self.label_check_2.show)
        QtCore.QObject.connect(self.lineEdit_mountPoint, QtCore.SIGNAL("textChanged(QString)"), self.label_check_3.show)
        QtCore.QObject.connect(self.lineEdit_password, QtCore.SIGNAL("textChanged(QString)"), self.label_check_4.show)
        QtCore.QMetaObject.connectSlotsByName(ConfigureTool)
        ConfigureTool.setTabOrder(self.configureTab, self.pushButton_reset)
        ConfigureTool.setTabOrder(self.pushButton_reset, self.pushButton_apply)
        ConfigureTool.setTabOrder(self.pushButton_apply, self.groupBox_videoSource)
        ConfigureTool.setTabOrder(self.groupBox_videoSource, self.radioButton_localDesktop)
        ConfigureTool.setTabOrder(self.radioButton_localDesktop, self.radioButton_hardware)
        ConfigureTool.setTabOrder(self.radioButton_hardware, self.radioButton_recordLocalDesktop)
        ConfigureTool.setTabOrder(self.radioButton_recordLocalDesktop, self.radioButton_recordLocalArea)
        ConfigureTool.setTabOrder(self.radioButton_recordLocalArea, self.radioButton_recordLocalWindow)
        ConfigureTool.setTabOrder(self.radioButton_recordLocalWindow, self.pushButton_setArea)
        ConfigureTool.setTabOrder(self.pushButton_setArea, self.radioButton_USBsrc)
        ConfigureTool.setTabOrder(self.radioButton_USBsrc, self.radioButton_firewiresrc)
        ConfigureTool.setTabOrder(self.radioButton_firewiresrc, self.comboBox_videoDeviceList)
        ConfigureTool.setTabOrder(self.comboBox_videoDeviceList, self.groupBox_soundSource)
        ConfigureTool.setTabOrder(self.groupBox_soundSource, self.comboBox_audioSourceList)
        ConfigureTool.setTabOrder(self.comboBox_audioSourceList, self.checkbox_autoHide)
        ConfigureTool.setTabOrder(self.checkbox_autoHide, self.lineEdit_recordKey)
        ConfigureTool.setTabOrder(self.lineEdit_recordKey, self.pushButton_recodrdKey)
        ConfigureTool.setTabOrder(self.pushButton_recodrdKey, self.lineEdit_stopKey)
        ConfigureTool.setTabOrder(self.lineEdit_stopKey, self.pushButton_StopKey)
        ConfigureTool.setTabOrder(self.pushButton_StopKey, self.lineEdit_videoDirectory)
        ConfigureTool.setTabOrder(self.lineEdit_videoDirectory, self.pushButton_open)

    def retranslateUi(self, ConfigureTool):
        ConfigureTool.setWindowTitle(QtGui.QApplication.translate("ConfigureTool", "Freeseer Config Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_videoSource.setTitle(QtGui.QApplication.translate("ConfigureTool", "Enable Video Recoding", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_localDesktop.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select this option to record the local desktop. \n"
"Freeseer currently only supports recording the full desktop. \n"
"We plan to support window and area modes in future versions.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_localDesktop.setText(QtGui.QApplication.translate("ConfigureTool", "&Local Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_hardware.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select hardware to record from either a usb device or firewire device.\n"
"\n"
"Freeseer finds USB devices by scanning /dev/videoX starting from index 0.\n"
"\n"
"Freeseer finds Firewire devices by scanning /dev/fwX starting from index 1.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_hardware.setText(QtGui.QApplication.translate("ConfigureTool", "&Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_localDesktopBox.setTitle(QtGui.QApplication.translate("ConfigureTool", "Local Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalDesktop.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select this option to record the entire desktop.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalDesktop.setText(QtGui.QApplication.translate("ConfigureTool", "&Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalArea.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select this option to record an small area of the desktop.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalArea.setText(QtGui.QApplication.translate("ConfigureTool", "&Area", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalWindow.setToolTip(QtGui.QApplication.translate("ConfigureTool", "This feature is currently not yet implemented.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_recordLocalWindow.setText(QtGui.QApplication.translate("ConfigureTool", "&Window (Not Supported)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setArea.setText(QtGui.QApplication.translate("ConfigureTool", "Set Area", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_hardware.setTitle(QtGui.QApplication.translate("ConfigureTool", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_USBsrc.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Use this option to record from a usb device.\n"
"\n"
"This option tries the v4l2src driver\n"
"and falls back to the v4lsrc driver if\n"
"v4l2src does not work.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_USBsrc.setText(QtGui.QApplication.translate("ConfigureTool", "&usb device", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_firewiresrc.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Firewire mode uses dv1394src as the video driver.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_firewiresrc.setText(QtGui.QApplication.translate("ConfigureTool", "&firewire device", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoDeviceList.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select the video device to record from.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_soundSource.setTitle(QtGui.QApplication.translate("ConfigureTool", "Enable Sound Recoding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_soundSource.setText(QtGui.QApplication.translate("ConfigureTool", "&Sound Source", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_audioSourceList.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Select the audio source to use for recording.", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTab.setTabText(self.configureTab.indexOf(self.SourceSetting), QtGui.QApplication.translate("ConfigureTool", "Source Setting ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_videoQuality.setTitle(QtGui.QApplication.translate("ConfigureTool", "Video Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.label_videoQuality.setText(QtGui.QApplication.translate("ConfigureTool", "Video Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(0, QtGui.QApplication.translate("ConfigureTool", "NONE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(1, QtGui.QApplication.translate("ConfigureTool", "640x480", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(2, QtGui.QApplication.translate("ConfigureTool", "800x600", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(3, QtGui.QApplication.translate("ConfigureTool", "1024x768", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(4, QtGui.QApplication.translate("ConfigureTool", "1280x800", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_videoQualityList.setItemText(5, QtGui.QApplication.translate("ConfigureTool", "1920x1080", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_derectScreenResoltion.setText(QtGui.QApplication.translate("ConfigureTool", "&Detect screen resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_screenResolution.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ConfigureTool", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTab.setTabText(self.configureTab.indexOf(self.Videosetting), QtGui.QApplication.translate("ConfigureTool", "Video setting", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_enableStreaming.setTitle(QtGui.QApplication.translate("ConfigureTool", "&Enable Streaming", None, QtGui.QApplication.UnicodeUTF8))
        self.label_mountPointl.setText(QtGui.QApplication.translate("ConfigureTool", "&Mount point", None, QtGui.QApplication.UnicodeUTF8))
        self.label_port.setText(QtGui.QApplication.translate("ConfigureTool", "&Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_URL_IP.setText(QtGui.QApplication.translate("ConfigureTool", "&URL/IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_password.setText(QtGui.QApplication.translate("ConfigureTool", "&Password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_testStreaming.setText(QtGui.QApplication.translate("ConfigureTool", "&Test", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigureTool", "Streaming Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_streamingQualityList.setItemText(0, QtGui.QApplication.translate("ConfigureTool", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_streamingQualityList.setItemText(1, QtGui.QApplication.translate("ConfigureTool", "480x360", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_streamingQualityList.setItemText(2, QtGui.QApplication.translate("ConfigureTool", "640x480", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_streamingQualityList.setItemText(3, QtGui.QApplication.translate("ConfigureTool", "1280x720", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_streamingQualityList.setItemText(4, QtGui.QApplication.translate("ConfigureTool", "1920x1080", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTab.setTabText(self.configureTab.indexOf(self.tab), QtGui.QApplication.translate("ConfigureTool", "Steaming setting", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_autoHide.setTitle(QtGui.QApplication.translate("ConfigureTool", "Auto Hide", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_autoHide.setToolTip(QtGui.QApplication.translate("ConfigureTool", "Enables auto-hide to system tray.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_autoHide.setText(QtGui.QApplication.translate("ConfigureTool", "&Enable Auto-Hide", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_shortKeys.setTitle(QtGui.QApplication.translate("ConfigureTool", "ShortKeys", None, QtGui.QApplication.UnicodeUTF8))
        self.label_record.setText(QtGui.QApplication.translate("ConfigureTool", "&Record", None, QtGui.QApplication.UnicodeUTF8))
        self.label_stop.setText(QtGui.QApplication.translate("ConfigureTool", "&Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_recodrdKey.setText(QtGui.QApplication.translate("ConfigureTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_StopKey.setText(QtGui.QApplication.translate("ConfigureTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_location.setTitle(QtGui.QApplication.translate("ConfigureTool", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open.setText(QtGui.QApplication.translate("ConfigureTool", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_videoDirectory.setText(QtGui.QApplication.translate("ConfigureTool", "&Video Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.configureTab.setTabText(self.configureTab.indexOf(self.Extrasetting), QtGui.QApplication.translate("ConfigureTool", "Extra setting", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("ConfigureTool", "&Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_apply.setText(QtGui.QApplication.translate("ConfigureTool", "&Apply", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
