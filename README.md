# m2Align python

### secMejorValor 

I have obtained the files *FUN.BB11001* and *VAR.BB11001* by running the class *M2AlignBALIBASERunner*.

The python file *secMejorValor* contains two methods:

* *readAndWriteFun* which saves each colum of the values *strike, tcp* and *sp* and computes the maximum and mean for the three ones.
	This method also writes 3 files (*Best_vble_value*) where it writes the entire row for the maximum of every variable and the mean.
	returns the position where the maximum of each variable is located in the file *FUN.BB1101*
	
* *readAndWriteVAR* writes 3 files too, (*Best_vble_seq*). Each file contains the group of 4 identifiers and their respective aligned sequences.
	The group is the one with the same index in *FUN.BB1101* that the maximum had (obtained by the previous method).
	
### secMejorValorTest

Contains several unit test verifying inputs, delimiters, some specific values of the value files, and the means.