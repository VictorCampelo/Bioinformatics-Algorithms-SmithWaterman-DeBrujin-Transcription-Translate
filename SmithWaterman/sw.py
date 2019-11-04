# -*- coding: utf-8 -*-
import sys
#import numpy as np

def smithWaterman(s1,s2):
	score = 0	
	backtrack = []
	l__Max = 0
	c__Max = 0
	gap = input("Digite o valor do GAP: ")
	misMatch = input("Digite o Valor do MISMATCH: ")	
	match = input("Digite o valor do MATCH")
	best = 0
	print(s1)
	print(s2)
	tam__s1 = len(s1)
	tam__s2 = len(s2)
	print(tam__s1)
	print(tam__s2)

	cols, rows = len(s1) + 1, len(s2) + 1

	# matriz = []
	# for x in range(0,tam__s2+2,1):
	# 	tmp = []
	# 	for y in range(0,tam__s1+2,1):
	# 		tmp.append(0)
	# 	matriz.append(tmp[:])

	matriz = [[0 for x in range(cols)] for x in range(rows)]

	matriz[0][0] = 0
	for i in range(1, cols):
		matriz[0][i] = matriz[0][i-1] + gap
	for i in range(1, rows):
		matriz[i][0] = matriz[i-1][0] + gap

	#1 = diagonal, 2 = topo, 3 = esquerda
	for x in range(1,tam__s2+1,1):
		tmp = []
		for y in range(1,tam__s1+1,1):
			values = []
			#diagonal
			#print(s1[y-1])
			#print(s2[x-1])
			if (s1[y-1] == s2[x-1]):
				values.append(matriz[x-1][y-1]+match)
			else:
				values.append(matriz[x-1][y-1]+misMatch)
			#topo
			values.append(matriz[x-1][y]+gap)
			#esqueda
			values.append(matriz[x][y-1]+gap)
			#max
			n = 0
			#values.append(0)
			if values[0] >= values[1] and values[0] >= values[2]:
				n = matriz[x][y] = values[0]
				t = 0
			elif values[1] >= values[0] and values[1] >= values[2]:
				n = matriz[x][y] = values[1]
				t = 1
			else:
				n = matriz[x][y] = values[2]
				t = 2		

			#t = [values[0], values[1], values[2]]
			#print("Lista: "+str(values))
			#print("max: "+str(t))
			score = n
			tmp.append(t)
		backtrack.append(tmp[:])

	print(backtrack)	
	print("\n")
	print(matriz)	

	new__s1 = ""
	new__s2 = ""
	x = len(s2)-1
	y = len(s1)-1
	print(x)		
	print(y)	
	while (x >= 0 and y >= 0):
		idx = backtrack[x][y]
		#print(idx)
		print("x: "+str(x))
		print("y: "+str(y))
		#seta diagonal s1 = s2
		if(idx == 0):
			new__s1 += s1[y]
			new__s2 += s2[x]
			# print(new__s1)
			# print(new__s2)
			x = x-1
			y = y-1
		#seta topo
		elif(idx == 1):
			new__s1 += "_"
			new__s2 += s2[x]
			# print(new__s1)
			# print(new__s2)
			x = x-1
		#seta esquerda
		elif(idx == 2):
			new__s1 += s1[y]
			new__s2 += "_"
			# print(new__s1)
			# print(new__s2)
			y = y-1
		print(new__s1)
		print(new__s2)	

	print(x)		
	print(y)

	if y == -1:	
		for i in range(x,-1,-1):
			new__s1 += "_"
			new__s2 += s2[i]
	elif x == -1:		
		for i in range(y,-1,-1):
			new__s2 += "_"
			new__s1 += s1[i]		
	# if x > y: #s2 > s1
	# 	print("aqui")
	# 	dif = x - y
	# 	print(x)
	# 	print(y)
	# 	for i in range(x,-1,-1):
	# 		if s2[i] == s1[i-dif]:
	# 			new__s2 += s2[i]
	# 			new__s1 += s1[i-dif]
	# 			continue
	# 		new__s1 += "_"
	# 		new__s2 += s2[i]
	# else:		
	# 	print("aqui 2")
	# 	dif = y - x
	# 	print(x)
	# 	print(y)
	# 	for i in range(y,-1,-1):
	# 		if s2[i-dif] == s1[i]:
	# 			new__s2 += s2[i-dif]
	# 			new__s1 += s1[i]
	# 			continue
	# 		new__s2 += "_"
	# 		new__s1 += s1[i]	

	print(new__s1[::-1])
	print(new__s2[::-1])
	print("Score: "+str(score))
	#write in file
	f= open("out_sw.txt","w+")
	f.write(new__s1[::-1])
	f.write("\n")
	f.write(new__s2[::-1])
	f.write("\n")
	f.write("Score: "+str(score))

def read_fasta(arquivo):
	s1 = ''
	s2 = ''
	aux = []
	w_seq = 0
	try:
		with open(arquivo, 'r') as fasta:
			for line in fasta:
				if line.startswith('>'):
					w_seq += 1
					continue
				if w_seq == 1:
					s1 += line
				elif w_seq == 2:
					s2 += line
			s1 = s1.replace("\n", "")
			s1 = s1.replace("\r", "")
			s1 = s1.replace(".", "")
			s2 = s2.replace("\n", "")
			s2 = s2.replace("\r", "")
			s2 = s2.replace(".", "")
			smithWaterman(s1, s2)
	except IOError as fnf_error:
		print(fnf_error)
		print("\n")
		return False
	return True

def main():
	s1 = ""
	s2 = ""
	if sys.version_info.major == 2:
		fasta = raw_input("Digite o nome do arquivo (inclua .fasta):  ")
	elif sys.version_info.major == 3:
		fasta = input("Digite o nome do arquivo (inclua .fasta): ")

	while read_fasta(fasta) == False:
		if sys.version_info.major == 2:
			fasta = raw_input("Digite o nome do arquivo (inclua .fasta): ")
		elif sys.version_info.major == 3:
			fasta = input("Digite o nome do arquivo (inclua .fasta): ")

main()
