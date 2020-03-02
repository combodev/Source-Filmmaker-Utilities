import vsUtils
import random
import sfm 
from PySide import *
import sfmApp
import sys
import sfmUtils
import ast,re
from vs import *
import time
from PySide import QtCore, QtGui

AnimSets = []


class Window(QtGui.QMainWindow):
    def __init__(self):
        sfm.SetCurrentFrame( 0 )
        super(Window, self).__init__()
        self.setWindowTitle("Phoneme Generator")
        self.setGeometry(400, 300, 1000, 500)
        #self.setFixedSize(1000, 500)   
        self.welcome()


    def setupUi(self, PhonemeWindow):
        PhonemeWindow.setObjectName("PhonemeWindow")
        PhonemeWindow.resize(495, 189)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhonemeWindow.sizePolicy().hasHeightForWidth())
        PhonemeWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(PhonemeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l1 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l1.sizePolicy().hasHeightForWidth())
        self.l1.setSizePolicy(sizePolicy)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setWordWrap(False)
        self.l1.setMargin(0)
        self.l1.setObjectName("l1")
        self.gridLayout_2.addWidget(self.l1, 0, 0, 1, 1)
        self.animSetComboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.animSetComboBox.sizePolicy().hasHeightForWidth())
        self.animSetComboBox.setSizePolicy(sizePolicy)
        self.animSetComboBox.setObjectName("animSetComboBox")
        self.gridLayout_2.addWidget(self.animSetComboBox, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        self.l2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l2.sizePolicy().hasHeightForWidth())
        self.l2.setSizePolicy(sizePolicy)
        self.l2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.gridLayout_2.addWidget(self.l2, 5, 0, 1, 1)
        self.l3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l3.sizePolicy().hasHeightForWidth())
        self.l3.setSizePolicy(sizePolicy)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.gridLayout_2.addWidget(self.l3, 6, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)
        PhonemeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PhonemeWindow)
        self.statusbar.setObjectName("statusbar")
        PhonemeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PhonemeWindow)
        QtCore.QMetaObject.connectSlotsByName(PhonemeWindow)

    def retranslateUi(self, PhonemeWindow):
        PhonemeWindow.setWindowTitle(QtGui.QApplication.translate("PhonemeWindow", "Phoneme Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.l1.setText(QtGui.QApplication.translate("PhonemeWindow", "Please select the Animation Set you want to create phonemes for.", None, QtGui.QApplication.UnicodeUTF8))
        self.l2.setText(QtGui.QApplication.translate("PhonemeWindow", "Script By ComboDev", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PhonemeWindow", "Leave Window", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("PhonemeWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.l3.setText(QtGui.QApplication.translate("PhonemeWindow", "Hey there! If you have the script, you are not allowed to share it unless, me, the creator says yes.", None, QtGui.QApplication.UnicodeUTF8))

    def setupControlUi(self, controlWindow):
        controlWindow.setObjectName("controlWindow")
        controlWindow.resize(571, 363)
        self.centralwidget = QtGui.QWidget(controlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        self.line2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        self.line2.setFrameShape(QtGui.QFrame.HLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 7, 1, 1, 1)
        self.selectControlsLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectControlsLabel.sizePolicy().hasHeightForWidth())
        self.selectControlsLabel.setSizePolicy(sizePolicy)
        self.selectControlsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectControlsLabel.setObjectName("selectControlsLabel")
        self.gridLayout.addWidget(self.selectControlsLabel, 0, 1, 1, 1)
        self.selectToUse = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectToUse.sizePolicy().hasHeightForWidth())
        self.selectToUse.setSizePolicy(sizePolicy)
        self.selectToUse.setObjectName("selectToUse")
        self.gridLayout.addWidget(self.selectToUse, 5, 1, 1, 1)
        self.selectToNotUse = QtGui.QPushButton(self.centralwidget)
        self.selectToNotUse.setObjectName("selectToNotUse")
        self.gridLayout.addWidget(self.selectToNotUse, 6, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 1, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 8, 1, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 2, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 9, 1, 1, 1)
        self.ControlsDoneButton = QtGui.QPushButton(self.centralwidget)
        self.ControlsDoneButton.setObjectName("ControlsDoneButton")
        self.gridLayout.addWidget(self.ControlsDoneButton, 10, 1, 1, 1)
        controlWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(controlWindow)
        self.statusbar.setObjectName("statusbar")
        controlWindow.setStatusBar(self.statusbar)

        self.retranslateControlUi(controlWindow)
        QtCore.QMetaObject.connectSlotsByName(controlWindow)

    def retranslateControlUi(self, controlWindow):
        controlWindow.setWindowTitle(QtGui.QApplication.translate("controlWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.selectControlsLabel.setText(QtGui.QApplication.translate("controlWindow", "Select ONLY the controls you want to use.", None, QtGui.QApplication.UnicodeUTF8))
        self.selectToUse.setText(QtGui.QApplication.translate("controlWindow", "Move Down", None, QtGui.QApplication.UnicodeUTF8))
        self.selectToNotUse.setText(QtGui.QApplication.translate("controlWindow", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.ControlsDoneButton.setText(QtGui.QApplication.translate("controlWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))



    def welcome(self):
        shot = sfm.GetCurrentShot()
        print(shot)
        self.setupUi(self)

        if(shot == None):
            shotError = QtGui.QMessageBox()
            shotError.setText("Couldn't get current shot. Make sure you run this script from the \"Rig\" menu of an animation set.")
            shotError.setIcon(QtGui.QMessageBox.Critical)
            shotError.setWindowTitle('Uh...')
            shotError.exec_()
            self.close()
            return

        for shotAttribute in shot.iterAttrs():
            if shotAttribute.GetName() == "animationSets": 
                for animSet in shotAttribute:
                    AnimSets.append(animSet)
                break
            
        if AnimSets is None:
            setAnimSet = QtGui.QMessageBox()
            setAnimSet.setText("There is not any Animation Set in the scene!")
            setAnimSet.setIcon(QtGui.QMessageBox.Critical)
            setAnimSet.setWindowTitle('Uh...')
            setAnimSet.exec_()
            self.close()
            return
        sfm.SetCurrentFrame( 0 )
        print(shot)
        print(AnimSets)

        for AnimSet in AnimSets:
            self.animSetComboBox.addItem(str(AnimSet.name))

        self.pushButton.clicked.connect(self.Close)
        self.pushButton_2.clicked.connect(self.ControlSelection)

        self.show()   
        

           
    def ControlSelection(self):
        global currentAnimationSet
        currentAnimationSet = AnimSets[self.animSetComboBox.currentIndex()]
        print currentAnimationSet
        global controls
        controls = []
        for attribute in currentAnimationSet.iterAttrs():
            if attribute.GetName() == "controls":
                for control in attribute:
                    controls.append(control)
        
        #Phoneme Setup Init
        currentAnimationSet.RestoreDefaultPhonemeMap()
        HL2 = QtGui.QMessageBox()
        HL2.setText("Please make sure you create a phoneme preset based on HL2 FACS controls or the program will crash. You can do that by right clicking your animation set in the Element Viewer and clicking on \"Create phonemes presets based...\"")
        HL2.setIcon(QtGui.QMessageBox.Warning)
        HL2.setWindowTitle('Do not skip this!')
        hl2_yesButton = HL2.addButton("I did it.", QtGui.QMessageBox.YesRole)
        hl2_noButton = HL2.addButton("Oh, I didn't do it.", QtGui.QMessageBox.NoRole)
        HL2.exec_()
        if HL2.clickedButton() == hl2_noButton:
            HL2_no = QtGui.QMessageBox()
            HL2_no.setText("Please do it first.")
            HL2_no.setIcon(QtGui.QMessageBox.Warning)
            HL2_no.setWindowTitle('Do not skip this!')
            HL2_no.exec_()
            self.close()
            return
        HL2_ = QtGui.QMessageBox()
        HL2_.setText("This step might be automated one day if I figure out how to create them automatically without making SFM crash.")
        HL2_.setIcon(QtGui.QMessageBox.Information)
        HL2_.setWindowTitle('P.S.')
        HL2_.exec_()
                
        
        

        self.hide()

        self.setupControlUi(self)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        
        for control in controls:
            print str(control.name)
            self.listWidget.addItem(str(control.name))

        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        self.controlsToUse = []

        def selectToUseAction():
            for selectedControl in self.listWidget.selectedItems():
                self.listWidget_2.addItem(str(selectedControl.text()))
                self.controlsToUse.append(str(selectedControl.text()))
        
        #!!!
        def selectToNotUseAction():
            for selectedControl in self.listWidget_2.selectedItems():
                del selectedControl

        self.selectToUse.clicked.connect(selectToUseAction)
        self.selectToNotUse.clicked.connect(selectToNotUseAction)
        self.selectToNotUse.clicked.connect(selectToNotUseAction)
        self.ControlsDoneButton.clicked.connect(self.doneWithControls)

        self.show()   

    def doneWithControls(self):
        print '--------------------------------'
        print 'Controls To Use!'
        print '--------------------------------'
        for x in self.controlsToUse:
            print x
        print '--------------------------------'
        seen = []
        for ctrl in self.controlsToUse:
            if ctrl in seen:
                print "Control repeated!"
                shotError = QtGui.QMessageBox()
                shotError.setText("Two Controls have the same name... Did you accidentally move down a control twice?")
                shotError.setIcon(QtGui.QMessageBox.Critical)
                shotError.setWindowTitle('Uh...')
                shotError.exec_()
                self.close()
                return
            else:
                seen.append(ctrl)
        
        tmpArray = self.controlsToUse

        self.controlsToUse = []

        for attribute in currentAnimationSet.iterAttrs():
            if attribute.GetName() == "controls":
                for control in attribute:
                    for x in tmpArray:
                        if control.GetName() == x:
                            self.controlsToUse.append(control)
        print '--------------------------------'
        print 'Controls To Use!'
        print '--------------------------------'
        for x in self.controlsToUse:
            print x
        print '--------------------------------'

        

        self.presetNameArray = []

        phonememap = currentAnimationSet.GetPhonemeMap()
        print help(phonememap)
        for phoneme in range(0,phonememap.Count()):
            self.presetNameArray.append(phoneme.preset)
        
        for presetName in self.presetNameArray:
            for control in self.controlsToUse:
                print presetName
                self.addControlValueToPreset(control, presetName)
                        
    


    def addControlValueToPreset(self, control, presetName):
        
        for attribute in currentAnimationSet.iterAttrs():
            if attribute.GetName() == "presetGroups":
                presetGroupArray = attribute
                for presetGroup in presetGroupArray:
                    if presetGroup.GetName() == "phoneme":
                        phonemePresetGroup = presetGroup
                        print type(presetGroup)
                        phonemePreset = phonemePresetGroup.FindPreset(presetName)
                        phonemePreset.FindOrAddControlValue(control)

    def LoadMap(self):
        sfmApp.LoadMap()
        


    def Close(self):
        choicequit = QtGui.QMessageBox.question(self, 'Exit', 'Are you sure you want to leave this window?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choicequit == QtGui.QMessageBox.Yes:
            self.close()
        else:
            pass

    


GUI = Window()