There are 6 files for each client. 
Run clients in different folders or machines. 
If running on different machines change the IP address in all client files.

ServHost,ServPort="127.0.0.3",65403
clientHost,clientPort="127.0.0.3",65409

keep the ServHost and clientHost ip same.

each client should have a file "list" in the same folder, which contains the list of locally RFCs stored.
the file should have just the rfc number, one on one line
The rfcs should be titled as "rfc3215.pdf" for example and stored in the same folder.

Suppose two RFCs are present with c1. RFC "rfc3216.pdf" and "rfc3215.pdf"
In this case the "list" file will have only two entry 
3216
3215

Run the RS server as: python rsserver.py 
Run the clients as: python <clientname>.py
for eg. python c1.py

Tested in Linux machines.