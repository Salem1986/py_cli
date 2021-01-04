#!/usr/bin/env python3


# class that is imported into main and instantiated there; import a class from a module in the same package

import os
from io import StringIO, BytesIO
from datetime import datetime
import pandas as pd
import csv
from dotenv import load_dotenv
#from driver.sftp import Sftp

load_dotenv()

class MyClass:

	def __init__(
		self
		,path
		,sep
		,dec
		,enc
	):
		self.path = path
		self.sep = sep
		self.dec = dec
		self.enc = enc


	def convertXlsxCsv(self):
		print('[] Reading data...', end ="\r")
		try:
			data = pd.read_excel(self.path, header=0, na_values=[""," "],na_filter=True)
			print('[] Writing data...')
			data.to_csv(
				self.path.replace(".xlsx",".csv")
				,sep = self.sep
				,decimal = self.dec
				,quoting = csv.QUOTE_NONNUMERIC
				,quotechar = '"'
				,index = False
				,encoding = self.enc
			)
			print('[ok] Writing data...')
			
		except Exception as ex:
			print('[x] Reading data...')
			print('Error: ' + str(ex))
			raise

	def run(self):
		self.convertXlsxCsv()