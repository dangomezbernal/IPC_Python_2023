import sys, os, signal

def myusr1(signum, frame):
        print("Hola radiola")
   

def myusr2(signum, frame):
        print("Adeu andreu")
        sys.exit(0)

print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
    #os.wait()
    print("Programa pare", os.getpid(), pid)
    print("Hasta luego lucas!")
    sys.exit(0)


# programa fill
print("Programa fill", os.getpid(), pid)

signal.signal(signal.SIGUSR2,myusr2) # 12
signal.signal(signal.SIGUSR1,myusr1) # 10

while True:
    pass

