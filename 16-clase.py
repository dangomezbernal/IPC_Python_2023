import sys, os, signal, argparse

parser = argparse.ArgumentParser(description="Gestionar alarma")
parser.add_argument("segons", type=int, help="segons")
args=parser.parse_args()
print(args)

up=0
down=0

def myusr1(signum, frame):
    print("Signal handler with signal:", signum)
    actual=signal.alarm(0)
    signal.alarm(actual+60)
    up+=1

def myusr2(signum, frame):
    print("Signal handler with signal:", signum)
    actual=signal.alarm(0)
    
    if actual > 60:
        signal.alarm(actual-60)
    else:
        signal.alarm(actual)
    
    down+=1
    

def myalarm(signum, frame):
    print("Signal handler with signal:", signum)
    print("Finalitzant..... up: %d down:%d" % (up, down))

def myterm(signum, frame):
    print("Signal handler with signal:", signum)
    falten=signal.alarm(0)
    signal.alarm(falten)
    print("falten %d segons" % (falten))

def myhup(signum, frame):
    print("Signal handler with signal:", signum)
    signal.alarm(args.segons)
    print("restoring value: %d" % (args.segons))

# assignar un handler al senyal
signal.signal(signal.SIGALRM,myalarm) # 14
signal.signal(signal.SIGUSR2,myusr2) # 12
signal.signal(signal.SIGUSR1,myusr1) # 10
signal.signal(signal.SIGINT,signal.SIG_IGN) # 2
signal.signal(signal.SIGTERM,myterm) # 15
signal.signal(signal.SIGHUP,myhup) # 1

signal.alarm(args.segons)
print(os.getpid())
while True:
    pass
signal.alarm(0)
sys.exit(0)