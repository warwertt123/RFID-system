from PyQt5.QtCore import *
import serial
import serial.tools.list_ports
import sqlite3
import time
from datetime import datetime, timedelta
import pandas as pd
import os
import values
import psutil
import logging

class detect(QThread):
	"""RFID detected and data process"""

	update_signal = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.stop_flag = False
		
	def stop(self):
		self.stop_flag = True

	def restart(self):
		self.stop_flag = False

	def run(self):
		conn = sqlite3.connect('RFID.db')
		cursor = conn.cursor()
		if values.delete:
			cursor.execute("DELETE FROM in_out_time_temp" )
			conn.commit()
		conn.close()
		ports = list(serial.tools.list_ports.comports()) #search ports
		csv_date = datetime.now().strftime("%Y-%m-%d")
		for i in range(0,len(ports)):
			if 'Serial' in ports[i][1]:
				print(ports[i][0])                
				self.ser = serial.Serial(ports[i][0],115200) #open port   
		logging.basicConfig(handlers=[logging.FileHandler('Log.log', 'w', 'utf-8')], level=logging.INFO)
		while not self.stop_flag: 
			conn=sqlite3.connect('RFID.db')
			cursor=conn.cursor()			
			index=0
			rfid=''
			error_flag=False
			s=''
			try:
				s=self.ser.read(1)
			except:
				logging.error("紀錄時間:"+datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "COM讀取失敗")
			if s == b'A':
				try:
					rfid=rfid+s.decode()
					s=self.ser.read(11)
					rfid=rfid+s.decode()
					#print(rfid)
					info = psutil.virtual_memory()
					memory_using = info.percent
					print(memory_using)
					process = psutil.Process(os.getpid())
					print(process.memory_info().rss)

					if not instance(rfid,str):
						rfid=''				
				except:
					logging.error("紀錄時間:"+datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "COM讀取失敗")    
				now= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				if rfid != '':
					if (rfid not in values.first_check) and (rfid not in values.second_check):  #第一次進入
						try:
							values.first_check.append(rfid)
							values.third_check.append(rfid)
							values.six_pic.append(rfid)
							cursor.execute("INSERT INTO in_out_time  (NO, INOUTtime, State)  VALUES ('{0}','{1}','In')".format(rfid[4:11],now))
							cursor.execute("INSERT INTO in_out_time_temp  (NO, INOUTtime, STATUS)  VALUES ('{0}','{1}','In')".format(rfid,now))
							check_in= cursor.execute("SELECT INOUTtime  FROM in_out_time_temp WHERE NO='{0}'".format(rfid))
							people= cursor.execute("SELECT name , department  FROM PEOPLE_DATA WHERE NO='{0}'".format(rfid))
							for aaa in people:
								values.people_data.append("   部門:  %s\n   人員:  %s" % (aaa[1],aaa[0]))   
							values.people_data.append('#99F73142')						
							conn.commit()				
							values.index+=1
							values.date_time.append('#99F73142')					
							values.date_time.append(0)
							values.clock.append('1') 					
							values.enter.append('#99F73142')					
							values.enter.append(now+'  '+rfid[4:13]+'\n')
							self.update_signal.emit() 
						except:
							logging.error("紀錄時間:"+datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "COM讀取失敗") 
					elif rfid in values.second_check:  #第二次進入
						try:
							second_in= cursor.execute("SELECT INOUTtime  FROM in_out_time_temp WHERE NO='{0}'".format(rfid))
							aaa=[]
							bbb=[]
							for aaa in second_in:
								break
							now_time=datetime.strptime(now,("%Y-%m-%d %H:%M:%S"))
							past_time=datetime.strptime(aaa[0],("%Y-%m-%d %H:%M:%S"))	+timedelta(seconds=10)	
							if now_time>past_time:
								if rfid in values.six_pic: #超過六個人圖片LIST會被清掉
									delete_ind=values.six_pic.index(rfid)
									del values.people_data[delete_ind*2]
									del values.people_data[delete_ind*2]
									values.people_data.appendleft("")					
									values.people_data.appendleft("")					
									del values.date_time[delete_ind*2]
									del values.date_time[delete_ind*2]
									values.date_time.appendleft(0)											
									values.date_time.appendleft('transparent')	
									del values.clock[delete_ind]					
									values.clock.appendleft('2')
									del values.six_pic[delete_ind]
									values.six_pic.appendleft([''])
								people= cursor.execute("SELECT name , department  FROM PEOPLE_DATA WHERE NO='{0}'".format(rfid))
								for bbb in people:
									values.people_data.append("   部門:  %s\n   人員:   %s" % (bbb[1],bbb[0])) 
								values.people_data.append('#99F73142')
								cursor.execute("DELETE FROM in_out_time_temp  WHERE NO='{0}'".format(rfid))	
								cursor.execute("INSERT INTO in_out_time_temp  (NO, INOUTtime, STATUS)  VALUES ('{0}','{1}','In')".format(rfid,now))
								cursor.execute("INSERT INTO in_out_time  (NO, INOUTtime, State)  VALUES ('{0}','{1}','In')".format(rfid[4:11],now))
								conn.commit()	
								values.first_check.append(rfid)												
								values.second_check.remove(rfid)	
								values.third_check.remove(rfid)																	
								values.third_check.append(rfid)
								values.date_time.append('#99F73142')					
								values.date_time.append(0)	
								values.clock.append('1')   						            
								values.six_pic.append(rfid)						
								values.index+=1
								values.enter.append('#99F73142')					
								values.enter.append(now+'  '+rfid[4:13]+'\n')
								self.update_signal.emit() 
						except:
							logging.error("紀錄時間:"+datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "COM讀取失敗") 
					else:  #出場
						try:
							check_in= cursor.execute("SELECT INOUTtime  FROM in_out_time_temp WHERE NO='{0}'".format(rfid))
							ccc=[]
							ddd=[]
							for ccc in check_in:
								print(ccc)
								break
							now_time=datetime.strptime(now,("%Y-%m-%d %H:%M:%S"))
							past_time=datetime.strptime(ccc[0],("%Y-%m-%d %H:%M:%S"))+timedelta(seconds=10)	
							if now_time>past_time:
							
								if rfid in values.six_pic: #超過六個人圖片LIST會被清掉
									delete_ind=values.six_pic.index(rfid)
									del values.people_data[delete_ind*2]
									del values.people_data[delete_ind*2]
									values.people_data.appendleft("")					
									values.people_data.appendleft("")					
									del values.date_time[delete_ind*2]
									del values.date_time[delete_ind*2]
									values.date_time.appendleft(0)											
									values.date_time.appendleft('transparent')	
									del values.clock[delete_ind]					
									values.clock.appendleft('2')
									del values.six_pic[delete_ind]
									values.six_pic.appendleft([''])
								people= cursor.execute("SELECT name , department  FROM PEOPLE_DATA WHERE NO='{0}'".format(rfid))
								for ddd in people:
									values.people_data.append("   部門:  %s\n   人員:  %s" % (ddd[1],ddd[0])) 
								values.people_data.append('#999FFFC2')						
								cursor.execute("DELETE FROM in_out_time_temp  WHERE NO='{0}'".format(rfid))	
								cursor.execute("INSERT INTO in_out_time_temp  (NO, INOUTtime,STATUS)  VALUES ('{0}','{1}','Out')".format(rfid,now))
								cursor.execute("INSERT INTO in_out_time  (NO, INOUTtime, State)  VALUES ('{0}','{1}','Out')".format(rfid[4:11],now))
								conn.commit()	
								values.first_check.remove(rfid)												
								values.third_check.remove(rfid)
								values.second_check.append(rfid)												
								values.third_check.append(rfid)
								values.date_time.append('#999FFFC2')					
								values.date_time.append(0)
								values.clock.append('0') 						
								values.six_pic.append(rfid)						
								values.index-=1
								values.enter.append('#999FFFC2')		
								values.enter.append(now+'  '+rfid[4:13]+'\n')
								self.update_signal.emit() 
						except:
							logging.error("紀錄時間:"+datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "COM讀取失敗") 
			if csv_date  < datetime.now().strftime("%Y-%m-%d"):  #reset databse for one day
				cursor.execute("SELECT * FROM in_out_time") #TEST
				his_data=cursor.fetchall()
				col_result = cursor.description                                    
				column = []
				for i in range(len(col_result)):
					column.append(col_result[i][0])
					df = pd.DataFrame(columns=column)  
                                            
				for i in range(len(his_data)):
					df.loc[i] = list(his_data[i])    
				file='employee/%s.csv' % datetime.now().strftime("%Y-%m-%d")
				if os.path.isfile(file): 
					flag=1
					file = file[:-4]+'_1.csv'
					num=1
					while flag:
						if os.path.isfile(file):
							num+=1
							file = file[:-6]+'_%s.csv' % num
						else:
							df.to_csv(file,index=False) 
							flag=0
				else:                                
					df.to_csv(file,index=False)                                        
				cursor.execute("DELETE FROM in_out_time" )
				conn.commit()
				csv_date = datetime.now().strftime("%Y-%m-%d")
				try:
					os.remove('Log.log') #可能正好遇到讀寫狀態
				except:
					pass
				today_time = datetime.now()
				for ddd in range(15,29):
					week_date = today_time + timedelta(days = -ddd)
					week_day= week_date.strftime("%Y-%m-%d")
					locate = 'employee/'+week_day+'.csv'
					if os.path.isfile(locate):
						os.remove(locate)
			conn.close()
