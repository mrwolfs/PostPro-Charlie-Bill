# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/charlie/python/PostPro/Form1.ui'
#
# Created: Sun Nov 25 16:15:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1045, 546)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/shinke2n.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.InputTextEdit = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTextEdit.sizePolicy().hasHeightForWidth())
        self.InputTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.InputTextEdit.setFont(font)
        self.InputTextEdit.setAcceptRichText(True)
        self.InputTextEdit.setObjectName(_fromUtf8("InputTextEdit"))
        self.horizontalLayout_2.addWidget(self.InputTextEdit)
        self.verticalSlider = Qslid(self.tab)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.horizontalLayout_2.addWidget(self.verticalSlider)
        self.splitter = QtGui.QSplitter(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.BouttonCalcul = QtGui.QPushButton(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BouttonCalcul.sizePolicy().hasHeightForWidth())
        self.BouttonCalcul.setSizePolicy(sizePolicy)
        self.BouttonCalcul.setObjectName(_fromUtf8("BouttonCalcul"))
        self.BouttonEffacer = QtGui.QPushButton(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BouttonEffacer.sizePolicy().hasHeightForWidth())
        self.BouttonEffacer.setSizePolicy(sizePolicy)
        self.BouttonEffacer.setObjectName(_fromUtf8("BouttonEffacer"))
        self.BoutonPrevusalisation = QtGui.QPushButton(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonPrevusalisation.sizePolicy().hasHeightForWidth())
        self.BoutonPrevusalisation.setSizePolicy(sizePolicy)
        self.BoutonPrevusalisation.setObjectName(_fromUtf8("BoutonPrevusalisation"))
        self.kpixmapregionselectorwidget = KPixmapRegionSelectorWidget(self.splitter)
        self.kpixmapregionselectorwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kpixmapregionselectorwidget.sizePolicy().hasHeightForWidth())
        self.kpixmapregionselectorwidget.setSizePolicy(sizePolicy)
        self.kpixmapregionselectorwidget.setToolTip(_fromUtf8(""))
        self.kpixmapregionselectorwidget.setStatusTip(_fromUtf8(""))
        self.kpixmapregionselectorwidget.setWhatsThis(_fromUtf8(""))
        self.kpixmapregionselectorwidget.setAccessibleName(_fromUtf8(""))
        self.kpixmapregionselectorwidget.setAccessibleDescription(_fromUtf8(""))
        self.kpixmapregionselectorwidget.setAutoFillBackground(False)
        self.kpixmapregionselectorwidget.setPixmap(QtGui.QPixmap(_fromUtf8("image/shinke2n.png")))
        self.kpixmapregionselectorwidget.setObjectName(_fromUtf8("kpixmapregionselectorwidget"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalSlider_2 = QtGui.QSlider(self.tab)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setInvertedAppearance(True)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.horizontalLayout_2.addWidget(self.verticalSlider_2)
        self.TransformTextEdit = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TransformTextEdit.sizePolicy().hasHeightForWidth())
        self.TransformTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TransformTextEdit.setFont(font)
        self.TransformTextEdit.setObjectName(_fromUtf8("TransformTextEdit"))
        self.horizontalLayout_2.addWidget(self.TransformTextEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spinBox = QtGui.QSpinBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 168, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 168, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(205, 200, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.spinBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setWrapping(False)
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox.setMaximum(9999999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 168, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 168, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(205, 200, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.spinBox_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spinBox_2.setMaximum(9999999)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.progressBar = QtGui.QProgressBar(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(205, 200, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        self.progressBar.setMaximum(28)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.comboBoxUnite = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUnite.sizePolicy().hasHeightForWidth())
        self.comboBoxUnite.setSizePolicy(sizePolicy)
        self.comboBoxUnite.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBoxUnite.setObjectName(_fromUtf8("comboBoxUnite"))
        self.comboBoxUnite.addItem(_fromUtf8(""))
        self.comboBoxUnite.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBoxUnite)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.comboBoxType = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxType.sizePolicy().hasHeightForWidth())
        self.comboBoxType.setSizePolicy(sizePolicy)
        self.comboBoxType.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBoxType.setObjectName(_fromUtf8("comboBoxType"))
        self.comboBoxType.addItem(_fromUtf8(""))
        self.comboBoxType.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBoxType)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.comboBoxPlan = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPlan.sizePolicy().hasHeightForWidth())
        self.comboBoxPlan.setSizePolicy(sizePolicy)
        self.comboBoxPlan.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBoxPlan.setObjectName(_fromUtf8("comboBoxPlan"))
        self.comboBoxPlan.addItem(_fromUtf8(""))
        self.comboBoxPlan.addItem(_fromUtf8(""))
        self.comboBoxPlan.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.comboBoxPlan)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.comboBoxCoordonees = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCoordonees.sizePolicy().hasHeightForWidth())
        self.comboBoxCoordonees.setSizePolicy(sizePolicy)
        self.comboBoxCoordonees.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBoxCoordonees.setObjectName(_fromUtf8("comboBoxCoordonees"))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.comboBoxCoordonees.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.comboBoxCoordonees)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_7.addWidget(self.checkBox)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMargin(0)
        self.label_5.setIndent(100)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.HeadertextEdit = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeadertextEdit.sizePolicy().hasHeightForWidth())
        self.HeadertextEdit.setSizePolicy(sizePolicy)
        self.HeadertextEdit.setObjectName(_fromUtf8("HeadertextEdit"))
        self.verticalLayout_3.addWidget(self.HeadertextEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setIndent(100)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.EnderTextEdit = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnderTextEdit.sizePolicy().hasHeightForWidth())
        self.EnderTextEdit.setSizePolicy(sizePolicy)
        self.EnderTextEdit.setObjectName(_fromUtf8("EnderTextEdit"))
        self.verticalLayout_4.addWidget(self.EnderTextEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.kpixmapregionselectorwidget_2 = KPixmapRegionSelectorWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kpixmapregionselectorwidget_2.sizePolicy().hasHeightForWidth())
        self.kpixmapregionselectorwidget_2.setSizePolicy(sizePolicy)
        self.kpixmapregionselectorwidget_2.setPixmap(QtGui.QPixmap(_fromUtf8("image/hye4putk.png")))
        self.kpixmapregionselectorwidget_2.setObjectName(_fromUtf8("kpixmapregionselectorwidget_2"))
        self.horizontalLayout_11.addWidget(self.kpixmapregionselectorwidget_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName(_fromUtf8("menuA_propos"))
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName(_fromUtf8("menuAide"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionEnregistrer = QtGui.QAction(MainWindow)
        self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionOuvrir_et_pr_visualiser = QtGui.QAction(MainWindow)
        self.actionOuvrir_et_pr_visualiser.setObjectName(_fromUtf8("actionOuvrir_et_pr_visualiser"))
        self.actionEnregistrer_sous = QtGui.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName(_fromUtf8("actionEnregistrer_sous"))
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionOuvrir_et_pr_visualiser)
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Post-Processeur", None, QtGui.QApplication.UnicodeUTF8))
        self.BouttonCalcul.setText(QtGui.QApplication.translate("MainWindow", "Calculer", None, QtGui.QApplication.UnicodeUTF8))
        self.BouttonEffacer.setText(QtGui.QApplication.translate("MainWindow", "Effacer", None, QtGui.QApplication.UnicodeUTF8))
        self.BoutonPrevusalisation.setText(QtGui.QApplication.translate("MainWindow", "Prévisualiser", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Calculer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Paramètres Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxUnite.setItemText(0, QtGui.QApplication.translate("MainWindow", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxUnite.setItemText(1, QtGui.QApplication.translate("MainWindow", "Inch", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Unité Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxType.setItemText(0, QtGui.QApplication.translate("MainWindow", "Absolues", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxType.setItemText(1, QtGui.QApplication.translate("MainWindow", "Relatifs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Types de déplacements", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPlan.setItemText(0, QtGui.QApplication.translate("MainWindow", "XY", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPlan.setItemText(1, QtGui.QApplication.translate("MainWindow", "XZ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPlan.setItemText(2, QtGui.QApplication.translate("MainWindow", "YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Choix du plan de travail", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(0, QtGui.QApplication.translate("MainWindow", "Origine piece 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(1, QtGui.QApplication.translate("MainWindow", "Origine piece 2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(2, QtGui.QApplication.translate("MainWindow", "Origine piece 3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(3, QtGui.QApplication.translate("MainWindow", "Origine piece 4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(4, QtGui.QApplication.translate("MainWindow", "Origine piece 5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(5, QtGui.QApplication.translate("MainWindow", "Origine piece 6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(6, QtGui.QApplication.translate("MainWindow", "Origine piece 7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(7, QtGui.QApplication.translate("MainWindow", "Origine piece 8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCoordonees.setItemText(8, QtGui.QApplication.translate("MainWindow", "Origine piece 9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Choix du système de coordonnées", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Vitesse rapide pour la simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Header", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ender", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Paramètres", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_propos.setTitle(QtGui.QApplication.translate("MainWindow", "A propos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAide.setTitle(QtGui.QApplication.translate("MainWindow", "Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuvrir.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setText(QtGui.QApplication.translate("MainWindow", "Enregistrer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuvrir_et_pr_visualiser.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir et prévisualiser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer_sous.setText(QtGui.QApplication.translate("MainWindow", "Enregistrer sous", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KPixmapRegionSelectorWidget
from qslid import Qslid

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

