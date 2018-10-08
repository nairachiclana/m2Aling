

def readAndWriteFun(filename, delimiter):

    #Create output files
    f_strike_value = open("Best_strike_value.txt", "w")
    f_tc_value = open("Best_tc_value.txt", "w")
    f_sp_value = open("Best_sp_value.txt", "w")

    f_strike_median = open("Median_strike_value.txt", "w")
    f_tc_median = open("Median_tc_value.txt", "w")
    f_sp_median = open("Median_sp_value.txt", "w")

    col_strike = []
    col_tc = []
    col_sp = []

    #open input file
    lines = open(filename, "r").readlines()
    number_rows = len(lines)

    #Save each colum in a list
    for row in range(0, number_rows):
        col_strike.append((lines[row].split(delimiter)[0]))
        col_tc.append((lines[row].split(delimiter)[1]))
        col_sp.append((lines[row].split(delimiter)[2]))


    # maximun value of each colum
    max_strike = max(col_strike)
    print("max strike", max_strike)
    max_tc = max(col_tc)
    print("max tc", max_tc)
    max_sp = max(col_sp)
    print("max sp", max_sp)


   #Parse string elements of cols to compute means
    strk=0
    for s in col_strike:
        strk=strk+float(s)
    strike_mean=strk/len(col_strike)

    tc=0
    for t in col_tc:
        tc=tc+float(t)
    tc_mean=tc/len(col_tc)

    sp=0
    for s in col_sp:
        sp=sp+float(s)
    sp_mean=sp/len(col_sp)

    #mediana
    col_strike_sorted = sorted(col_strike)
    col_tc_sorted = sorted(col_tc)
    col_sp_sorted = sorted(col_sp)


    #if number rows is even, the median is only the number in N/2
    #no take into account if it's even or odd
    mediana_strike = col_strike_sorted[number_rows//2]
    mediana_tc = col_tc_sorted[number_rows//2]
    mediana_sp = col_sp_sorted[number_rows//2]





    # index of each maximum value
    index_max_strike = col_strike.index(max(col_strike))
    index_max_tc = max_tc.index(max(col_tc))
    index_max_sp = col_sp.index(max(col_sp))

    #idex of each median value
    index_median_strike = col_strike.index(mediana_strike)
    index_median_tc = col_tc.index(mediana_tc)
    index_median_sp = col_sp.index(mediana_sp)


    # write in output files entire row of where maximun value belongs and means and close them
    row_max_strike = lines[index_max_strike].split(delimiter)
    f_strike_value.write(str(row_max_strike)+ "\n" + "strike mean: " + str(strike_mean))
    f_strike_value.close()

    row_max_tc = lines[index_max_tc].split(delimiter)
    f_tc_value.write(str(row_max_tc)+ "\n"+  "tc mean: " + str(tc_mean))
    f_tc_value.close()

    row_max_sp = lines[index_max_sp].split(delimiter)
    f_sp_value.write(str(row_max_sp)+ "\n" + "sp mean: " +  str(sp_mean))
    f_sp_value.close()

    f_strike_median.write(str(mediana_strike))
    f_strike_median.close()
    f_sp_median.write(str(mediana_sp))
    f_sp_median.close()
    f_tc_median.write(str(mediana_tc))
    f_tc_median.close()




    return (index_max_strike, index_max_tc, index_max_sp, index_median_strike, index_median_sp, index_median_tc)



def readAndWriteVAR(filename, delimiter):

    #Create output files
    f_strike_seq = open("Best_strike_seq.txt", "w")
    f_tc_seq = open("Best_tc_seq.txt", "w")
    f_sp_seq = open("Best_sp_seq.txt", "w")

    f_median_strike_seq = open("Median_strike_seq.txt", "w")
    f_median_tc_seq = open("Median_tc_seq.txt", "w")
    f_median_sp_seq = open("Median_sp_seq.txt", "w")

    #open input file
    lines = open(filename, "r").readlines()
    number_rows = len(lines)


    lineas = [] #entire file
    group = ""  # each group in a string
    groups = [] #all groups (each one in a string)


    #save all rows of the input file in the list lineas
    for row in range(0, number_rows):
        lineas.append(lines[row].split(delimiter))

    #save each group(10 rows) in a string and append to list groups
    for row in range(0, len(lineas)):
        if not row%10:
            for cont in range(row, row+10):
                group = group + "\n" + str(lineas[cont])
            groups.append(group)
            group = ""

    posiciones_maximos_medianas = readAndWriteFun("FUN.BB11001.tsv", "\t")

   #Write output files with sequences with the same indexes that maximums and close them
    group_max_strike = groups[posiciones_maximos_medianas[0]]
    f_strike_seq.write("MÁXIMO: \n")
    f_strike_seq.write(group_max_strike)
    f_strike_seq.close()

    group_max_tc = groups[posiciones_maximos_medianas[1]]
    f_tc_seq.write("MÁXIMO: \n")
    f_tc_seq.write(group_max_tc)
    f_tc_seq.close()

    group_max_sp = groups[posiciones_maximos_medianas[2]]
    f_sp_seq.write("MÁXIMO: \n")
    f_sp_seq.write(group_max_sp)
    f_sp_seq.close()

    #seqs of median
    group_median_strike = groups[posiciones_maximos_medianas[3]]
    f_median_strike_seq.write("MEDIANA: \n")
    f_median_strike_seq.write(group_median_strike)
    f_median_strike_seq.close()

    group_median_tc = groups[posiciones_maximos_medianas[4]]
    f_median_tc_seq.write("MEDIANA: \n")
    f_median_tc_seq.write(group_median_tc)
    f_median_tc_seq.close()

    group_median_sp = groups[posiciones_maximos_medianas[5]]
    f_median_sp_seq.write("MEDIANA: \n")
    f_median_sp_seq.write(group_median_sp)
    f_median_sp_seq.close()





class secMejorValor(object):

    def __init__(self):
        pass

    def makeFilesValues(self, fileFun,delim):
        return readAndWriteFun(fileFun, delim)

    def makeFilesSeq(self, fileVar, delim):
        return  readAndWriteVAR(fileVar, delim)


#Execute functions
files = secMejorValor()
files.makeFilesValues("FUN.BB11001.tsv", "\t")
files.makeFilesSeq("VAR.BB11001.tsv", "\n")


