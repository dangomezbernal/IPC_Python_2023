import sys,os

print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
    #os.wait()
    print("Programa pare", os.getpid(), pid)
else:
    print("Programa fill", os.getpid(), pid)
    while True:
        pass

print("Hasta luego lucas!")
sys.exit(0)