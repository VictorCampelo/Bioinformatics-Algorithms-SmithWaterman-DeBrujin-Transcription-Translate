# -*- coding: utf-8 -*-
import sys
#import numpy as np

def smithWaterman(s1,s2):
	print(s1)
	print(s2)
	tam__s1 = len(s1)
	tam__s2 = len(s2)
	print(tam__s1)
	print(tam__s2)

	#preencher a matriz com zeros
	matriz = []
	for x in xrange(0,tam__s2+1):
		tmp = []
		for y in xrange(0,tam__s1+1):
			tmp.append(0)
		matriz.append(tmp[:])
	#matriz 0 0 0
	#		0 0 0
	#		0 0 0
	#print(matriz)
	backtrack = []
	l__Max = 0
	c__Max = 0
	match = 1
	misMatch = -1
	gap = -1
	best = 0
	for x in xrange(1,tam__s2):
		tmp = []
		for y in xrange(1,tam__s1):
			values = []
			
			#diagonal
			if (s1[y-1] == s2[x-1]):
				values[0] = matriz[x-1][y-1]+match
			else:
				values[0] = matriz[x-1][y-1]+misMatch
			#topo
			values[1] = matriz[x-1][y]+gap
			#esqueda
			values[2] = matriz[x][y-1]+gap
			#max
			t = (0, values[0], values[1], values[2])
			matriz[x][y] = max(t)
			tmp.append(t)
			if(matriz[x][y] >= best):
				best = matriz[x][y]
				l__Max = x+1
				c__Max = y+1
		backtrack.append(tmp[:])
def read_file(name):
	try:
	    with open(name, "r") as file:
	    	seq = file.read()
	except IOError as fnf_error:
		print(fnf_error)
		print("\n")
		return ""

	seq = seq.replace("\n", "")  
	seq = seq.replace("\r", "")
	seq = seq.replace(".", "")
	#print("\nmRna: " + seq)
	#print("\n")
	return seq

def main():
	seq = ["",""]
	for x in xrange(1,2):
		if sys.version_info.major == 2:
			name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
		elif sys.version_info.major == 3:
			name = input("Digite o nome do arquivo com a sua extenção (.txt): ")
		seq[x] = read_file(name)	
		while seq[x-1] == "":
			if sys.version_info.major == 2:
				name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
			elif sys.version_info.major == 3:
				name = input("Digite o nome do arquivo com a sua extenção (.txt): ")
			seq[x-1] = read_file(name)
	smithWaterman(seq[0], seq[1])
main()
