import sys, os, signal

def myhandler(signum, frame):
    print("Signal handler with signal:", signum)
    print("hasta luego lucas!")
    sys.exit(1)

def myhandler2(signum, frame):
    print("Signal handler with signal:", signum)
    print("Buenos dias")

# assignar un handler al senyal
signal.signal(signal.SIGALRM,myhandler) # 14
signal.signal(signal.SIGUSR2,myhandler) # 12
signal.signal(signal.SIGUSR1,myhandler2) # 10
signal.signal(signal.SIGINT,signal.SIG_IGN) # 2
signal.signal(signal.SIGTERM,signal.SIG_IGN) # 15


signal.alarm(60)
print(os.getpid())
while True:
    pass
signal.alarm(0)
sys.exit(0)