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
	for x in range(0,tam__s2+2,1):
		tmp = []
		for y in range(0,tam__s1+2,1):
			tmp.append(0)
		matriz.append(tmp[:])

	backtrack = []
	l__Max = 0
	c__Max = 0
	match = 2
	misMatch = -1
	gap = -1
	best = 0
	#1 = diagonal, 2 = topo, 3 = esquerda
	for x in range(1,tam__s2+1,1):
		tmp = []
		for y in range(1,tam__s1+1,1):
			values = []
			#diagonal
			if (s1[y-1] == s2[x-1]):
				values.append(matriz[x-1][y-1]+match)
			else:
				values.append(matriz[x-1][y-1]+misMatch)
			#topo
			values.append(matriz[x-1][y]+gap)
			#esqueda
			values.append(matriz[x][y-1]+gap)
			#max
			t = [0, values[0], values[1], values[2]]
			matriz[x][y] = max(t)
			tmp.append(t.index(max(t)))
		backtrack.append(tmp[:])

	new__s1 = ""
	new__s2 = ""
	x = len(s2)-1
	y = len(s1)-1
	while (x >= 0 and y >= 0):
		idx = backtrack[x][y]
		#print(idx)
		print("x: "+str(x))
		print("y: "+str(y))
		#seta diagonal s1 = s2
		if(idx == 1):
			new__s1 += s1[y]
			new__s2 += s2[x]
			x = x-1
			y = y-1
		#seta topo
		elif(idx == 2):
			new__s1 += "_"
			new__s2 += s2[x]
			x = x-1
		#seta esquerda
		elif(idx == 3):
			new__s1 += s1[y]
			new__s2 += "_"
			y = y-1
		else:
			break	

	for i in range(x+1,0,-1):
		new__s1 += "_"
		new__s2 += s2[i]
	for i in range(y+1,0,-1):
		new__s2 += "_"
		new__s1 += s1[i]	

	print(new__s1[::-1])
	print(new__s2[::-1])
	#write in file
	f= open("out_sw.txt","w+")
	f.write(new__s1[::-1])
	f.write("\n")
	f.write(new__s2[::-1])
	
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
	for x in range(0,2,1):
		if sys.version_info.major == 2:
			name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
		elif sys.version_info.major == 3:
			name = input("Digite o nome do arquivo com a sua extenção (.txt): ")
		seq[x] = read_file(name)	
		while seq[x] == "":
			if sys.version_info.major == 2:
				name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
			elif sys.version_info.major == 3:
				name = input("Digite o nome do arquivo com a sua extenção (.txt): ")
			seq[x] = read_file(name)
	smithWaterman(seq[0], seq[1])
main()
