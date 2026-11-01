#Create a resolve() function that performs hostname, local IP,
#  forward DNS, extended DNS and reverse DNS lookups. 
# Catch socket.error inside the function. 
# Start two threads and join both.


import threading, socket

def resolve():
    try:
        host = socket.gethostname()
        print("Hostname: " , host)

        ip= socket.gethostbyname(host)
        print("IP address: " , ip)

        dns = socket.gethostbyname('www.example.com')
        print("DNS address: " , dns)

        ex_dns = socket.gethostbyname_ex('www.example.com')
        print("Extended DNS address: " , ex_dns)

        reverse_dns = socket.gethostbyaddr('1.1.1.1')
        print("Reverse DNS address: " , reverse_dns)

    except socket.error as err:
        print("Socket error: ", err)

t1 = threading.Thread(target=resolve)
t2 = threading.Thread(target=resolve)

t1.start()
t2.start()

t1.join()
t2.join()