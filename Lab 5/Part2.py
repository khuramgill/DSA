import csv
##-----------------------------All District Name and Tehsil ----------------------------##
district=["Attock","Bahawalnagar","Bahawalpur","Bhakkar","Chakwal","Chiniot",
"Dera Ghazi Khan","Faisalabad","Gujranwala","Gujrat","Hafizabad","Jhang","Jhelum",
"Kasur","Khanewal","Khushab","Lahore","Layyah","Lodhran","Mandi Bahauddin",
"Mianwali","Multan","Muzaffargarh","Narowal","Nankana Sahib","Okara","Pakpattan",
"Rahim Yar Khan""Rajanpur","Rawalpindi","Sahiwal","Sargodha","Sheikhupura","Sialkot"
,"Toba Tek Singh","Vehari"]
Tehsil=["GUJAR KHAN","KAHUTA","KALLAR SAYYEDAN","KOTLI SATTIAN","MURREE","RAWALPINDI","TAXILAz"]

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 592)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblChallanForm = QtWidgets.QLabel(self.centralwidget)
        self.lblChallanForm.setGeometry(QtCore.QRect(140, 0, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblChallanForm.setFont(font)
        self.lblChallanForm.setObjectName("lblChallanForm")
        self.lblChallanDetail = QtWidgets.QLabel(self.centralwidget)
        self.lblChallanDetail.setGeometry(QtCore.QRect(10, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblChallanDetail.setFont(font)
        self.lblChallanDetail.setObjectName("lblChallanDetail")
        self.lblDistrict = QtWidgets.QLabel(self.centralwidget)
        self.lblDistrict.setGeometry(QtCore.QRect(30, 50, 111, 41))
        ##--------------------District------------------------##
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDistrict.setFont(font)
        self.lblDistrict.setObjectName("lblDistrict")
        self.cmbxDistrict = QtWidgets.QComboBox(self.centralwidget)
        self.cmbxDistrict.setGeometry(QtCore.QRect(30, 80, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbxDistrict.setFont(font)
        self.cmbxDistrict.setObjectName("cmbxDistrict")
        for i in range(len(district)):
            self.cmbxDistrict.addItem(district[i])
        ##--------------------Tehsil------------------------##
        self.cmbxTehsil = QtWidgets.QComboBox(self.centralwidget)
        self.cmbxTehsil.setGeometry(QtCore.QRect(260, 80, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbxTehsil.setFont(font)
        self.cmbxTehsil.setObjectName("cmbxTehsil")
        for i in range(len(Tehsil)):
            self.cmbxTehsil.addItem(Tehsil[i])
        self.lblTehsil = QtWidgets.QLabel(self.centralwidget)
        self.lblTehsil.setGeometry(QtCore.QRect(260, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTehsil.setFont(font)
        self.lblTehsil.setObjectName("lblTehsil")
        self.lblStampPaper = QtWidgets.QLabel(self.centralwidget)
        self.lblStampPaper.setGeometry(QtCore.QRect(30, 90, 111, 41))
      
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblStampPaper.setFont(font)
        self.lblStampPaper.setObjectName("lblStampPaper")
        self.cmbxDeedName = QtWidgets.QComboBox(self.centralwidget)
        self.cmbxDeedName.setGeometry(QtCore.QRect(260, 120, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbxDeedName.setFont(font)
        self.cmbxDeedName.setObjectName("cmbxDeedName")
        self.lblDeedName = QtWidgets.QLabel(self.centralwidget)
        self.lblDeedName.setGeometry(QtCore.QRect(260, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDeedName.setFont(font)
        self.lblDeedName.setObjectName("lblDeedName")
        self.cmbxStampPaper = QtWidgets.QComboBox(self.centralwidget)
        self.cmbxStampPaper.setGeometry(QtCore.QRect(30, 120, 221, 22))
        ##-------------------- Combox Box Stamp Paper ------------------------##
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbxStampPaper.setFont(font)
        self.cmbxStampPaper.setObjectName("cmbxStampPaper")
        self.cmbxStampPaper.addItem("Judical")
        self.cmbxStampPaper.addItem("Non-Judical")
        # if (self.cmbxStampPaper.currentIndex()==1):
        #     ckbxRegistrationFee.setCheckable(False)
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(260, 150, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName("lblMessage")
        self.lblPurpose = QtWidgets.QLabel(self.centralwidget)
        self.lblPurpose.setGeometry(QtCore.QRect(30, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPurpose.setFont(font)
        self.lblPurpose.setObjectName("lblPurpose")
        self.ckbxRegistrationFee = QtWidgets.QCheckBox(self.centralwidget)
        self.ckbxRegistrationFee.setGeometry(QtCore.QRect(30, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ckbxRegistrationFee.setFont(font)
        self.ckbxRegistrationFee.setObjectName("ckbxRegistrationFee")
        self.lblChallanAmount = QtWidgets.QLabel(self.centralwidget)
        self.lblChallanAmount.setGeometry(QtCore.QRect(30, 180, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblChallanAmount.setFont(font)
        self.lblChallanAmount.setObjectName("lblChallanAmount")
        self.rdbtnFirstParty = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbtnFirstParty.setGeometry(QtCore.QRect(30, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbtnFirstParty.setFont(font)
        self.rdbtnFirstParty.setObjectName("rdbtnFirstParty")
        self.rdbtnSecondParty = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbtnSecondParty.setGeometry(QtCore.QRect(130, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbtnSecondParty.setFont(font)
        self.rdbtnSecondParty.setObjectName("rdbtnSecondParty")
        self.lblAgentInformation = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentInformation.setGeometry(QtCore.QRect(10, 230, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblAgentInformation.setFont(font)
        self.lblAgentInformation.setObjectName("lblAgentInformation")
        self.lblAgentName = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentName.setGeometry(QtCore.QRect(30, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAgentName.setFont(font)
        self.lblAgentName.setObjectName("lblAgentName")
        self.lblAgentCNIC = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentCNIC.setGeometry(QtCore.QRect(260, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAgentCNIC.setFont(font)
        self.lblAgentCNIC.setObjectName("lblAgentCNIC")
        self.txtbxAgentCNIC = QtWidgets.QTextEdit(self.centralwidget)
        self.txtbxAgentCNIC.setGeometry(QtCore.QRect(260, 280, 221, 21))
        self.txtbxAgentCNIC.setObjectName("txtbxAgentCNIC")
        self.txtbxAgentName = QtWidgets.QTextEdit(self.centralwidget)
        self.txtbxAgentName.setGeometry(QtCore.QRect(30, 280, 221, 21))
        self.txtbxAgentName.setObjectName("txtbxAgentName")
        self.txtbxAgentContact = QtWidgets.QTextEdit(self.centralwidget)
        self.txtbxAgentContact.setGeometry(QtCore.QRect(30, 320, 221, 21))
        self.txtbxAgentContact.setObjectName("txtbxAgentContact")
        self.txtbxAgenrEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.txtbxAgenrEmail.setGeometry(QtCore.QRect(260, 320, 221, 21))
        self.txtbxAgenrEmail.setObjectName("txtbxAgenrEmail")
        self.lblAgentEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentEmail.setGeometry(QtCore.QRect(260, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAgentEmail.setFont(font)
        self.lblAgentEmail.setObjectName("lblAgentEmail")
        self.lblAgentContact = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentContact.setGeometry(QtCore.QRect(30, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAgentContact.setFont(font)
        self.lblAgentContact.setObjectName("lblAgentContact")
        self.lblFirstPartyInofrmation = QtWidgets.QLabel(self.centralwidget)
        self.lblFirstPartyInofrmation.setGeometry(QtCore.QRect(10, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblFirstPartyInofrmation.setFont(font)
        self.lblFirstPartyInofrmation.setObjectName("lblFirstPartyInofrmation")
        self.btnAddFirstParty = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddFirstParty.setGeometry(QtCore.QRect(350, 350, 131, 23))
        self.btnAddFirstParty.setObjectName("btnAddFirstParty")
        self.btnAddSecondParty = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddSecondParty.setGeometry(QtCore.QRect(350, 430, 131, 23))
        self.btnAddSecondParty.setObjectName("btnAddSecondParty")
        self.lblSecondPartyInofrmation = QtWidgets.QLabel(self.centralwidget)
        self.lblSecondPartyInofrmation.setGeometry(QtCore.QRect(10, 420, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblSecondPartyInofrmation.setFont(font)
        self.lblSecondPartyInofrmation.setObjectName("lblSecondPartyInofrmation")
        self.lblFirstPartyMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblFirstPartyMessage.setGeometry(QtCore.QRect(30, 380, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblFirstPartyMessage.setFont(font)
        self.lblFirstPartyMessage.setObjectName("lblFirstPartyMessage")
        self.lblSecondPartyMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblSecondPartyMessage.setGeometry(QtCore.QRect(30, 460, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSecondPartyMessage.setFont(font)
        self.lblSecondPartyMessage.setObjectName("lblSecondPartyMessage")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(390, 500, 91, 41))
        self.btnNext.setObjectName("btnNext")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(290, 500, 91, 41))
        self.btnReset.setObjectName("btnReset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def save_data_to_csv(self):
        # Gather data from UI
        district = self.cmbxDistrict.currentText()
        tehsil = self.cmbxTehsil.currentText()
        stamp_paper_type = self.cmbxStampPaper.currentText()
        deed_name = self.cmbxDeedName.currentText()
        purpose = "Sale Deed" if self.ckbxRegistrationFee.isChecked() else "Other"
        party_type = "First Party" if self.rdbtnFirstParty.isChecked() else "Second Party"
        agent_name = self.txtbxAgentName.toPlainText()
        agent_cnic = self.txtbxAgentCNIC.toPlainText()
        agent_contact = self.txtbxAgentContact.toPlainText()
        agent_email = self.txtbxAgenrEmail.toPlainText()

        # Create or append to the CSV file
        with open('challan_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([district, tehsil, stamp_paper_type, deed_name, purpose,
                             party_type, agent_name, agent_cnic, agent_contact, agent_email])

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblChallanForm.setText(_translate("MainWindow", "Challan Form No. 32-A"))
        self.lblChallanDetail.setText(_translate("MainWindow", "Challan Details"))
        self.lblDistrict.setText(_translate("MainWindow", "District"))
        self.lblTehsil.setText(_translate("MainWindow", "Tehsil"))
        self.lblStampPaper.setText(_translate("MainWindow", "Stamp Paper Type"))
        self.lblDeedName.setText(_translate("MainWindow", "Deed Name"))
        self.lblMessage.setText(_translate("MainWindow", "For Sale Deed please use Conveyance"))
        self.lblPurpose.setText(_translate("MainWindow", "Purpose of Challan"))
        self.ckbxRegistrationFee.setText(_translate("MainWindow", "RegistrationFee"))
        self.lblChallanAmount.setText(_translate("MainWindow", "Challan Amount Paid By?"))
        self.rdbtnFirstParty.setText(_translate("MainWindow", "First Party"))
        self.rdbtnSecondParty.setText(_translate("MainWindow", "Second Party"))
        self.lblAgentInformation.setText(_translate("MainWindow", "Agent Information"))
        self.lblAgentName.setText(_translate("MainWindow", "Agent Name"))
        self.lblAgentCNIC.setText(_translate("MainWindow", "Agent CNIC"))
        self.lblAgentEmail.setText(_translate("MainWindow", "Agent Email"))
        self.lblAgentContact.setText(_translate("MainWindow", "Agent Contact"))
        self.lblFirstPartyInofrmation.setText(_translate("MainWindow", "First Party Information"))
        self.btnAddFirstParty.setText(_translate("MainWindow", "Add First Party"))
        self.btnAddSecondParty.setText(_translate("MainWindow", "Add Second Party"))
        self.lblSecondPartyInofrmation.setText(_translate("MainWindow", "Second Party Information"))
        self.lblFirstPartyMessage.setText(_translate("MainWindow", "Please add one First Party"))
        self.lblSecondPartyMessage.setText(_translate("MainWindow", "Please add one Second Party"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnNext.clicked.connect(self.save_data_to_csv)
        self.btnReset.clicked.connect(self.save_data_to_csv)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())