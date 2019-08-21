from string import maketrans 

str_in = open('input.txt', 'r').readline()
str_out = open('output.txt', 'w')
in_FDna = "T"
out_Rna = "U"
transc = maketrans(in_FDna, out_Rna)

#print "Original:    " + str 
#print "Transcricao: " + str.translate(transc)
str_out.write(str_in.translate(transc))
