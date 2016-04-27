#!/bin/python3
# -*- coding: utf-8 -*-
import os
import csv
import io

def reencode(file):
	for line in file:
		yield line.decode('iso-8859-15').encode('utf-8')

def import_from_csv(path):

	with io.open(path, encoding='iso-8859-15', newline='') as f:
		content = csv.reader(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONE)
		for row in content:
			try:
				print("%s (%s) = %s" % (row[0], row[1], row[2]))
			except IndexError:
				pass

if __name__=="__main__":
	import_from_csv("/home/aurelienroy/dev/2016.02/bv/products/import/test.csv")			