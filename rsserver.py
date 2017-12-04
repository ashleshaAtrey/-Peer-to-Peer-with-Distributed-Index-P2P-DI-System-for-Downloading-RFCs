import socket
import datetime
import threading
import shlex

def main():
	global j
	j=1
	thread10=threading.Thread(target=server)
	thread10.daemon= True
	thread10.start()
	while True:
		print "Press 1 to EXIT"
		i=raw_input()
		if i=='1':
			return


def server():
	TCP_IP = '127.0.0.1'
	TCP_PORT = 55567
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	while True:
		s.listen(6)
    		print "Waiting for incoming connections..."
    		(conn, (ip,port)) = s.accept()
		thread1=threading.Thread(target=mainserver,args=(conn,ip,port,))
		thread1.daemon= True
		thread1.start()
	tcpsock.close()
	return


def mainserver(conn,ip,port):
		global j
    		print 'Got connection from ', (ip,port)
		y=conn.recv(1024)
		z=shlex.split(y)
		print y
		t=datetime.datetime.now().time()
		timex=(t.hour * 60 + t.minute) * 60 + t.second
		#print timex		
		Dictionary.counter(timex,j)
		j=j+1	
		if z[0]=="Register":
			servport=z[1]
			Dictionary.register(ip,port,conn,servport)

		if z[0]=="Leave":
			Dictionary.leave(ip,port,conn)

		if z[0]=="PQuery":
			Dictionary.pquery(ip,conn)

		if z[0]=="KeepAlive":
			Dictionary.keepalive(ip,conn)

class Dictionary:
	#def __init__(self):
	database={}
	cookie=45
	timey=0
	
	
	
	@staticmethod
	def register(ip,port,conn,servport):
		
		fl=0
		#print Dictionary.dict
		for key in Dictionary.database.keys():
			#print "inside f"
			#print Dictionary.dict[x]
			if key==ip:
				y= "Version 1.1 \n Status code: Passed \n Client already registered with cookie: "+ str(Dictionary.database[key][0])
				Dictionary.database[ip][4]=Dictionary.database[ip][4]+1
				
				if Dictionary.database[ip][1]==False:
					Dictionary.database[ip][1]==True
					Dictionary.database[ip][2]==7200	
				fl=1
				break 	
		
		if fl==0:
			rgno=1
			time= str(datetime.datetime.now())
			data=[Dictionary.cookie,True,7200,servport,rgno,time]
			Dictionary.database.update({ip:data})
			#print Dictionary.dict
			c=str(Dictionary.cookie)
			y= "Version 1.1 /n Status code: Passed \n Client registered successfully with cookie: " + c
			Dictionary.cookie=Dictionary.cookie+1
			
			#cookie=str(cookie)
		conn.send(y)
		conn.close()
		return
	@staticmethod
	def leave(ip,port,conn):
		
		Dictionary.database[ip][1]=False
		y="Version 1.1 \n Status code: Passed \n Client is marked as inactive"
		conn.send(y)
		conn.close()	
		return
	@staticmethod
	def pquery(ip,conn):
		data=[]
		time=datetime.datetime.now()
		Dictionary.database[ip][2]=7200
		Dictionary.database[ip][5]=time
		for x in Dictionary.database.keys():
				g=str(Dictionary.database[x][2])
				if Dictionary.database[x][1]== True:
					list1=[x,Dictionary.database[x][3],g]
					data.append(list1)
		msg="Version 1.1 \n Status code: Passed \n Active list directory"
		#print len(msg)
		conn.send(msg)
		#print data
		for z in data:
			for e in z:
				conn.send(e)
				conn.send(" ")	
		conn.close()
		return
	@staticmethod
	def keepalive(ip,conn):
		Dictionary.database[ip][2]=7200
		if Dictionary.database[ip][1]== False:
			Dictionary.database[ip][1]=True
		y="Version 1.1 \n Status code: Passed \n Client TTL set to 7200 sec"
		conn.send(y)
		conn.close()
		return	

	@staticmethod
	def counter(timex,j):
		if j==1:
			z=0
			Dictionary.timey=timex
		else:
			z=timex-Dictionary.timey
		
		for x in Dictionary.database.keys():
			if Dictionary.database[x][1]==True:
				Dictionary.database[x][2]=Dictionary.database[x][2]-z
				#print Dictionary.database[x][2]

		for t in Dictionary.database.keys():
			if Dictionary.database[t][2] <= 0:
					#print t
					Dictionary.database[t][1]=False
					#print Dictionary.database[t]
			
if __name__=="__main__":

	main()

