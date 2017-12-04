import socket
import threading
import shlex
import os
import platform
import datetime
import time

def GetRFC(RFC_NO,ServHost,msg):
        #t=datetime.datetime.now().time()
        starts=int(round(time.time() * 1000))
        global list1

        file1="rfc"+RFC_NO
        file1=file1+".pdf"

        with open('list') as f:
                 #print "inside file "
                 list3 = f.read().split("\n")
                 f.close 
        for hx in list3:
                if hx==RFC_NO:
                        print "File already in local database"
                        return
        for y in range(0,len(list1)):
                rfclist=list1[y][3]
                #print rfclist
                for a in rfclist:
                        filename="rfc"+a
                        filename=filename+".pdf"
                        if file1==filename:
                                sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                #sx.bind((clientHost,clientPort))
                                port=list1[y][1]
                                port=int(port)
                                ip=list1[y][0]
                                sx.connect((ip,port))
                                msg="GETRFC "+a+" "+"P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                                sx.send(msg)
                                q=sx.recv(46)
                                print q 
                                q1=shlex.split(q)
                                if q1[6]=='not':
                                        sx.close()
                                else:
                                        with open(filename, 'wb') as f:
                                                #print 'File opened'
                                                while True:
                                                        #print('receiving data...')
                                                        data = sx.recv(1024)
                                                        #print('data=%s', (data))
                                                        if not data:
                                                                f.close()
                                                                #print 'file close()'
                                                                break
                                                        # write data to a file
                                                        f.write(data)

                                        with open("list",'a') as f:
                                                f.write(a + os.linesep)
                                                f.close()
                                        sx.close()
                                        print "File received succcessfully from host"+ list1[y][0]
                                        #t=datetime.datetime.now().time()
                                        stops=int(round(time.time() * 1000))
                                        diff=stops-starts
                                        print "Time taken to receive RFC  "+filename+" is "+str(diff)
                                        return

def GetfromallRFC(ServHost):                    #decentralized
        starts=int(round(time.time() * 1000))
        global list1            
        for y in range(0,len(list1)):
                if list1[y][0]!=ServHost:
                        port=int(list1[y][1])
                        ip=list1[y][0]
                        msg2="RFCQuery P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                        getList(ip,port,ServHost,msg2)
                        rfclist=list1[y][3]
                        for a in rfclist:
                                flag=1
                                with open('list') as f:
                                         #print "inside file "
                                         list3 = f.read().split("\n")
                                         f.close 
                                for hx in list3:
                                        if hx==a:
                                                flag=0
                                if flag==1:
                                        sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        #sx.bind((clientHost,clientPort))
                                        sx.connect((ip,port))
                                        msg="GETRFC "+a+" "+"P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                                        sx.send(msg)
                                        filename="rfc"+a
                                        filename=filename+".pdf"
                                        q=sx.recv(43)
                                        q1=shlex.split(q)
                                        print q
                                        if q1[6]=='NOTfound':
                                                #print "File not found with host: "+y[0]
                                                sx.close()
                                        else:
                                                with open(filename, 'wb') as f:
                                                        while True:
                                                                data = sx.recv(1024)
                                                                if not data:
                                                                        f.close()
                                                                        #print 'file close()'
                                                                        break
                                                                # write data to a file
                                                                f.write(data)

                                                with open("list",'a') as f:
                                                        f.write(a + os.linesep)
                                                        f.close()
                                                sx.close()
                                                print "File received succcessfully from host"+ list1[y][0]
                                                stops=int(round(time.time() * 1000))
                                                diff=stops-starts
                                                dif=str(diff)
                                                print "Time taken to receive RFC  "+filename+" is "+str(diff)
                                                with open("c1-test2",'a') as f:
                                                        f.write(dif+ os.linesep)
                                                        f.close()
        return
        



def bestcase(ServHost):                 #decentralized
        starts=int(round(time.time() * 1000))
        global list1    
        listbest=[["127.0.0.3",65403,1],["127.0.0.4",65404,2],["127.0.0.5",65405,3],["127.0.0.6",65406,4],["127.0.0.7",65407,5]]        
        count=0
        for y in range(0,len(listbest)):
                if listbest[y][0]!=ServHost:
                        port=int(listbest[y][1])
                        ip=listbest[y][0]
                        msg2="RFCQuery P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                        getList(ip,port,ServHost,msg2)
                        d=listbest[y][2]
                        rfclist=list1[d][3]
                        for a in rfclist:
                                        flag=1
                                        with open('list') as f:
                                                 #print "inside file "
                                                 list3 = f.read().split("\n")
                                                 f.close 
                                        for hx in list3:
                                                if hx==a:
                                                        flag=0
                                        if flag==1:
                                                sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                #sx.bind((clientHost,clientPort))
                                                sx.connect((ip,port))
                                                msg="GETRFC "+a+" "+"P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                                                sx.send(msg)
                                                filename="rfc"+a
                                                filename=filename+".pdf"
                                                q=sx.recv(43)
                                                q1=shlex.split(q)
                                                print q
                                                if q1[6]=='NOTfound':
                                                        #print "File not found with host: "+y[0]
                                                        sx.close()
                                                else:
                                                        with open(filename, 'wb') as f:
                                                                #print 'File opened'
                                                                        while True:
                                                                        #print('receiving data...')
                                                                                data = sx.recv(1024)
                                                                                #print('data=%s', (data))
                                                                                if not data:
                                                                                        f.close()
                                                                                        #print 'file close()'
                                                                                        break
                                                                                # write data to a file
                                                                                f.write(data)

                                                        with open("list",'a') as f:
                                                                f.write(a + os.linesep)
                                                                f.close()
                                                        sx.close()
                                                        print "File received succcessfully from host"+ list1[y][0]
                                                        stops=int(round(time.time() * 1000))
                                                        diff=stops-starts
                                                        dif=str(diff)
                                                        print "Time taken to receive RFC  "+filename+" is "+str(diff)
                                                        with open("c1-test2",'a') as f:
                                                                f.write(dif+ os.linesep)
                                                                f.close()
                                                        count=count+1
                                                        if count==50:
                                                                return
        return

def GetallRFC(ip,port,ServHost):                  #centralized
        starts=int(round(time.time() * 1000))
        global list1    
        count=0
        for y in range(0,len(list1)):
                if list1[y][0]==ip:
                        rfclist=list1[y][3]
                        for a in rfclist:
                                sx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                #sx.bind((clientHost,clientPort))
                                sx.connect((ip,port))
                                msg="GETRFC "+a+" "+"P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                                #print len(msg)
                                sx.send(msg)
                                filename="rfc"+a
                                filename=filename+".pdf"
                                q=sx.recv(43)
                                q1=shlex.split(q)
                                print q
                                if q1[6]=='NOTfound':
                                        sx.close()
                                else:
                                        with open(filename, 'wb') as f:
                                                #print 'File opened'
                                                while True:
                                                        #print('receiving data...')
                                                        data = sx.recv(1024)
                                                        #print('data=%s', (data))
                                                        if not data:
                                                                f.close()
                                                                #print 'file close()'
                                                                break
                                                        # write data to a file
                                                        f.write(data)

                                        with open("list",'a') as f:
                                                f.write(a + os.linesep)
                                                f.close()
                                        sx.close()
                                        print "File received succcessfully from host"+ list1[y][0]
                                        stops=int(round(time.time() * 1000))
                                        diff=stops-starts
                                        dif=str(diff)
                                        print "Time taken to receive RFC  "+filename+" is "+str(diff)
                                        with open("c1-test1",'a') as f:
                                                        f.write(dif+ os.linesep)
                                                        f.close()
                                        count=count+1
                                        if count==50:
                                                return
                                        
        return



def getList(ip,port,ServHost,msg1):
                global list1
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #s.bind((clientHost,clientPort))
                s.connect((ip,port))
                s.send(msg1)
                data1=s.recv(67)
                print data1
                #msg=s.recv(1024)
                #print msg
                data=s.recv(1024)
                z=shlex.split(data)
                print z
                s.close()
                
                for y in range(0,len(list1)):
                        #print "inside for"
                        if list1[y][0]==ip:
                                list1[y][3]=z
                        if ip == ServHost:
                                with open('list') as f:
                                        list3 = f.read().split("\n")
                                        f.close 
                                list1[y][3]=list3
                        
                return



def sendList(ip,port,conn):
                global list1
                msg="Version 1.1"+"\n"+"Status code: Passed"+"\n"+"Connection established successfully"
                #print len(msg)
                conn.send(msg)
                with open('list') as f:
                         list3 = f.read().split("\n")
                         f.close 
                while True:
                        for x in list3:
                                conn.send(x)
                                conn.send(" ")
                        conn.close()                # Close the connection
                        return


def sendFile(ip,port,conn,filename):
        global list1
        file1="rfc"+filename+".pdf"
        #print file1
        if os.path.isfile(file1):
                msg="Version 1.1"+"\n"+"Status code: Passed"+"\n"+"File found "
                #print len(msg)
                conn.send(msg)
                f = open(file1,'rb')
                while True:
                        l = f.read(1024)
                        while (l):
                                conn.send(l)
                                l = f.read(1024)
                        if not l:
                                f.close()
                                conn.close()
                                break

        else:
                msg="Version 1.1"+"\n"+"Status code: Failed"+"\n"+"File NOTfound "
                print len(msg)
                conn.send(msg)
                conn.close()
        return

def counter(timex,j,ServHost,ServPort):
                global list1
                global timez
                if j==1:
                        z=0
                        timez=timex
                else:
                        z=timex-timez
                for x in list1:
                        if x[0]!=ServHost:
                                c=int(x[2])-z
                                x[2]=str(c)
                                


def getallrfclist(ServHost,msg1):
                global list1
                for y in range(0,len(list1)):
                        ip=list1[y][0]
                        port=list1[y][1]
                        port=int(port)
                        if ip == ServHost:
                                with open('list') as f:
                                        list3 = f.read().split("\n")
                                        f.close 
                                list1[y][3]=list3
                                
                        if ip!=ServHost:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                #s.bind((clientHost,clientPort))
                                s.connect((ip,port))
                                s.send(msg1)
                                data1=s.recv(67)
                                print data1
                                data=s.recv(1024)
                                z=shlex.split(data)
                                print z
                                s.close()
                                for y in range(0,len(list1)):
                                        if list1[y][0]==ip:
                                                list1[y][3]=z
                                
                return
        
                

def mainserver(ServHost,ServPort):
        global list1
        
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((ServHost, ServPort))
        while True:
                tcpsock.listen(7)
                #print "Waiting for incoming connections..."
                (conn, (ip,port)) = tcpsock.accept()
                thread14=threading.Thread(target=server, args=(ip,port,conn,))
                thread14.daemon=True
                thread14.start()
        tcpsock.close()
        return

def server(ip,port,conn):
                print 'Got connection from ', (ip,port)
                y=conn.recv(1024)
                print y
                z=shlex.split(y)
                #print z
                if z[0]=="RFCQuery":
                        thread5=threading.Thread(target=sendList, args=(ip,port,conn,))
                        thread5.daemon=True
                        thread5.start()
                if z[0]=="GETRFC":
                        filename=z[1]
                        thread3=threading.Thread(target=sendFile, args=(ip,port,conn,filename,))
                        thread3.daemon=True
                        thread3.start()
        
def menu(ServPort,ServHost):
        global list1
        j=1
        clientHost,clientPort="192.168.0.2",65408
        while (True):

            print "Menu"

            print "0.Register to Server"

            print "1.List all the available RFC's"

            print "2.Server lookup PQUERY"

            print "3.LEAVE "

            print "4.KEEPALIVE"

            print "5.Request for RFC"
            
            print "6 Get active directory"
                
            print "7.Exit"
          
            print "8.Task 1 Centralized"                                     #first register, pquery 
                
            print "9 Task 2 Decentralized worst case"                                 #First register, and pquery
            
            print "10 Task 2 Decentralized Best case"                                 #First register, and pquery
        

            t=datetime.datetime.now().time()
            timex=(t.hour * 60 + t.minute) * 60 + t.second
                                
            counter(timex,j,ServHost,ServPort)
                
            i = raw_input()
            
            Serv=str(ServPort)

            if i=="0":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((clientHost,clientPort))
                s.connect(("192.168.223.148",55567))
                s.send('Register ')
                s.send(Serv)
                data7=s.recv(1024)
                print data7
                s.close()
                j=j+1

            if i=="2":
                s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s1.bind((clientHost,clientPort))
                s1.connect(("192.168.223.148",55567))
                s1.send("PQuery")
                data1=s1.recv(57)
                print data1
                data5=s1.recv(1024)
                z1=shlex.split(data5)
                s1.close()      
                t=0
                list2=[]
                list1=[]
                list7=[]
                while t<len(z1):
                        list2=[z1[t],z1[t+1],z1[t+2],list7]
                        list1.append(list2)
                        t=t+3
                print list1

            if i=="3":
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s2.bind((clientHost,clientPort))
                s2.connect(("192.168.223.148",55567))
                s2.send("Leave")
                data=s2.recv(1024)
                z=shlex.split(data)
                print data
                s2.close()
                
            if i=="4":
                s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s3.bind((clientHost,clientPort))
                s3.connect(("192.168.223.148",55567))
                s3.send("KeepAlive")
                data9=s3.recv(1024)
                print data9
                s3.close()
                
            if i=='1':
                ip,port=raw_input("Enter the Peer Hostname and port(Space Seperated)").split(" ")
                msg1="RFCQuery P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                port=int(port)
                getList(ip,port,ServHost,msg1)

            if i=='5':
                RFC_NO=raw_input("Enter the RFC no ")
                msg="GETRFC "+RFC_NO+" "+"P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                GetRFC(RFC_NO,ServHost,msg)
                
            if i=="6":
                        print list1
            if i=='7':
                return
            
            if i=="8":                                                   #centralized
                ip1="127.0.0.7"
                port1='65407'
                msgn="RFCQuery P2P-DI/1.0"+"\n"+"Host: "+ServHost+"\n"+"OS:"+platform.system()
                port1=int(port1) 
                getList(ip1,port1,ServHost,msgn)
                GetallRFC(ip1,port1,ServHost)

                
            if i=="9":                                  #decentralized
                GetfromallRFC(ServHost)
                
            if i=="10":                                 #decentralized
                bestcase(ServHost)                                              
                
                
        return 
        



def main():
        global list1
        global timez
        timez=0
        list1=[]
        ServHost,ServPort="192.168.0.2",65402
        thread1=threading.Thread(target=mainserver,args=(ServHost,ServPort,))
        thread2=threading.Thread(target=menu,args=(ServPort,ServHost,))
        thread1.daemon=True
        thread1.start()
        thread2.start()
                
        



if __name__=="__main__":

        main()
