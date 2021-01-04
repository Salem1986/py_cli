#!/usr/bin/env python3

import sys
import argparse
import os
from .classmodule import MyClass

#-----------------------------------------------------------------------------------------------
# Imports

def getBoolean(arg):
	if arg.lower() in ('yes','true','t','y','1'):
		return True
	elif arg.lower() in ('no','false','f','n','0'):
		return False
	else:
		raise argparse.ArgumentTypeError(arg + '? ->Boolean value expected!')
#-----------------------------------------------------------------------------------------------


def main():
	
	#create the parser
	my_parser=argparse.ArgumentParser(description='convert xlsx files to csv by defined citeria')

	my_parser.add_argument(
							'path'
							,type=str
							,help='location of the file(s)'
							#,required = True
	)

	my_parser.add_argument("--csv_separator"
							,type=str
							,default=','
							,help="the character the csv-file is separated by; default is ','"
							#,required = False
	)

	my_parser.add_argument(	"--csv_decimal"
							,type=str
							,default = '.'
							,help ="the decimal separator in the csv-file; default is '.'"
							#,required = False
	)
	
	my_parser.add_argument(	"--csv_encoding"
							,type=str
							,default = 'utf-8'
							,help = "the encoding used to write the csv-file; default is 'UTF-8'"
							#,required = False
	)


	#execute the arg_parse method
	args=my_parser.parse_args()

	my_class = MyClass(
		args.path
		,args.csv_separator
		,args.csv_decimal
		,args.csv_encoding
	)

	run = my_class.run()

	
if __name__== '__main__':
	main()