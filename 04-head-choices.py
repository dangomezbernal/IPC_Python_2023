# /usr/bin/python
# *-coding: utf-8-*-
#
# head [-n 5|10|15]] [-f file]
# 10 lines, file o stdin
# ----------------------------------------
# @ edt ASIX M06 Curs 2022-2023
# Gener 2022

#---------------------------
import argparse
parser= argparse.ArgumentParser(description="programa exemple arguments",\
				prog="02-arguments.py",\
				epilog="hasta luego lucas")
parser.add_argument("-n","--nlin", type=int, dest="nlin", help="numero de lineas", metavar="[5|10|15]", default=10, choices=[5,10,15])

parser.add_argument("-f","--file", type=str, dest="file", metavar="file")
args=parser.parse_args()

#--------------------------

MAXLIN=args.nlin
fileIn=open(args.file,"r")
counter=0
for line in fileIn:
    counter+=1
    print(line, end="")
    if counter==MAXLIN: break
fileIn.close()
exit(0)

