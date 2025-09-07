from PyQt5 import QtCore, QtGui, QtWidgets
import Open_Team_Window as OTW
import Create_Team_Dialogue as CTD
import sqlite3

class Ui_MainWindow(object):
    def CreateTeamDialogue(self):
        self.window=QtWidgets.QDialog()
        self.ui=CTD.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.l7.setText(CTD.Ui_Form.TeamName)
       
        

    def OpenTeamWindow(self):
        self.window=QtWidgets.QWidget()
        self.ui=OTW.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 661)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)

















        
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: bold italic 9pt \"Comic Sans MS\";\n"+"background-image:url(\"c.jpeg\")")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(197, 197, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.l1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.l1.setObjectName("l1")
        self.horizontalLayout.addWidget(self.l1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(197, 197, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setStyleSheet("background-color: rgb(255, 255, 191);\n""")
        self.l2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.l2.setObjectName("l2")
        self.horizontalLayout.addWidget(self.l2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(197, 197, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setStyleSheet("background-color: rgb(255, 255, 191);\n""")
        self.l3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.l3.setObjectName("l3")
        self.horizontalLayout.addWidget(self.l3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n""background-color: rgb(197, 197, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.l4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.l4.setObjectName("l4")
        self.horizontalLayout.addWidget(self.l4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(197, 197, 0);\n""background-color: rgb(0, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(253, 84, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.l5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l5.setObjectName("l5")
        self.horizontalLayout_3.addWidget(self.l5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rb3.setFont(font)
        self.rb3.setStyleSheet("\n""background-color: rgb(170, 255, 0);")
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rb4.setFont(font)
        self.rb4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-image:url(\"d.jpeg\")\n""")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 191);\n""background-color: rgb(85, 170, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(253, 84, 0);\n""")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.l6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.l6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l6.setObjectName("l6")
        self.horizontalLayout_4.addWidget(self.l6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.l7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l7.setFont(font)
        self.l7.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.l7.setText("")
        self.l7.setObjectName("l7")
        self.horizontalLayout_5.addWidget(self.l7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-image:url(\"d.jpeg\")\n""")
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 191);\n""background-color: rgb(85, 170, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionNew_Team_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionNew_Team_2.setFont(font)
        self.actionNew_Team_2.setObjectName("actionNew_Team_2")
        self.actionOpen_Team_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionOpen_Team_2.setFont(font)
        self.actionOpen_Team_2.setObjectName("actionOpen_Team_2")
        self.actionSave_Team_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionSave_Team_2.setFont(font)
        self.actionSave_Team_2.setObjectName("actionSave_Team_2")
        self.actionEvaluate_Team_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionEvaluate_Team_2.setFont(font)
        self.actionEvaluate_Team_2.setObjectName("actionEvaluate_Team_2")
        self.menuManage_Teams.addAction(self.actionNew_Team_2)
        self.menuManage_Teams.addAction(self.actionOpen_Team_2)
        self.menuManage_Teams.addAction(self.actionSave_Team_2)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team_2)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menuFunction)
        self.rb1.toggled.connect(self.checkable)
        self.rb2.toggled.connect(self.checkable)
        self.rb3.toggled.connect(self.checkable)
        self.rb4.toggled.connect(self.checkable)
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def menuFunction(self,action):
        txt=action.text()

        if txt=="New Team":
            self.CreateTeamDialogue()


        if txt=="Open Team":
            self.OpenTeamWindow()

        if txt=="Save Team":
            Cricket=sqlite3.connect("FantasyCricketApp.db")
            curplayers=Cricket.cursor()
            team_name = self.l7.text()
            players = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
            self.points=0
            for item in players:
                sql="select value from stats where player = '"+item+"';"
                curplayers.execute(sql)
                point=curplayers.fetchone()
                self.points+=int(str(point)[1:-2])
            sql = "INSERT INTO TEAMS  VALUES (?, ?, ?)"
            curplayers.execute(sql, (team_name, str(players),self.points))
            Cricket.commit()
            Cricket.close()
            QtWidgets.QMessageBox.information(None, "Success", "Saved successfully!")
            QtWidgets.QWidget().close()
        if txt=="Evaluate Team":
            QtWidgets.QMessageBox.information(None, "Evluate score", f"Your Team Score is \n\t{OTW.Ui_Form.team_score}")
            QtWidgets.QWidget().close()
             

           
    def checkable(self):
        self.listWidget.clear()
        Cricket=sqlite3.connect("FantasyCricketApp.db")
        curplayers=Cricket.cursor()


        if self.rb1.isChecked():
                sql="SELECT PLAYER,VALUE FROM STATS WHERE CATEGORY = 'BAT';"
                curplayers.execute(sql)
                records=curplayers.fetchall()
                
                for record in records:
                    f=(str(record))[2:len(str(record))-1]
                    self.listWidget.addItem(f.split(',')[0][0:-1]+" - "+f.split(',')[1])
                
        if self.rb2.isChecked():
                sql="SELECT PLAYER,VALUE FROM STATS WHERE CATEGORY = 'BWL';"
                curplayers.execute(sql)
                records=curplayers.fetchall()
                for record in records:
                    f=(str(record))[2:len(str(record))-1]
                    self.listWidget.addItem(f.split(',')[0][0:-1]+" - "+f.split(',')[1])

        if self.rb3.isChecked():
                sql="SELECT PLAYER,VALUE FROM STATS WHERE CATEGORY = 'AR';"
                curplayers.execute(sql)
                records=curplayers.fetchall()
                for record in records:
                    f=(str(record))[2:len(str(record))-1]
                    self.listWidget.addItem(f.split(',')[0][0:-1]+" - "+f.split(',')[1])
        if self.rb4.isChecked():
                sql="SELECT PLAYER,VALUE FROM STATS WHERE CATEGORY = 'WK';"
                curplayers.execute(sql)
                records=curplayers.fetchall()
                self.l=[]
                for record in records:
                    f=(str(record))[2:len(str(record))-1]
                    self.listWidget.addItem(f.split(',')[0][0:-1]+" - "+f.split(',')[1])
                    self.l.append(f.split(',')[0][0:-1])

    def removelist1(self,item):
        Cricket=sqlite3.connect("FantasyCricketApp.db")
        curplayers=Cricket.cursor()
        self.total_players=int(self.l1.text())+int(self.l2.text())+int(self.l3.text())+int(self.l4.text())

        if self.total_players<11:

            if (self.total_players==10 and int(self.l4.text())<=0 and str(item.text().split(' - ')[0]) not in self.l) or (int(self.l4.text())==1 and str(item.text().split(' - ')[0]) in self.l):
                QtWidgets.QMessageBox.warning(None, "Warning", "There must be one wicket keeper!")
                QtWidgets.QWidget().close()
            else:
                 
                if str(item.text().split(' - ')[0]) not in [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]:
                
                    self.points_available=int(self.l5.text())
                    
                    sql="select value from stats where player = '"+str(item.text().split(' - ')[0])+"';"
                    curplayers.execute(sql)
                    point=curplayers.fetchone()

                    n=self.points_available-int(str(point)[1:-2])
                    if n<0:
                        QtWidgets.QMessageBox.warning(None, "Warning", "Point limit exceeded")
                        QtWidgets.QWidget().close()
                    else:
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.listWidget_2.addItem(str(item.text().split(' - ')[0]))
                        self.points_available=self.points_available-int(str(point)[1:-2])
                        self.l6.setText(str(1000-self.points_available))
                        self.l5.setText(str(self.points_available))
                        
                        if self.rb1.isChecked():
                            count=int(self.l1.text())
                            count=count+1
                            self.l1.setText(str(count))

                        if self.rb2.isChecked():
                                count=int(self.l2.text())
                                count=count+1
                                self.l2.setText(str(count))

                        if self.rb3.isChecked():
                                count=int(self.l3.text())
                                count=count+1
                                self.l3.setText(str(count))

                        if self.rb4.isChecked():
                                count=int(self.l4.text())
                                count=count+1
                                self.l4.setText(str(count)) 
                    Cricket.close()
                    
                else:
                    QtWidgets.QMessageBox.warning(None, "Warning", f"{str(item.text().split(' - ')[0])} already selected !")
                    QtWidgets.QWidget().close()
        else:
             QtWidgets.QMessageBox.warning(None, "Warning", "Team limit exceeded !")
             QtWidgets.QWidget().close()
             
        
        


    def removelist2(self,item):
        

        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        # self.listWidget.addItem(item.text())
        Cricket=sqlite3.connect("FantasyCricketApp.db")
        curplayers=Cricket.cursor()
        sql="select value from stats where player = '"+item.text()+"';"
        curplayers.execute(sql)
        point=curplayers.fetchone()
        self.points_available=self.points_available+int(str(point)[1:-2])
        self.l6.setText(str(1000-self.points_available))
        self.l5.setText(str(self.points_available))
        Cricket.close()

        if self.rb1.isChecked():
                count=int(self.l1.text())
                count=count-1
                self.l1.setText(str(count))

        if self.rb2.isChecked():
                count=int(self.l2.text())
                count=count-1
                self.l2.setText(str(count))

        if self.rb3.isChecked():
                count=int(self.l3.text())
                count=count-1
                self.l3.setText(str(count))

        if self.rb4.isChecked():
                count=int(self.l4.text())
                count=count-1
                self.l4.setText(str(count))
        self.total_players=int(self.l1.text())+int(self.l2.text())+int(self.l3.text())+int(self.l4.text())

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Team"))
        self.label_2.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.l1.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.l2.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.l3.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.l4.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_4.setText(_translate("MainWindow", "Points Available :"))
        self.l5.setText(_translate("MainWindow", "1000"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_3.setText(_translate("MainWindow", "Available Players"))
        self.label_6.setText(_translate("MainWindow", "Points Used :"))
        self.l6.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Team Name"))
        self.label_8.setText(_translate("MainWindow", "Selected Players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionNew_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionSave_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionEvaluate_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionNew_Team_2.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team_2.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team_2.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team_2.setText(_translate("MainWindow", "Evaluate Team"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())