# -*- coding: utf-8 -*-
import sys
from fasta import *
#import numpy as np


def deBrujin(data, k, d):
	matrix = []
	v = int(k)-1
	for seq in data:
		vet = seq.split('|')
		matrix.append(vet)
	#two sequences splited and a identifier	
	matrix_splited = []
	for comp in matrix:
		aux = []
		for seq in comp: #2x
			vet1 = []
			vet2 = []
			vet3 = []
			vet1.append(seq[:v]) #abcde -> abcd | bcde
			vet2.append(seq[1:]) #abcde -> abcd | bcde
			vet3.append(vet1)
			vet3.append(vet2)
			aux.append(vet3)
		#[abcd -> abc | bcd] + [abcd -> abc | bcd]
		matrix_splited.append(aux)#[[[[abc],[bcd]],[[abc],[bcd]]], [[[abc],[bcd]],[[abc],[bcd]]]]

	for tup in matrix_splited:
		print(tup)

	sort_list = []
	final = []
	head = 0
	last = 0
	#Remove first
	i = 0
	for t in matrix_splited:#tup = [ [[abc],[bcd]] , [[abc],[bcd]] ]
		flag = 0 
		for t2 in matrix_splited:#seach to head of list
			if (t[0][0] == t2[0][1] and t[1][0] == t2[1][1]):
				flag = 1
				break
		if flag == 0:
			head = i
			break
		i+=1			
	sort_list.append(matrix_splited[head])
	matrix_splited.remove(matrix_splited[head])			
	#remove last
	i = 0
	for t in matrix_splited:#tup = [ [[abc],[bcd]] , [[abc],[bcd]] ]
		flag = 0
		for t2 in matrix_splited:#seach to head of list
			if (t[0][1] == t2[0][0] and t[1][1] == t2[1][0]):
				flag = 1
				break
		if flag == 0:
			last = i
			break
		i+=1					
	final.append(matrix_splited[last])
	matrix_splited.remove(matrix_splited[last])	

	n = 0
	i = 0
	print(sort_list)
	while (len(matrix_splited) >= n):
		vet = []
		vet = sort_list[n]
		print(vet[0][1])
		print(vet[1][1])
		for tup in matrix_splited:
			if  (vet[0][1] == tup[0][0] and vet[1][1] == tup[1][0]):
				print(tup[0][0])
				print(tup[1][0])
				print(tup)
				sort_list.append(tup)
				break
		n+=1
	print(final)
	sort_list.append(final[0])
	seq_list = []		
	for tup in sort_list:
		aux = []
		aux.append(tup[0][0])
		aux.append(tup[1][0])
		print(aux)
		seq_list.append(aux)
	aux = []	
	aux.append(sort_list[-1][0][1])
	aux.append(sort_list[-1][1][1])
	seq_list.append(aux)
	print("aquiiii")
	mount_list = []
	i = 0
	for seq in seq_list:
		print(seq)
		if i+1 == len(seq_list):
			break
		aux = []
		obj = seq_list[i+1]
		aux.append(seq[0][0]+obj[0][0][-1])
		aux.append(seq[1][0]+obj[1][0][-1])
		mount_list.append(aux)	
		i+=1

	result = ""
	for seq in mount_list:
		result += seq[0][0]
	result += mount_list[-1][0][1:]
	aux = ""
	for i in range(len(mount_list)-1,len(mount_list)-int(d), -1):
		aux += mount_list[i][1][0]
	result += aux[::-1]
	result += mount_list[-1][1]
	print(result)		

def main():
	s1 = ""
	s2 = ""
	if sys.version_info.major == 2:
		fasta = raw_input("Digite o nome do arquivo (inclua .fasta):  ")
	elif sys.version_info.major == 3:
		fasta = input("Digite o nome do arquivo (inclua .fasta): ")

	fst = Fasta_r()	

	while fst.setFile(fasta) == False:
		if sys.version_info.major == 2:
			fasta = raw_input("Digite o nome do arquivo (inclua .fasta): ")
		elif sys.version_info.major == 3:
			fasta = input("Digite o nome do arquivo (inclua .fasta): ")

	deBrujin(fst.getData(), fst.getK(), fst.getD())		

main()
