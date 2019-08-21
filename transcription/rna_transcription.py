from string import maketrans 

in_FDna = "T"
out_Rna = "U"
transc = maketrans(in_FDna, out_Rna)

str = "GGCCGATTAATGCTTAAATGCGGCCTAAATTAT"
print "Original:    " + str 
print "Transcricao: " + str.translate(transc)