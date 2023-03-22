import sys,os

print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
    
    print("Programa pare", os.getpid(), pid)
    sys.exit(0)


print("Programa fill", os.getpid(), pid)
#os.execv("/usr/bin/ls",["/usr/bin/ls","-la","/","/opt"])  
#os.execl("/usr/bin/ls","/usr/bin/ls","-lh","/opt")
#os.execlp("ls","ls","-lh","/opt")
#os.execvp("uname",["uname","-a"])
#os.execv("/bin/bash",["/bin/bash","show.sh"])
os.execle("/bin/bash","/bin/bash","show.sh",{"nom":"joan","edat":"25"})

print("Hasta luego lucas!")
sys.exit(0) 