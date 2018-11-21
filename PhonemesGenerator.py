
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
class Window(QtGui.QMainWindow):
    def __init__(self):
        sfm.SetCurrentFrame( 0 )
        super(Window, self).__init__()
        self.setWindowTitle("Phoneme Generator For SFM")
        self.setGeometry(400, 300, 1000, 500)   
        self.setFixedSize(1000, 500)
        extractAction = QtGui.QAction('Close', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave Source Filmmaker')
        extractAction.triggered.connect(self.close)
        SaveextractAction = QtGui.QAction('Save and Exit', self)
        SaveextractAction.setShortcut('Ctrl+Shift+Q')
        SaveextractAction.setStatusTip('Leave Source Filmmaker and save')
        SaveextractAction.triggered.connect(self.saveclose)
        LoadMapAction = QtGui.QAction('Load Map', self)
        LoadMapAction.setShortcut('Ctrl+L')
        LoadMapAction.setStatusTip('Load a map')
        LoadMapAction.triggered.connect(self.LoadMap)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu= mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(SaveextractAction)
        fileMenu.addAction(LoadMapAction)

        

       
 
        self.welcome()

    def welcome(self):
 
        shot = sfm.GetCurrentShot()

        
        l1 = QtGui.QLabel(self)
        l1.setText('Animation Set Selected :')
        l1.setGeometry(450, 5, 300, 100)
        l2 = QtGui.QLabel(self)
        l2.setText('Script by Combo Studios.')
        l2.setGeometry(445, 410, 300, 100)

        global AnimSets

        comboBox = QtGui.QComboBox(self)
        shot = sfm.GetCurrentShot()
        AnimSets = sfm.GetCurrentAnimationSet()
        sfm.SetCurrentFrame( 0 )
        print(shot)
        print(AnimSets)
        global AnimSetsname
        AnimSetsname = str(AnimSets.name)
        comboBox.addItem(AnimSetsname)
        comboBox.move(460, 80)
        comboBox.size()

        comboBox.setStyleSheet('''*    
        QComboBox QAbstractItemView 
        {
        min-width: 150px;
        }
        ''')

        l3 = QtGui.QLabel(self)
        l3.setText('Hey there! If you have the script, you are not allowed to share it unless, me, the creator says yes.')
        l3.setGeometry(300, 100, 500, 100)



        btnQuit = QtGui.QPushButton("Quit SFM", self)
        btnQuit.clicked.connect(self.close)
        btnQuit.resize(90,25)
        btnQuit.move(0, 455)
            


        btnNext1 = QtGui.QPushButton("Next", self)
        btnNext1.clicked.connect(self.GeneratePhoneme)
        btnNext1.resize(90,25)
        btnNext1.move(910, 455)           
        self.show()   

        

           
    def GeneratePhoneme(self):
        CDmeAnimationSet.RestoreDefaultPhonemeMap(AnimSets)
        HL2 = QtGui.QMessageBox()
        HL2.setText('Please make sure you created phoneme presets based on HL2 characters. You can do that by right click on your animation set in the Element Viewer.')
        HL2.setIcon(QtGui.QMessageBox.Information)
        HL2.setWindowTitle('WAIT!')
        HL2.exec_()

        self.hide()

        self.wid = QtGui.QWidget()
        self.wid.resize(870, 890)
        self.wid.setWindowTitle('NewWindow')
        self.wid.show()
        l1 = QtGui.QLabel(self.wid)
        l1.setText('Choose the bones and flexes you want to work with. No use for now. The script will do hos job. Please wait.')
        l1.setGeometry(300, -10, 500, 100)
        l1.show()
        controlsarray = AnimSets.controls
        phonememap = movieobjects.CDmeAnimationSet.GetPresetGroups(AnimSets)

        for phonemes in phonememap[1]:

            movieobjects.CDmeCombinationOperator.CopyControls(controlsarray, )




        print(ctrlsstr)
        
        controls = QtGui.QListWidget(self.wid)
        controls.resize(300, 200)
        controls.move(275, 200)
        controls.show()




    def LoadMap(self):
        sfmApp.LoadMap()

    def saveclose(self):
        choicequit = QtGui.QMessageBox.question(self, 'Exit', 'Are you sure you want to quit SFM?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
            sfmApp.SaveDocument()
        else:
            pass
        


    def close(self):
        choicequit = QtGui.QMessageBox.question(self, 'Exit', 'Are you sure you want to quit SFM?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

GUI = Window()

   