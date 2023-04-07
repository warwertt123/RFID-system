from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import time
from datetime import datetime, timedelta
import os
from PIL import Image
import glob
import values
import sqlite3
from collections import deque 
import math
import os
from qt_layout import Ui_MainWindow
from rfid_detect import detect


class temp_data(QThread):  


	update_signal = pyqtSignal()  

	def __init__(self):
		super().__init__()
		self.stop_flag = False
		
	def stop(self):
		self.stop_flag = True

	def restart(self):
		self.stop_flag = False

	def run(self):
		while not self.stop_flag: 
			conn = sqlite3.connect('RFID.db')
			cursor = conn.cursor()
			cursor.execute( "SELECT COUNT(DISTINCT INOUTtime) FROM in_out_time_temp \
				             WHERE INOUTtime < (datetime('now','localtime', '-9 hour'))")
			values.time_out_count = cursor.fetchone()
			cursor.execute( "SELECT COUNT(PEOPLE_DATA.Health_EX) FROM in_out_time_temp JOIN PEOPLE_DATA  \
				             ON in_out_time_temp.NO=PEOPLE_DATA.NO  WHERE  PEOPLE_DATA.Health_EX='Y' and STATUS='In'")
			values.Health_EX_count = cursor.fetchone()
			cursor.execute( "SELECT COUNT(PEOPLE_DATA.Temp_Enter)  FROM in_out_time_temp JOIN PEOPLE_DATA  \
				             ON in_out_time_temp.NO=PEOPLE_DATA.NO  WHERE  PEOPLE_DATA.Temp_Enter='Y' and STATUS='In'")
			values.Temp_Enter_count = cursor.fetchone()
			conn.close()	
			self.update_signal.emit() 
			time.sleep(3)


class MainWindow(QtWidgets.QMainWindow):
	"""UI logic"""

	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow() 
		self.flag = Qt.WindowFlags()
		self.ui.setupUi(self)      
		self.setWindowTitle('Access control')    
		self.ui.btn1.clicked.connect(self.showMinimized)
		self.ui.btn2.clicked.connect(self.screen)
		self.ui.btn3.clicked.connect(self.close)		
		self.ui.pushButton_1.clicked.connect(self.detect_thread)
		self.ui.pushButton_2.clicked.connect(self.stop_thread)
		self.ui.pushButton_3.clicked.connect(self.clear_data)
		self.timer = QTimer(self)       
		self.timer.timeout.connect(self.count_down)
		self.ui.label2.setText('進入人數  : 0') 
		self.ui.label45.setText('超時人數 (9小時)') 
		self.ui.label47.setText('體檢合格人數') 
		self.ui.label49.setText('臨時入場人數') 

	def detect_thread(self):
		try:
			self.timer.start(1000)
			self.ui.pushButton_1.setEnabled(False)
			self.ui.pushButton_1.setStyleSheet('QPushButton{border-image:url(1.png);font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;color:#F73142;}')
			self.detect.start()	
			self.temp_data.start()			
		except:
			self.timer.start(1000)
			self.ui.pushButton_1.setEnabled(False)
			self.ui.pushButton_1.setStyleSheet('QPushButton{border-image:url(1.png);font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;color:#F73142;}')
			self.detect = detect()
			self.temp_data = temp_data()			
			self.detect.start()	
			self.temp_data.start()			
			self.detect.update_signal.connect(self.get_data) 
			self.temp_data.update_signal.connect(self.temp_data_update) 		

	def clock_time(self):	
		current_time = QTime.currentTime()  
		label_time = current_time.toString('hh:mm:ss') 
		self.ui.label44.setText(label_time)

	def count_down(self):	
		self.clock_time()
		time_1 = int(values.date_time[1])+1
		time_2 = int(values.date_time[3])+1
		time_3 = int(values.date_time[5])+1
		time_4 = int(values.date_time[7])+1
		time_5 = int(values.date_time[9])+1
		time_6 = int(values.date_time[11])+1
		values.time_s1 = time.strftime("%H:%M:%S", time.gmtime(time_1))
		values.time_s2 = time.strftime("%H:%M:%S", time.gmtime(time_2))
		values.time_s3 = time.strftime("%H:%M:%S", time.gmtime(time_3))
		values.time_s4 = time.strftime("%H:%M:%S", time.gmtime(time_4))
		values.time_s5 = time.strftime("%H:%M:%S", time.gmtime(time_5))
		values.time_s6 = time.strftime("%H:%M:%S", time.gmtime(time_6))
		values.date_time[1] = time_1
		values.date_time[3] = time_2
		values.date_time[5] = time_3		
		values.date_time[7] = time_4
		values.date_time[9] = time_5
		values.date_time[11] = time_6
		if values.clock[5] == '1':
			self.ui.label4.setText("<font color=#{0}>{1}</font>".format(values.date_time[10][3:9], values.time_s6))
		elif values.clock[5] == '0':
			self.ui.label4.setText("<font color=#{0}>{1}</font>".format(values.date_time[10][3:9], "Exit"))
		if values.clock[4] == '1':
			self.ui.label7.setText("<font color=#{0}>{1}</font>".format(values.date_time[8][3:9], values.time_s5))
		elif values.clock[4] == '0':
			self.ui.label7.setText("<font color=#{0}>{1}</font>".format(values.date_time[8][3:9], "Exit"))		
		if values.clock[3] == '1':
			self.ui.label10.setText("<font color=#{0}>{1}</font>".format(values.date_time[6][3:9], values.time_s4))
		elif values.clock[3] == '0':
			self.ui.label10.setText("<font color=#{0}>{1}</font>".format(values.date_time[6][3:9], "Exit"))
		if values.clock[2] == '1':			
			self.ui.label13.setText("<font color=#{0}>{1}</font>".format(values.date_time[4][3:9], values.time_s3))
		elif values.clock[2] == '0':
			self.ui.label13.setText("<font color=#{0}>{1}</font>".format(values.date_time[4][3:9], "Exit"))
		if values.clock[1] == '1':
			self.ui.label16.setText("<font color=#{0}>{1}</font>".format(values.date_time[2][3:9], values.time_s2))
		elif values.clock[1] == '0':
			self.ui.label16.setText("<font color=#{0}>{1}</font>".format(values.date_time[2][3:9], "Exit"))			
		if values.clock[0] == '1':
			self.ui.label19.setText("<font color=#{0}>{1}</font>".format(values.date_time[0][3:9], values.time_s1))
		elif values.clock[0] == '0':
			self.ui.label19.setText("<font color=#{0}>{1}</font>".format(values.date_time[0][3:9], "Exit"))

	def get_data(self):
		pic = QPixmap('pic/%s.jpg' % values.third_check[-1]).scaled(100,120, Qt.IgnoreAspectRatio)
		self.ui.label22.setPixmap(QPixmap(""))
		self.ui.label22.setPixmap(pic)        
		self.ui.label22.setScaledContents(True)
		self.ui.label23.setText(values.people_data[-2]) 
		self.ui.label23.setStyleSheet("QLabel{color:#FCFCFC;}"
									"QLabel{font-size:32px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:QLinearGradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 transparent, stop: 1 %s);}" %values.people_data[-1])
		self.ui.label2.setText('進入人數  :  %d' % values.index) 
		self.ui.label24.setText("<font color=%s>%s</font>" % (values.enter[0], values.enter[1]))
		self.ui.label25.setText("<font color=%s>%s</font>" % (values.enter[2], values.enter[3]))
		self.ui.label26.setText("<font color=%s>%s</font>" % (values.enter[4], values.enter[5]))
		self.ui.label27.setText("<font color=%s>%s</font>" % (values.enter[6], values.enter[7]))
		self.ui.label28.setText("<font color=%s>%s</font>" % (values.enter[8], values.enter[9]))
		self.ui.label29.setText("<font color=%s>%s</font>" % (values.enter[10], values.enter[11]))
		self.ui.label30.setText("<font color=%s>%s</font>" % (values.enter[12], values.enter[13]))
		self.ui.label31.setText("<font color=%s>%s</font>" % (values.enter[14], values.enter[15]))
		self.ui.label32.setText("<font color=%s>%s</font>" % (values.enter[16], values.enter[17]))
		self.ui.label33.setText("<font color=%s>%s</font>" % (values.enter[18], values.enter[19]))
		self.ui.label34.setText("<font color=%s>%s</font>" % (values.enter[20], values.enter[21]))
		self.ui.label35.setText("<font color=%s>%s</font>" % (values.enter[22], values.enter[23]))
		self.ui.label36.setText("<font color=%s>%s</font>" % (values.enter[24], values.enter[25]))
		self.ui.label37.setText("<font color=%s>%s</font>" % (values.enter[26], values.enter[27]))
		self.ui.label38.setText("<font color=%s>%s</font>" % (values.enter[28], values.enter[29]))
		self.ui.label39.setText("<font color=%s>%s</font>" % (values.enter[30], values.enter[31]))
		self.ui.label40.setText("<font color=%s>%s</font>" % (values.enter[32], values.enter[33]))
		self.ui.label41.setText("<font color=%s>%s</font>" % (values.enter[34], values.enter[35]))
		self.ui.label42.setText("<font color=%s>%s</font>" % (values.enter[36], values.enter[37]))
		self.ui.label43.setText("<font color=%s>%s</font>" % (values.enter[38], values.enter[39]))
		self.ui.label5.setPixmap(QPixmap(""))
		self.ui.label5.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[5]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label5.setScaledContents(True)
		self.ui.label8.setPixmap(QPixmap(""))
		self.ui.label8.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[4]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label8.setScaledContents(True)		
		self.ui.label11.setPixmap(QPixmap(""))
		self.ui.label11.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[3]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label11.setScaledContents(True)
		self.ui.label14.setPixmap(QPixmap(""))
		self.ui.label14.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[2]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label14.setScaledContents(True)
		self.ui.label17.setPixmap(QPixmap(""))
		self.ui.label17.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[1]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label17.setScaledContents(True)
		self.ui.label20.setPixmap(QPixmap(""))
		self.ui.label20.setPixmap(QPixmap('pic/%s.jpg' % values.six_pic[0]).scaled(100,120, Qt.IgnoreAspectRatio))        
		self.ui.label20.setScaledContents(True)
		self.ui.label6.setText(values.people_data[10]) 
		self.ui.label6.setStyleSheet("QLabel{border-radius:5px ; color:#FCFCFC ; font-size:20px ; font-weight:bold ; font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0  y1: 0, x2: 0, y2: 1, stop: 0 transparent, stop: 1 %s);}" %values.people_data[11])
		self.ui.label9.setText(values.people_data[8]) 
		self.ui.label9.setStyleSheet("QLabel{border-radius:5px;color:#FCFCFC;font-size:20px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #990D3F67, stop: 1 %s);}" %values.people_data[9])
		self.ui.label12.setText(values.people_data[6]) 
		self.ui.label12.setStyleSheet("QLabel{border-radius:5px;color:#FCFCFC;font-size:20px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #990D3F67, stop: 1 %s);}" %values.people_data[7])
		self.ui.label15.setText(values.people_data[4]) 
		self.ui.label15.setStyleSheet("QLabel{border-radius:5px;color:#FCFCFC;font-size:20px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #990D3F67, stop: 1 %s);}" %values.people_data[5])
		self.ui.label18.setText(values.people_data[2]) 
		self.ui.label18.setStyleSheet("QLabel{border-radius:5px;color:#FCFCFC;font-size:20px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #990D3F67, stop: 1 %s);}" %values.people_data[3])
		self.ui.label21.setText(values.people_data[0]) 
		self.ui.label21.setStyleSheet("QLabel{border-radius:5px;color:#FCFCFC;font-size:20px;font-weight:bold;font-family:Bahnschrift SemiLight;}"
									"QLabel{background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #990D3F67, stop: 1 %s);}" %values.people_data[1])

	def temp_data_update(self):  
		self.ui.label46.setText("<font color=#99F73142>%s</font>" % values.time_out_count)
		self.ui.label48.setText("<font color=#99F73142>%s</font>" % values.Health_EX_count)
		self.ui.label50.setText("<font color=#99F73142>%s</font>" % values.Temp_Enter_count)

	def clear_data(self):
		conn = sqlite3.connect('RFID.db')
		cursor = conn.cursor()		
		cursor.execute("DELETE FROM in_out_time_temp")	
		conn.commit()
		conn.close()
		values.delete = 1		
		values.index = 0
		values.first_check = []
		values.second_check = []
		values.third_check = []
		values.six_pic = deque(['', '', '', '', '', ''], maxlen=6)
		values.enter = deque(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
			                  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], maxlen=40)
		values.people_data = deque(["", "transparent", "", "transparent", "", "transparent", "", 
			                        "transparent", "", "transparent", "", "transparent"], maxlen=12)
		values.date_time = deque(["", "", "", "", "", "", "", "", "", "", "", ""], maxlen=12)
		values.date_clock = deque([2, 2, 2, 2, 2, 2], maxlen=6)
		values.clock = deque([2, 2, 2, 2, 2, 2], maxlen=6)
		values.time_s1 = "00:00:00"
		values.time_s2 = "00:00:00"
		values.time_s2 = "00:00:00"
		values.time_s4 = "00:00:00"
		values.time_s5 = "00:00:00"
		values.time_s6 = "00:00:00"
		values.date_time = deque(["", "0", "", "0", "", "0", "", "0", "", "0", "", "0"], maxlen=12)
		self.ui.label4.setText("")
		self.ui.label7.setText("")
		self.ui.label10.setText("")
		self.ui.label13.setText("")
		self.ui.label16.setText("")
		self.ui.label19.setText("")
		self.ui.label22.setPixmap(QPixmap(""))
		self.ui.label23.setText("") 
		self.ui.label23.setStyleSheet("QLabel{background:transparent}")   
		self.ui.label2.setText("") 
		self.ui.label24.setText("")
		self.ui.label25.setText("")
		self.ui.label26.setText("")
		self.ui.label27.setText("")
		self.ui.label28.setText("")
		self.ui.label29.setText("")
		self.ui.label30.setText("")
		self.ui.label31.setText("")
		self.ui.label32.setText("")
		self.ui.label33.setText("")
		self.ui.label34.setText("")
		self.ui.label35.setText("")
		self.ui.label36.setText("")
		self.ui.label37.setText("")
		self.ui.label38.setText("")
		self.ui.label39.setText("")
		self.ui.label40.setText("")
		self.ui.label41.setText("")
		self.ui.label42.setText("")
		self.ui.label43.setText("")
		self.ui.label5.setPixmap(QPixmap(""))
		self.ui.label8.setPixmap(QPixmap(""))	
		self.ui.label11.setPixmap(QPixmap(""))
		self.ui.label14.setPixmap(QPixmap(""))
		self.ui.label17.setPixmap(QPixmap(""))
		self.ui.label20.setPixmap(QPixmap(""))
		self.ui.label6.setText("")
		self.ui.label9.setText("")
		self.ui.label12.setText("")
		self.ui.label15.setText("")
		self.ui.label18.setText("") 
		self.ui.label21.setText("")
		self.ui.label6.setStyleSheet("QLabel{background:transparent}") 
		self.ui.label9.setStyleSheet("QLabel{background:transparent}") 
		self.ui.label12.setStyleSheet("QLabel{background:transparent}") 
		self.ui.label15.setStyleSheet("QLabel{background:transparent}") 
		self.ui.label18.setStyleSheet("QLabel{background:transparent}") 
		self.ui.label21.setStyleSheet("QLabel{background:transparent}") 

	def stop_thread(self):
		try:
			self.timer.stop()
			self.detect.stop()
			self.temp_data.stop()			
			self.detect.ser.close() 
			self.ui.pushButton_1.setEnabled(True)	        
			self.ui.pushButton_1.setStyleSheet('QPushButton{color:#F0F0F0;border-image:url(button.png); \
				                                border-radius:3px;font-weight:bold;font-family:Bahnschrift SemiLight;font-size:32px;} \
				                                QPushButton:hover{border-image:url(2.png);font-size:28px;color:#4DCCCF;}')
			print('Thread Stop: Com port close')
			values.delete=0
		except:
			print('Thread does not run')

	def screen(self):
		if self.isFullScreen()  is False:
			self.showFullScreen()
			self.flag=False
		else:
			self.showNormal()

	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton and self.isFullScreen()==False:  #按下滑鼠左鍵視窗為全螢幕
			self.flag=True
			self.flagPosition=event.globalPos()-self.pos()  #計算滑鼠座標到界面座標的偏移量
			event.accept()
			self.setCursor(self.cursor)
			self.setCursor(QCursor(Qt.OpenHandCursor))

	def mouseMoveEvent(self, QMouseEvent):
		if Qt.LeftButton and self.flag:
			self.move(QMouseEvent.globalPos()-self.flagPosition) #移動滑鼠座標位置減去偏移量的距離
			QMouseEvent.accept()

	def mouseReleaseEvent(self, QMouseEvent):
		self.flag=False
		self.setCursor(self.ui.cursor)

	def closeEvent(self, event):
		reply = QtWidgets.QMessageBox.question(self,'!!!',"Exit？",
											   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
											   QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:
			event.accept()             
			sys.exit(app.exec_())
			os._exit(0)
		else:
			event.ignore()

if __name__ == '__main__':
	app =QtWidgets.QApplication(sys.argv)
	new = MainWindow()
	new.show()
	sys.exit(app.exec_())
