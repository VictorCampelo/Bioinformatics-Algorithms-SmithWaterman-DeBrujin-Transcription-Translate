# -*- coding: utf-8 -*-
import sys
from fasta import *
#import numpy as np


def deBrujin(data, k, d):
	matrix = []
	for seq in data:
		print(seq)
		vet = seq.split('|')
		matrix.append(vet)
	for i in matrix:
		for j in i:
			print(j)


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
