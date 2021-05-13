import sys
import socket as s

def parse() :
	if len(sys.argv) ==  1 :
		IP = input(">Type the IPV4 of the machine you want to scan\n")
		try:
			s.inet_aton(IP)
		except s.error:
			print("Please use IPV4 adress only")
			sys.exit()
		PORTS = input(">Type the port range you want to scan at format START/END. \n\tAs example : 80/443.\n\tIf you want to scan only one port, please type PORT\n\tAs example 80\n")
		if '/' in PORTS :
			STARPORT = int(PORTS.split('/')[0])
			ENDPORT = int(PORTS.split('/')[1])
		else :
			STARPORT=ENDPORT=PORTS
		try :
			TIMEOUT = int(input(">Enter timeout in ms you want to use\n"))
		except :
			print("Please use int for timeout, need to be between 100 and 1000 ms")
			sys.exit()
		if not 100<=TIMEOUT<=1000 :
			print("Please use int for timeout, need to be between 100 and 1000 ms")
			sys.exit()
		return(IP,STARPORT,ENDPORT,TIMEOUT)
	else :
		if len(sys.argv) > 4 :
			print('Too much arguments, only use the p:PORT/PORT ip:IP t:TIMEOUT (in ms) , nothing else')  
			sys.exit()
		for arg in sys.argv :
			if "p:" in arg :
				if '/' in arg :
					STARPORT = int(arg[2:].split('/')[0])
					ENDPORT = int(arg[2:].split('/')[1])
			if 'ip:' in arg :
				IP = arg[3:]
				try:
					s.inet_aton(IP)
				except s.error:
					print("Please use IPV4 adress only")
					sys.exit()
			if "t:" in arg :
				try  :
					TIMEOUT = int(arg[2:]) 
				except :
					print("Please use int for timeout, need to be between 100 and 1000 ms")
					sys.exit()
				if not 100<=TIMEOUT<=1000 :
					print("Please use int for timeout, need to be between 100 and 1000 ms")
					sys.exit()
		return(IP,STARPORT,ENDPORT,TIMEOUT)

def scanport(ip,port) :
	scanner = s.socket()
	try :
		scanner.connect((ip,port))
		print('[*] Port '+str(port)+' is open')
	except s.error :
		pass

if __name__ == '__main__' :
	IP,STARPORT,ENDPORT,TIMEOUT = parse()
	print("ip : ",IP,"\nstartport : ",STARPORT,"\nendport : ",ENDPORT,"\ntimoeout : ",TIMEOUT)
	s.setdefaulttimeout(TIMEOUT/1000)
	for port in range(STARPORT,ENDPORT) :
		scanport(IP,port)
