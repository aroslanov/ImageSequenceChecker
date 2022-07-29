#!/usr/bin/env python
""" This program checks for the missing/broken/suspicious images in
rendered sequence. Here is the list of supported image formats:
<https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html>
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Timur Aroslanov"
__contact__ = "aroslanov@gmail.com"
__copyright__ = "Copyright 2021, Timur Aroslanov"
__date__ = "2022/07/22"
__deprecated__ = False
__email__ = "aroslanov@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Beta"
__version__ = "0.1.1 Beta"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import os, sys

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class Ui_MainWindow(object): 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 355)
        MainWindow.setFixedSize(530, 355)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.path = ''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFileName.setGeometry(QtCore.QRect(10, 30, 471, 21))
        self.lineEditFileName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 350, 16))
        self.label.setObjectName("label")
        self.toolButtonChooseFileName = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonChooseFileName.setGeometry(QtCore.QRect(490, 30, 25, 19))
        self.toolButtonChooseFileName.setObjectName("toolButtonChooseFileName")
        self.toolButtonChooseFileName.clicked.connect(self.chooseFileName)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 131, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEditOutputConsole = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditOutputConsole.setGeometry(QtCore.QRect(10, 210, 511, 121))
        self.plainTextEditOutputConsole.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.plainTextEditOutputConsole.setUndoRedoEnabled(False)
        self.plainTextEditOutputConsole.setReadOnly(True)
        self.plainTextEditOutputConsole.setObjectName("plainTextEditOutputConsole")
        self.checkBoxMissing = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxMissing.setGeometry(QtCore.QRect(10, 60, 220, 17))
        self.checkBoxMissing.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBoxMissing.setObjectName("checkBoxMissing")
        self.checkBoxAnomalies = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAnomalies.setGeometry(QtCore.QRect(10, 80, 260, 17))
        self.checkBoxAnomalies.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBoxAnomalies.setObjectName("checkBoxAnomalies")
        self.pushButtonStartStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartStop.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.pushButtonStartStop.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButtonStartStop.setObjectName("pushButtonStartStop")
        self.pushButtonStartStop.clicked.connect(self.startStop)
        self.lineEditAnomalySize = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAnomalySize.setGeometry(QtCore.QRect(260, 80, 81, 20))
        self.lineEditAnomalySize.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditAnomalySize.setObjectName("lineEditAnomalySize")
        self.checkBoxBroken = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxBroken.setGeometry(QtCore.QRect(10, 100, 200, 17))
        self.checkBoxBroken.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBoxBroken.setObjectName("checkBoxBroken")
        self.checkBoxSaveDefaults = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSaveDefaults.setGeometry(QtCore.QRect(10, 120, 200, 17))
        self.checkBoxSaveDefaults.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBoxSaveDefaults.setObjectName("checkBoxSaveDefaults")
        self.radioButtonBytes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBytes.setGeometry(QtCore.QRect(350, 80, 51, 17))
        self.radioButtonBytes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonBytes.setChecked(False)
        self.radioButtonBytes.setObjectName("radioButtonBytes")
        self.radioButtonKilobytes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonKilobytes.setGeometry(QtCore.QRect(410, 80, 41, 17))
        self.radioButtonKilobytes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonKilobytes.setChecked(True)
        self.radioButtonKilobytes.setObjectName("radioButtonKilobytes")
        self.radioButtonMegabytes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonMegabytes.setGeometry(QtCore.QRect(460, 80, 41, 17))
        self.radioButtonMegabytes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonMegabytes.setObjectName("radioButtonMegabytes")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 170, 511, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditFileName, self.toolButtonChooseFileName)
        MainWindow.setTabOrder(self.toolButtonChooseFileName, self.checkBoxMissing)
        MainWindow.setTabOrder(self.checkBoxMissing, self.checkBoxAnomalies)
        MainWindow.setTabOrder(self.checkBoxAnomalies, self.lineEditAnomalySize)
        MainWindow.setTabOrder(self.lineEditAnomalySize, self.radioButtonBytes)
        MainWindow.setTabOrder(self.radioButtonBytes, self.radioButtonKilobytes)
        MainWindow.setTabOrder(self.radioButtonKilobytes, self.radioButtonMegabytes)
        MainWindow.setTabOrder(self.radioButtonMegabytes, self.checkBoxBroken)
        MainWindow.setTabOrder(self.checkBoxBroken, self.checkBoxSaveDefaults)
        MainWindow.setTabOrder(self.checkBoxSaveDefaults, self.pushButtonStartStop)
        MainWindow.setTabOrder(self.pushButtonStartStop, self.plainTextEditOutputConsole)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image sequence checker"))
        self.label.setText(_translate("MainWindow", "Select image sequence (you may click on any file in sequence):"))
        self.toolButtonChooseFileName.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Output console:"))
        self.checkBoxMissing.setText(_translate("MainWindow", "Check for missing files in a sequence"))
        self.checkBoxAnomalies.setText(_translate("MainWindow", "Check for file size anomalies, threshold is:"))
        self.pushButtonStartStop.setText(_translate("MainWindow", "Start!"))
        self.lineEditAnomalySize.setToolTip(_translate("MainWindow", "Could be in bytes (500000), kilobytes (500K) or megabytes (0.5M)"))
        self.checkBoxBroken.setText(_translate("MainWindow", "Check for broken files (slow)"))
        self.checkBoxSaveDefaults.setText(_translate("MainWindow", "Save current settings as defaults"))
        self.radioButtonBytes.setText(_translate("MainWindow", "bytes"))
        self.radioButtonKilobytes.setText(_translate("MainWindow", "Kb"))
        self.radioButtonMegabytes.setText(_translate("MainWindow", "Mb"))
   


    def chooseFileName(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file sequence', MainWindow.path, 'Image files (*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.gif *.psd *.webp *.pixar *.dds *.j2p *.jpx *.2k)')
        #if sequenceName is not empty, set the file name in the line edit
        if fileName[0] != '':
            self.lineEditFileName.setText(fileName[0])
    
    def startStop(self): #start/stop button

          
         #if lineEditFileName is not empty, and this file exists
        if self.lineEditFileName.text() != '' and os.path.isfile(self.lineEditFileName.text()):
            MainWindow.setEnabled(False) #disable main window
            self.checkSequence() #check the sequence
            self.saveDefaults() #save current settings as defaults
            MainWindow.setEnabled(True) #enable main window

        
        else: #show message box "Please choose a file"
            QtWidgets.QMessageBox.warning(None, "Error", "Please choose a file")
            #print("Please choose a file")
            return
                #if save defaults is checked, save the current settings
        

    def checkSequence(self):
        import sys
        import re
        import glob
        import os
        import PIL
        import itertools
        from PIL import Image
        
        app.setOverrideCursor(Qt.WaitCursor) #show wait cursor

        self.plainTextEditOutputConsole.clear() #clear the output console

        
        path = os.path.dirname(self.lineEditFileName.text()) #set path to the file name in the line edit
        extension = os.path.splitext(self.lineEditFileName.text())[1] #set extension to the file name in the line edit
        MainWindow.path=path #set path to the class level variable


        list_of_files = glob.glob(path + '/*' + extension) #get all files in the sequence

        first_file = min(list_of_files) #get the first file in the sequence
        last_file = max(list_of_files) #get the last file in the sequence

        regex = re.compile(r'\d{3,6}\.') #regex for finding the number between 3 and 6 in the file name

        try:
            first_file_number_str = regex.search(first_file).group(0) #find the number in the file name
            first_file_number_str = first_file_number_str.rstrip(first_file_number_str[-1]) #remove the dot at the end
            first_file_number_int = int(first_file_number_str) #convert the number to an integer
            
            last_file_number_str = regex.search(last_file).group(0) #find the number in the file name
            last_file_number_str = last_file_number_str.rstrip(last_file_number_str[-1]) #remove the dot at the end
            last_file_number_int = int(last_file_number_str) #convert the number to an integer
        except:
            QtWidgets.QMessageBox.warning(None, "Error", "Selected file is not a part of the sequence")
            #print("Selected file is not a part of the sequence")
            return

        padding = len(first_file_number_str) #find the padding of the number in the file name

        base_file_name = first_file.replace(first_file_number_str, '') #remove the number from the file name
        base_file_name = os.path.splitext(base_file_name)[0] #remove the extension from the file name

        file_size = os.path.getsize(first_file) #get the size of the first file
        old_file = first_file

        #bytes/kilobytes/megabytes
        if self.radioButtonKilobytes.isChecked():
            anomaly=int(float(self.lineEditAnomalySize.text())*1000)
        elif self.radioButtonMegabytes.isChecked():
            anomaly=int(float(self.lineEditAnomalySize.text())*1000000)
        else:
            anomaly=int(self.lineEditAnomalySize.text())
        #print(anomaly)

        err_list = [] #list of files with errors

        for filenum in range(first_file_number_int, last_file_number_int): #for each file in the sequence

            app.processEvents() #process events (update the GUI)

            num = str(filenum).rjust(padding, '0') #pad the number with zeros
            file_name_generated = base_file_name + num + extension #generate the file name

            percentage = int((filenum-first_file_number_int)/(last_file_number_int-first_file_number_int)*100) #calculate the percentage of the sequence
            self.progressBar.setValue(percentage)  #set progress bar to the percentage of the file

            if self.checkBoxMissing.isChecked() and not os.path.isfile(file_name_generated): 
                msg = 'Missing: ' + os.path.basename(file_name_generated)
                self.plainTextEditOutputConsole.appendPlainText(msg)
                err_list.append(msg)

                
            if self.checkBoxAnomalies.isChecked() and os.path.isfile(file_name_generated) and abs(file_size - os.path.getsize(file_name_generated)) > anomaly: 

                #msg = 'Size anomaly: ' + os.path.basename(file_name_generated) + ' (with ' + os.path.basename(old_file) + ' and its ' + shrinkBytes(abs(file_size - os.path.getsize(file_name_generated))) + ')'
                msg = 'Size anomaly: ' + os.path.basename(file_name_generated) + ' (' + shrinkBytes(abs(file_size - os.path.getsize(file_name_generated))) + ')'
                self.plainTextEditOutputConsole.appendPlainText(msg)
                err_list.append(msg)
            
            if os.path.isfile(file_name_generated):
                old_file = file_name_generated
                file_size = os.path.getsize(file_name_generated)

            if self.checkBoxBroken.isChecked() and os.path.isfile(file_name_generated):
                try:
                    im = Image.open(file_name_generated)
                    im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
                    im.close()
                except (IOError, SyntaxError) as e:
                    msg = 'Broken:  ' + os.path.basename(file_name_generated)
                    self.plainTextEditOutputConsole.appendPlainText(msg)
                    err_list.append(msg)
        
        self.progressBar.setValue(100)

        #print('Checking done')

        app.restoreOverrideCursor() #restore cursor

        if len(err_list) == 0:
            #print('No errors found')
            #add a message to the output console
            self.plainTextEditOutputConsole.appendPlainText('No errors found')
        else:
            #show question box with message 'Would you like to save a report?' and if user clicked  yes save the report
            reply = QtWidgets.QMessageBox.question(None, 'Report', 'Would you like to save a report?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                #replace all symbols after last dot in the self.lineEditFileName.text()with txt, and apply this value to the filename variable
                filename = self.lineEditFileName.text().replace(os.path.splitext(self.lineEditFileName.text())[1], '.txt')
                
                #print(filename)

                #show txt file save dialog
                fileName = QtWidgets.QFileDialog.getSaveFileName(None, 'Save report', filename, 'Text files (*.txt)')
                #if fileName is not empty, save the report
                if fileName[0] != '':
                    with open(fileName[0], 'w') as f:
                        for msg in err_list:
                            f.write(msg + '\n')
                        f.close()

        #self.Enabled(True)

    def saveDefaults(self):
        #save current settings
        settings = QtCore.QSettings("./isc.ini", QtCore.QSettings.IniFormat)
        if self.checkBoxSaveDefaults.isChecked():
            settings.setValue("missing", self.checkBoxMissing.isChecked())
            settings.setValue("anomalies", self.checkBoxAnomalies.isChecked())
            settings.setValue("broken", self.checkBoxBroken.isChecked())
            if self.radioButtonBytes.isChecked():
                settings.setValue("anomaly_size", self.lineEditAnomalySize.text())
            elif self.radioButtonKilobytes.isChecked():
                settings.setValue("anomaly_size", self.lineEditAnomalySize.text() + "K")
            elif self.radioButtonMegabytes.isChecked():
                settings.setValue("anomaly_size", self.lineEditAnomalySize.text() + "M")
        settings.setValue("path", MainWindow.path)
        settings.sync()

def shrinkBytes(val):
    if val > 1000000:
        return str(val/1000000) + "M"
    elif val > 1000:
        return str(val/1000) + "K"
    else:
        return str(val) + " bytes"
               
                
if __name__ == "__main__":
    import sys, os, configparser

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #if config file exists, load the settings
    if os.path.isfile('./isc.ini'):
        #restoring configuration from the ini file
        config = configparser.ConfigParser() 
        config.read('./isc.ini')
        if config.has_section('General'):
            if config.has_option('General', 'missing'):
                ui.checkBoxMissing.setChecked(config.getboolean('General', 'missing'))
            if config.has_option('General', 'anomalies'):
                ui.checkBoxAnomalies.setChecked(config.getboolean('General', 'anomalies'))
            if config.has_option('General', 'broken'):
                ui.checkBoxBroken.setChecked(config.getboolean('General', 'broken'))
            if config.has_option('General', 'anomaly_size'):
                anosize=config.get('General', 'anomaly_size')
                #print(anosize)
                if anosize.endswith('K'):
                    ui.radioButtonKilobytes.setChecked(True)
                    anosize=anosize[:-1]
                    #print("K")
                elif anosize.endswith('M'):
                    ui.radioButtonMegabytes.setChecked(True)
                    anosize=anosize[:-1]
                    #print("M")
                else:
                    ui.radioButtonBytes.setChecked(True)
                ui.lineEditAnomalySize.setText(anosize)
            else:
                ui.lineEditAnomalySize.setText('500')
            if config.has_option('General','path'):
                MainWindow.path = config.get('General', 'path')
    else: #if config file does not exist, set default values and create the config file
        #create the config file
        config = configparser.ConfigParser()
        config.add_section('General')
        config.set('General', 'missing', 'True')
        config.set('General', 'anomalies', 'True')
        config.set('General', 'broken', 'True')
        config.set('General', 'anomaly_size', '500K')
        config.set('General', 'path', '')
        with open('./isc.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()

        ui.lineEditAnomalySize.setText('500')   #set default value for anomaly size

    MainWindow.show()
    sys.exit(app.exec_())





    