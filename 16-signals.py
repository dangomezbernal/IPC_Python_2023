import sys, os, signal, argparse

# establir argument dels segons amb el que comença l'alarma
parser = argparse.ArgumentParser(description ="""Exemple signals""")
parser.add_argument("seconds",type=int,help="segons de a establir per a l'alarma")
args=parser.parse_args()


upper=0
down=0

# sigusr1 --> +60 segons
def increment(signum, frame):
    
    global upper
    upper += 1

    actual = signal.alarm(0)
    signal.alarm(actual+60)

# sigusr2 --> -60 segons (si queden >60)
def minva(signum, frame):
    
    global down
    actual = signal.alarm(0)
    
    if actual > 60:
        down+=1
        signal.alarm(actual-60)
    
    else:
        print("No pots reduir l'alarma, queden menys de 60 segons!!!")
        signal.alarm(actual)

# sigterm --> no plega, mostra cuants segons queden
def restants(signum, frame):
    
    actual = signal.alarm(0)
    print("Queden",actual,"segons.")
    signal.alarm(actual)

# sighup --> reinicia argument
def reset(signum, frame):
    
    signal.alarm(args.seconds)

# sigalarm --> quants upp, quants down, acaba

def recompte(signum, frame):
    global upper, down

    print("Has fet",upper,"upper")
    print("Has fet",down,"down")
    print("Finalitzant alarma...")

    sys.exit(0)
    

  

# assignar un handler al senyal
signal.signal(signal.SIGUSR1,increment) # 10
signal.signal(signal.SIGUSR2,minva) # 12
signal.signal(signal.SIGTERM,restants) # 15
signal.signal(signal.SIGHUP,reset) # 1
signal.signal(signal.SIGINT,signal.SIG_IGN) # 2
signal.signal(signal.SIGALRM,recompte) # 14


######
signal.alarm(args.seconds)
print(os.getpid())
while True:
    pass
signal.alarm(0)
sys.exit(0)


# 16.py nsegons
# sigusr1 --> +60 segons
# sigusr2 --> -60 segons (si queden >60)
# sighup --> reinicia argument
# sigterm --> no plega, mostra cuants segons queden
# sigalarm --> quants upp, quants down, acaba
