from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
	"""UI layout"""
	
	def setupUi(self, MainWindow):   
		MainWindow.setObjectName("MainWindow")
		MainWindow.showFullScreen()
		MainWindow.setStyleSheet("MainWindow{background:#8392AA;border:3px solid gray;border-radius:5px;padding: 4 4 4 4px;}"
								 "QMenuBar{background:#8392AA;};")
		MainWindow.setWindowIcon(QtGui.QIcon('50X18.png'))         
		MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 
		MainWindow.setWindowOpacity(1)
		MainWindow.setStyleSheet("MainWindow{border-image:url(free.jpg);}")  
		self.cursor = QCursor(QPixmap('cursor.png').scaled(30,40),5,5)
		MainWindow.setCursor(self.cursor)
		self.centralwidget = QtWidgets.QWidget(MainWindow)         
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)
		self.btn1 = QtWidgets.QPushButton(self.centralwidget)
		self.btn1.setStyleSheet(""'''QPushButton{background:#45c952;font-size:20px;border-radius:5px;font-family:Roman times;} \
			                         QPushButton:hover{background:solid gray;}'''"")
		self.btn2 = QtWidgets.QPushButton(self.centralwidget)
		self.btn2.setStyleSheet('''QPushButton{background:#fdcc38;font-size:20px;border-radius:5px;font-family:Roman times;} \
			                       QPushButton:hover{background:solid gray;}''')        
		self.btn3 = QtWidgets.QPushButton(self.centralwidget)
		self.btn3.setStyleSheet('''QPushButton{background:#dc143c;font-size:20px;border-radius:5px;font-family:Roman times;} \
			                       QPushButton:hover{background:solid gray;}''')
		self.label = QtWidgets.QLabel(self.centralwidget) 
		pix = QPixmap("stan.png")
		self.label.setPixmap(pix)        
		self.label.setScaledContents(True)
		self.label1 = QtWidgets.QLabel("                Access Control System",self.centralwidget)               
		self.label1.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EDBA19;}"
								   "QLabel{font-size:30px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label1.setAlignment(QtCore.Qt.AlignCenter)    
		self.label2 = QtWidgets.QLabel(self.centralwidget)               
		self.label2.setAlignment(QtCore.Qt.AlignCenter) 
		self.label2.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label4 = QtWidgets.QLabel(self.centralwidget)               
		self.label4.setAlignment(QtCore.Qt.AlignCenter)
		self.label4.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")          
		self.label5 = QtWidgets.QLabel(self.centralwidget)               
		self.label5.setAlignment(QtCore.Qt.AlignCenter)
		self.label5.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Roman times;}")        
		self.label6 = QtWidgets.QLabel(self.centralwidget)               
		self.label6.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label6.setAlignment(QtCore.Qt.AlignLeft)
		self.label6.setAlignment(QtCore.Qt.AlignVCenter)
		self.label7 = QtWidgets.QLabel(self.centralwidget)               
		self.label7.setAlignment(QtCore.Qt.AlignCenter)
		self.label7.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label8 = QtWidgets.QLabel(self.centralwidget)               
		self.label8.setAlignment(QtCore.Qt.AlignCenter)
		self.label8.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Roman times;}")
		self.label9 = QtWidgets.QLabel(self.centralwidget)               
		self.label9.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label9.setAlignment(QtCore.Qt.AlignLeft)
		self.label9.setAlignment(QtCore.Qt.AlignVCenter)
		self.label10 = QtWidgets.QLabel(self.centralwidget)               
		self.label10.setAlignment(QtCore.Qt.AlignCenter)
		self.label10.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label11 = QtWidgets.QLabel(self.centralwidget)               
		self.label11.setAlignment(QtCore.Qt.AlignCenter)
		self.label11.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Roman times;}")
		self.label12 = QtWidgets.QLabel(self.centralwidget)               
		self.label12.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label12.setAlignment(QtCore.Qt.AlignLeft)
		self.label12.setAlignment(QtCore.Qt.AlignVCenter)
		self.label13 = QtWidgets.QLabel(self.centralwidget)               
		self.label13.setAlignment(QtCore.Qt.AlignCenter)
		self.label13.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label14 = QtWidgets.QLabel(self.centralwidget)               
		self.label14.setAlignment(QtCore.Qt.AlignCenter)
		self.label14.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Roman times;}")
		self.label15 = QtWidgets.QLabel(self.centralwidget)               
		self.label15.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label15.setAlignment(QtCore.Qt.AlignLeft)
		self.label15.setAlignment(QtCore.Qt.AlignVCenter)
		self.label16 = QtWidgets.QLabel(self.centralwidget)               
		self.label16.setAlignment(QtCore.Qt.AlignCenter)
		self.label16.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label17 = QtWidgets.QLabel(self.centralwidget)               
		self.label17.setAlignment(QtCore.Qt.AlignCenter)
		self.label17.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label18 = QtWidgets.QLabel(self.centralwidget)               
		self.label18.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label18.setAlignment(QtCore.Qt.AlignLeft)
		self.label18.setAlignment(QtCore.Qt.AlignVCenter)
		self.label19 = QtWidgets.QLabel(self.centralwidget)
		self.label19.setAlignment(QtCore.Qt.AlignCenter)
		self.label19.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:36px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label20 = QtWidgets.QLabel(self.centralwidget)               
		self.label20.setAlignment(QtCore.Qt.AlignCenter)
		self.label20.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Roman times;}")
		self.label21 = QtWidgets.QLabel(self.centralwidget)               
		self.label21.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}")
		self.label21.setAlignment(QtCore.Qt.AlignLeft)
		self.label21.setAlignment(QtCore.Qt.AlignVCenter)
		self.label22 = QtWidgets.QLabel(self.centralwidget)               
		self.label22.setAlignment(QtCore.Qt.AlignCenter)
		self.label22.setStyleSheet("QLabel{background:transparent;border-radius:10px;}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:12px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label23 = QtWidgets.QLabel(self.centralwidget)               
		self.label23.setAlignment(QtCore.Qt.AlignLeft)
		self.label23.setAlignment(QtCore.Qt.AlignVCenter)       
		self.label23.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#DAF6D7;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label24 = QtWidgets.QLabel(self.centralwidget)               
		self.label24.setAlignment(QtCore.Qt.AlignLeft)
		self.label24.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")  
		self.label25 = QtWidgets.QLabel(self.centralwidget)
		self.label25.setAlignment(QtCore.Qt.AlignLeft)
		self.label25.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")

		self.label26 = QtWidgets.QLabel(self.centralwidget)
		self.label26.setAlignment(QtCore.Qt.AlignLeft)
		self.label26.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label27 = QtWidgets.QLabel(self.centralwidget)
		self.label27.setAlignment(QtCore.Qt.AlignLeft)
		self.label27.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label28 = QtWidgets.QLabel(self.centralwidget)
		self.label28.setAlignment(QtCore.Qt.AlignLeft)
		self.label28.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")  
		self.label29 = QtWidgets.QLabel(self.centralwidget)
		self.label29.setAlignment(QtCore.Qt.AlignLeft)
		self.label29.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label30 = QtWidgets.QLabel(self.centralwidget)
		self.label30.setAlignment(QtCore.Qt.AlignLeft)
		self.label30.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label31 = QtWidgets.QLabel(self.centralwidget)
		self.label31.setAlignment(QtCore.Qt.AlignLeft)
		self.label31.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label32 = QtWidgets.QLabel(self.centralwidget)
		self.label32.setAlignment(QtCore.Qt.AlignLeft)
		self.label32.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label33 = QtWidgets.QLabel(self.centralwidget)
		self.label33.setAlignment(QtCore.Qt.AlignLeft)
		self.label33.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label34 = QtWidgets.QLabel(self.centralwidget)
		self.label34.setAlignment(QtCore.Qt.AlignLeft)
		self.label34.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label35 = QtWidgets.QLabel(self.centralwidget)
		self.label35.setAlignment(QtCore.Qt.AlignLeft)
		self.label35.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label36 = QtWidgets.QLabel(self.centralwidget)
		self.label36.setAlignment(QtCore.Qt.AlignLeft)
		self.label36.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label37 = QtWidgets.QLabel(self.centralwidget)
		self.label37.setAlignment(QtCore.Qt.AlignLeft)
		self.label37.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")								
		self.label38 = QtWidgets.QLabel(self.centralwidget)               
		self.label38.setAlignment(QtCore.Qt.AlignLeft)
		self.label38.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label39 = QtWidgets.QLabel(self.centralwidget)
		self.label39.setAlignment(QtCore.Qt.AlignLeft)
		self.label39.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label40 = QtWidgets.QLabel(self.centralwidget)
		self.label40.setAlignment(QtCore.Qt.AlignLeft)
		self.label40.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label41 = QtWidgets.QLabel(self.centralwidget)
		self.label41.setAlignment(QtCore.Qt.AlignLeft)
		self.label41.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label42 = QtWidgets.QLabel(self.centralwidget)
		self.label42.setAlignment(QtCore.Qt.AlignLeft)
		self.label42.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label43 = QtWidgets.QLabel(self.centralwidget)
		self.label43.setAlignment(QtCore.Qt.AlignLeft)
		self.label43.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#071405;}"
								   "QLabel{font-size:18px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label44 = QtWidgets.QLabel(self.centralwidget)
		self.label44.setAlignment(QtCore.Qt.AlignCenter)
		self.label44.setStyleSheet("QLabel{background:transparent}"
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:50px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label45 = QtWidgets.QLabel(self.centralwidget)
		self.label45.setAlignment(QtCore.Qt.AlignCenter)
		self.label45.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}")
		self.label46 = QtWidgets.QLabel(self.centralwidget)
		self.label46.setAlignment(QtCore.Qt.AlignCenter)
		self.label46.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}") 
		self.label47 = QtWidgets.QLabel(self.centralwidget)               
		self.label47.setAlignment(QtCore.Qt.AlignCenter)
		self.label47.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}") 
		self.label48 = QtWidgets.QLabel(self.centralwidget)               
		self.label48.setAlignment(QtCore.Qt.AlignCenter)
		self.label48.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}") 
		self.label49 = QtWidgets.QLabel(self.centralwidget)               
		self.label49.setAlignment(QtCore.Qt.AlignCenter)
		self.label49.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}") 
		self.label50 = QtWidgets.QLabel(self.centralwidget)               
		self.label50.setAlignment(QtCore.Qt.AlignCenter)
		self.label50.setStyleSheet("QLabel{background:transparent}" 
								   "QLabel{color:#EBB666;}"
								   "QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}") 
		self.verticalLayout_13 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_13.addWidget(self.label2) 
		self.verticalLayout_14 = QtWidgets.QVBoxLayout()
		self.verticalLayout_14.addWidget(self.label24)                 
		self.verticalLayout_14.addWidget(self.label25)                 
		self.verticalLayout_14.addWidget(self.label26)                 
		self.verticalLayout_14.addWidget(self.label27)                 
		self.verticalLayout_14.addWidget(self.label28)                 
		self.verticalLayout_14.addWidget(self.label29)                 
		self.verticalLayout_14.addWidget(self.label30)                 
		self.verticalLayout_14.addWidget(self.label31)                 
		self.verticalLayout_14.addWidget(self.label32)                 
		self.verticalLayout_14.addWidget(self.label33)                 
		self.verticalLayout_14.addWidget(self.label34)                 
		self.verticalLayout_14.addWidget(self.label35)                 
		self.verticalLayout_14.addWidget(self.label36)                 
		self.verticalLayout_14.addWidget(self.label37)                 
		self.verticalLayout_14.addWidget(self.label38)                 
		self.verticalLayout_14.addWidget(self.label39)                 
		self.verticalLayout_14.addWidget(self.label40)                 
		self.verticalLayout_14.addWidget(self.label41)                 
		self.verticalLayout_14.addWidget(self.label42)                 
		self.verticalLayout_14.addWidget(self.label43) 
		self.verticalLayout_15 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_15.addLayout(self.verticalLayout_13)                 
		self.verticalLayout_15.addLayout(self.verticalLayout_14)   
		self.verticalLayout_15.setStretch(0, 1) 
		self.verticalLayout_15.setStretch(0, 8) 
		self.verticalLayout_16 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_16.addWidget(self.label45) 
		self.verticalLayout_16.addWidget(self.label46) 
		self.verticalLayout_17 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_17.addWidget(self.label47) 
		self.verticalLayout_17.addWidget(self.label48) 
		self.verticalLayout_18 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_18.addWidget(self.label49) 
		self.verticalLayout_18.addWidget(self.label50)               
		self.groupBox_9 = QtWidgets.QGroupBox()
		self.groupBox_9.setFlat(False) 
		self.groupBox_9.setLayout(self.verticalLayout_15)
		self.groupBox_10 = QtWidgets.QGroupBox() 
		self.groupBox_10.setFlat(False) 
		self.groupBox_10.setLayout(self.verticalLayout_16)
		self.groupBox_11 = QtWidgets.QGroupBox() 
		self.groupBox_11.setFlat(False) 
		self.groupBox_11.setLayout(self.verticalLayout_17)
		self.groupBox_12 = QtWidgets.QGroupBox() 
		self.groupBox_12.setFlat(False) 
		self.groupBox_12.setLayout(self.verticalLayout_18)
		self.pushButton_1 = QtWidgets.QPushButton("Start",self.centralwidget)
		self.pushButton_1.setStyleSheet('QPushButton{color:#F0F0F0;border-image:url(button.png); \
										 border-radius:3px;font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;} \
										 QPushButton:hover{border-image:url(2.png);font-size:28px;color:#4DCCCF;}')
		self.pushButton_1.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.pushButton_2 = QtWidgets.QPushButton("Stop",self.centralwidget)
		self.pushButton_2.setStyleSheet('QPushButton{color:#F0F0F0;border-image:url(button.png);\
			                             border-radius:3px;font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;} \
			                             QPushButton:hover{border-image:url(2.png);font-size:28px;color:#4DCCCF;}')
		self.pushButton_2.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.pushButton_3 = QtWidgets.QPushButton("Clear",self.centralwidget)
		self.pushButton_3.setStyleSheet('QPushButton{color:#F0F0F0;border-image:url(button.png); \
			                             border-radius:3px;font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;} \
			                             QPushButton:hover{border-image:url(2.png);font-size:28px;color:#4DCCCF;}')
		self.pushButton_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.horizontalLayout_1 = QtWidgets.QHBoxLayout()           
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()                
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()           
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()           
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()           
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout() 
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout() 
		self.verticalLayout_1 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_4 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_5 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_6 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_7 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_8 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_9 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_10 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_11 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_12 = QtWidgets.QVBoxLayout()   
		self.verticalLayout_5.addWidget(self.label4)                 
		self.verticalLayout_5.addWidget(self.label5)
		self.verticalLayout_5.addWidget(self.label6)
		self.verticalLayout_5.setStretch(0, 1)  
		self.verticalLayout_5.setStretch(1, 3)    
		self.verticalLayout_5.setStretch(2, 1)              
		self.groupBox_1 =  QtWidgets.QGroupBox() 
		self.groupBox_1.setFlat(False) 
		self.groupBox_1.setLayout(self.verticalLayout_5)
		self.verticalLayout_6.addWidget(self.label7)                 
		self.verticalLayout_6.addWidget(self.label8)
		self.verticalLayout_6.addWidget(self.label9)
		self.verticalLayout_6.setStretch(0, 1)  
		self.verticalLayout_6.setStretch(1, 3)    
		self.verticalLayout_6.setStretch(2, 1)        
		self.groupBox_2 =  QtWidgets.QGroupBox() 
		self.groupBox_2.setFlat(False) 
		self.groupBox_2.setFlat(False) 
		self.groupBox_2.setLayout(self.verticalLayout_6)
		self.verticalLayout_7.addWidget(self.label10)                 
		self.verticalLayout_7.addWidget(self.label11)
		self.verticalLayout_7.addWidget(self.label12)
		self.verticalLayout_7.setStretch(0, 1)  
		self.verticalLayout_7.setStretch(1, 3)    
		self.verticalLayout_7.setStretch(2, 1)        
		self.groupBox_3 =  QtWidgets.QGroupBox() 
		self.groupBox_3.setFlat(False) 
		self.groupBox_3.setFlat(False) 
		self.groupBox_3.setLayout(self.verticalLayout_7)
		self.verticalLayout_8.addWidget(self.label13)                 
		self.verticalLayout_8.addWidget(self.label14)
		self.verticalLayout_8.addWidget(self.label15)
		self.verticalLayout_8.setStretch(0, 1)  
		self.verticalLayout_8.setStretch(1, 3)    
		self.verticalLayout_8.setStretch(2, 1)        
		self.groupBox_4 =  QtWidgets.QGroupBox() 
		self.groupBox_4.setFlat(False) 
		self.groupBox_4.setFlat(False) 
		self.groupBox_4.setLayout(self.verticalLayout_8)
		self.verticalLayout_9.addWidget(self.label16)                 
		self.verticalLayout_9.addWidget(self.label17)
		self.verticalLayout_9.addWidget(self.label18)
		self.verticalLayout_9.setStretch(0, 1)  
		self.verticalLayout_9.setStretch(1, 3)    
		self.verticalLayout_9.setStretch(2, 1)        
		self.groupBox_5 =  QtWidgets.QGroupBox() 
		self.groupBox_5.setFlat(False) 
		self.groupBox_5.setFlat(False) 
		self.groupBox_5.setLayout(self.verticalLayout_9)
		self.verticalLayout_10.addWidget(self.label19)                 
		self.verticalLayout_10.addWidget(self.label20)
		self.verticalLayout_10.addWidget(self.label21)
		self.verticalLayout_10.setStretch(0, 1)  
		self.verticalLayout_10.setStretch(1, 3)    
		self.verticalLayout_10.setStretch(2, 1)          
		self.groupBox_6 =  QtWidgets.QGroupBox() 
		self.groupBox_6.setFlat(False) 
		self.groupBox_6.setFlat(False) 
		self.groupBox_6.setLayout(self.verticalLayout_10)
		self.verticalLayout_11.addWidget(self.label44)                 
		self.verticalLayout_11.addWidget(self.label22)                 
		self.verticalLayout_11.addWidget(self.label23)
		self.verticalLayout_11.setStretch(0, 1)            
		self.verticalLayout_11.setStretch(1, 4)    
		self.verticalLayout_11.setStretch(2, 1)        
		self.groupBox_7 =  QtWidgets.QGroupBox() 
		self.groupBox_7.setFlat(False) 
		self.groupBox_7.setFlat(False) 
		self.groupBox_7.setLayout(self.verticalLayout_11)
		self.horizontalLayout_5.addWidget(self.groupBox_1)
		self.horizontalLayout_5.addWidget(self.groupBox_2)
		self.horizontalLayout_5.addWidget(self.groupBox_3)
		self.horizontalLayout_6.addWidget(self.groupBox_4)
		self.horizontalLayout_6.addWidget(self.groupBox_5)
		self.horizontalLayout_6.addWidget(self.groupBox_6)
		self.verticalLayout_12.addLayout(self.horizontalLayout_5)
		self.verticalLayout_12.addLayout(self.horizontalLayout_6)
		self.groupBox_8 =  QtWidgets.QGroupBox() 
		self.groupBox_8.setFlat(False) 
		self.groupBox_8.setLayout(self.verticalLayout_12)
		self.verticalLayout_2.addWidget(self.groupBox_8) 
		self.horizontalLayout_7.addWidget(self.pushButton_1)
		self.horizontalLayout_7.addWidget(self.pushButton_2)
		self.horizontalLayout_7.addWidget(self.pushButton_3)
		self.verticalLayout_3.addWidget(self.groupBox_7)
		self.verticalLayout_3.addLayout(self.horizontalLayout_7 )
		self.verticalLayout_3.setStretch(0, 5)
		self.verticalLayout_3.setStretch(1, 1)
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.horizontalLayout_1.addWidget(self.label)
		self.horizontalLayout_1.addWidget(self.label1)
		self.horizontalLayout_1.addWidget(self.btn1)
		self.horizontalLayout_1.addWidget(self.btn2)
		self.horizontalLayout_1.addWidget(self.btn3)
		self.horizontalLayout_1.setStretch(1, 4)
		self.horizontalLayout_1.setStretch(1, 9)
		self.horizontalLayout_1.setStretch(2, 1)
		self.horizontalLayout_1.setStretch(3, 1)
		self.horizontalLayout_1.setStretch(4, 1)
		self.horizontalLayout_2.addLayout(self.verticalLayout_1)
		self.horizontalLayout_2.addLayout(self.verticalLayout_2)
		self.horizontalLayout_2.addLayout(self.verticalLayout_3)
		self.horizontalLayout_2.setStretch(0, 1)
		self.horizontalLayout_2.setStretch(1, 2)
		self.horizontalLayout_2.setStretch(2, 1)
		self.verticalLayout_1.addWidget(self.groupBox_9)
		self.verticalLayout_1.addWidget(self.groupBox_10)
		self.verticalLayout_1.addWidget(self.groupBox_11)
		self.verticalLayout_1.addWidget(self.groupBox_12)
		self.verticalLayout_1.setStretch(0, 3)
		self.verticalLayout_1.setStretch(1, 1)
		self.verticalLayout_1.setStretch(2, 1)
		self.verticalLayout_1.setStretch(3, 1)
		self.verticalLayout_4.addLayout(self.horizontalLayout_1)
		self.verticalLayout_4.addLayout(self.horizontalLayout_2)
		self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
