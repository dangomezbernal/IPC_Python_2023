# /usr/bin/python
# *-coding: utf-8-*-
#
# head [file]
# 10 lines, file o stdin
# ----------------------------------------
# @ edt ASIX M06 Curs 2022-2023
# Gener 2022
#---------------------------
import argparse
parser= argparse.ArgumentParser(description="programa exemple arguments",\
				prog="02-arguments.py",\
				epilog="hasta luego lucas")
parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar", metavar="edat")

parser.add_argument("-n","--nom", type=str)
args=parser.parse_args()
print(args)
print(args.useredat, args.nom)
