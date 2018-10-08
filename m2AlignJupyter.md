
# Alineamiento múltiple de secuencias 

Naira María Chiclana García 


### secMejorValor.py

#### readAndWriteFun


Crearé una función para cada fichero generado por *M2AlignBALIBASERunner.* 
La primera de ellas, para el archivo *FUN* *readAndWriteFun* recibirá como parámetros  el nombre del archivo a analizar y su correspondiente delimitador por el que separará las lineas.

Primero, creo los archivos en formato escritura *w* y los guardo en variables.


```python
f_strike_value = open("Best_strike_value.txt", "w")
f_tc_value = open("Best_tc_value.txt", "w")
f_sp_value = open("Best_sp_value.txt", "w")

f_strike_median = open("Median_strike_value.txt", "w")
f_tc_median = open("Median_tc_value.txt", "w")
f_sp_median = open("Median_sp_value.txt", "w")

```

Leo y guardo laslineas del archivo de entrada, en este caso *"FUN.BB11001.tsv"*:


```python
lines = open("FUN.BB11001.tsv", "r").readlines()
number_rows = len(lines)
```

Este archivo tienes 3 columnas, una para cada variable: *strike*, *tc*, *sp*. Creo una lista para almacenar cada una de las columnas:


```python
col_strike = []
col_tc = []
col_sp = []
```


```python
for row in range(0, number_rows):
    col_strike.append((lines[row].split("\t")[0]))
    col_tc.append((lines[row].split("\t")[1]))
    col_sp.append((lines[row].split("\t")[2]))
```

Teniendo cada variable en una lista, puedo facilmente calcular el máximo usando la función `max` definida para las listas:


```python
max_strike = max(col_strike)
max_tc = max(col_tc)
max_sp = max(col_sp)
```

Para calcular la **media**, será necesario parsear cada elemento a *float*, ya que están guardados como *string*. Para ello recorro las columnas creadas sumando cada valor y dividiendolo por el total:


```python
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
```

Calculo de **medianas**, tomaremos la mediana como el valor que se encuentre en la posición $\frac{N}{2}$, sin diferenciar entre $N$ par o impar. Para ello, primero ordenaderemos las columnas de cada valor de menor a mayor y después cogeremos el valor en la posición $\frac{N}{2}$ de la lista ordenada.

```python
col_strike_sorted = sorted(col_strike)
col_tc_sorted = sorted(col_tc)
col_sp_sorted = sorted(col_sp)

```

Para sacar el **índice** en el cual se encontraban cada uno de los valores **máximos** también usaré la función definida para listas en python `lista.index(valor)`


```python
index_max_strike = col_strike.index(max(col_strike))
index_max_tc = max_tc.index(max(col_tc))
index_max_sp = col_sp.index(max(col_sp))

index_median_strike = col_strike.index(mediana_strike)
index_median_tc = col_tc.index(mediana_tc)
index_median_sp = col_sp.index(mediana_sp)
```

Ahora quiero escribir en cada archivo *Best_vble_value* la fila con los 3 valores correspondiente al máximo de cada variable, además de las medias. Para ello, accedo a la variable anteriormente creada *lines* que contiene todas las lineas, y accedo a la posición que acabo de calcular *index_max_vble* indicandole que el separador es un espacio, y cierro los ficheros al acabar.


```python
row_max_strike = lines[index_max_strike].split("\t")
f_strike_value.write(str(row_max_strike)+ "\n" + "strike mean: " + str(strike_mean))
f_strike_value.close()

row_max_tc = lines[index_max_tc].split("\t")
f_tc_value.write(str(row_max_tc)+ "\n"+  "tc mean: " + str(tc_mean))
f_tc_value.close()

row_max_sp = lines[index_max_sp].split("\t")
f_sp_value.write(str(row_max_sp)+ "\n" + "sp mean: " +  str(sp_mean))
f_sp_value.close()
```

Para escribirlos en el fichero de salida los transformo a *string* previamente usando la función `str()`


Archivos $Median_vble_value$ de la misma manera:

```python
f_strike_median.write(str(mediana_strike))
f_strike_median.close()
f_sp_median.write(str(mediana_sp))
f_sp_median.close()
f_tc_median.write(str(mediana_tc))
f_tc_median.close()
```

Devuelvo los indices ya que serán necesarios para el objetivo de la siguiente función


*return(index_max_strike, index_max_tc, index_max_sp, index_median_strike, index_median_sp, index_median_tc)*

#### readAndWriteVAR

Esta función también escribirá 3 ficheros de salida (*Best_vble_seq*). Estos ficheros contendrán el grupo de 4 secuencias alineadas pertenecientes a *VAR.BB11001* que se encuentren en la posición en la que estaba en máximo de cada variable devuelto por la función anterior.


Al igual que antes, empezamos creando los ficheros en formato escritura en los que guardaremos las secuencias:



```python
f_strike_seq = open("Best_strike_seq.txt", "w")
f_tc_seq = open("Best_tc_seq.txt", "w")
f_sp_seq = open("Best_sp_seq.txt", "w")
```

También lo abrimos en formato lectura *"r"* de la misma manera que antes y almacenamos el lineas.


```python
lines = open("VAR.BB11001.tsv", "r").readlines()
number_rows = len(lines)
```

El objetivo es crear una lista *groups* que en cada posición contenga un grupo de con 4 secuencias, de esta manera, con la posición anterior podremos acceder al grupo directamente.
Para ello, primero guardaré todo el archivo separado en lineas independientes en la lista *lineas*, y después, sabiendo que cada uno de los grupos tiene 10 lineas, guardare en *group* un *string* que contenga a cada grupo y añadiré a *groups*. Sabiendo que cada grupo tiene 10 lineas empezará esta cuenta cada vez que llegue a una fila divisible por 10 (siendo group1 lineas 0-10, grupo 2 10-20,....).


Empiezo creando las variables mencionadas:


```python
lineas = [] #entire file
group = ""  # each group in a string
groups = [] #all groups (each one in a string)
```

Guardo en *lineas* cada linea del fichero, para poder acceder a llas por posiciones con el objetivo mencionado anteriormente:


```python
for row in range(0, number_rows):
    lineas.append(lines[row].split("\n"))
    
```

Ahora reccorro todas las lineas y guardo en *groups* un string conteniendo cada grupo de 10 lineas(4 secuencias):


```python
for row in range(0, len(lineas)):
    if not row%10:
        for cont in range(row, row+10):
            group = group + "\n" + str(lineas[cont])
        groups.append(group)
        group = ""
```

* Como vemos, *group* solo es una variable temporal que se reinicia después de añadir cada group a *groups*

LLamo a la función anterior que además de darme los máximos, me devolverá sus indices, guardándolos en *posiciones_maximos*. 


```python
posiciones_maximos_medianas = readAndWriteFun("FUN.BB11001.tsv", "\t")
```

    max strike 3.021251039770574
    max tc 5.825242718446602
    max sp 91.75531914893618


Accederé con estos indices a esa misma posición en la lista *groups* que acabo de crear, y será ese el string que escribiré en los ficheros de salida.


```python
group_max_strike = groups[posiciones_maximos_medianas[0]]
f_strike_seq.write(group_max_strike)
f_strike_seq.close()

group_max_tc = groups[posiciones_maximos_medianas[1]]
f_tc_seq.write(group_max_tc)
f_tc_seq.close()

group_max_sp = groups[posiciones_maximos_medianas[2]]
f_sp_seq.write(group_max_sp)
f_sp_seq.close()
```

También escribiré las secuencias que se encuentren en la posición de las medianas en los archivos $Median_vble_seq$:

```python
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

```

Después de crear las dos funciones por separádo, crearé una clase que las llamará.


```python
class secMejorValor(object):

    def __init__(self):
        pass

    def makeFilesValues(self, fileFun,delim):
        return readAndWriteFun(fileFun, delim)

    def makeFilesSeq(self, fileVar, delim):
        return  readAndWriteVAR(fileVar, delim)
```

### Test unitarios:

Creo un método `setUp` que se ejecutará por defecto antes de los test en el que se creará un objeto *files* de la clase, y desde este se podrá llamar a los métodos:


```python
def setUp(self):
    self.files = secMejorValor()
    self.files.makeFilesValues("FUN.BB11001.tsv", "\t")
    self.files.makeFilesSeq("VAR.BB11001.tsv", "\n")
```

Crearé test para:

* Ver errores si los inputFiles no son correctos:


```python
    def test_should_WrongInputFile_in_Fun_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesValues("nombreErroneo", "\t")

    def test_should_WrongInputFile_in_Val_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesSeq("nombreErroneo2", "\n")
```

* Ver errores si los delimitadores no son correctos:


```python
    def test_should_WrongDelimiter_in_Fun_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesValues("FUN.BB11001.tsv", "!")

    def test_should_WrongDelimiter_in_Val_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesSeq("VAR.BB11001.tsv", "*")
```

* Comprobar si los inicios de los archivos que guardan la secuencia son correctos (todos deben empezar por *>1aab_*


```python
    def test_should_first_item_of_strik_seq_be_1aab(self):
        strike_seq = open("Best_strike_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", strike_seq[1])

    def test_should_first_item_of_sp_seq_be_1aab(self):
        sp_seq = open("Best_sp_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", sp_seq[1])

    def test_should_first_item_of_tc_seq_be_1aab(self):
        tc_seq = open("Best_tc_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", tc_seq[1])
```

* Comprobar algunos valores específicos de cada archivo *value* aver si son correctos:



```python
    def test_should_strike_value_of_sp_max_be_199(self):
        sp_seq = open("Best_sp_value.txt", "r").readlines()
        sp_seq_separado = sp_seq[0].split(",")
        self.assertEqual("['1.9975781240868502'", sp_seq_separado[0])

    def test_should_sp_value_of_tc_max_be_837(self):
        sp_tc = open("Best_tc_value.txt", "r").readlines()
        sp_tc_separado = sp_tc[0].split(",")
        self.assertEqual(" '83.7378640776699'", sp_tc_separado[2])
```

* Comprobar las medias de cada variable:
* *Debido a que el archivo contenia otros datos, para acceder a ese en concreto tenemos que separarlo dentro de su linea con split, y luego acceder a esa posición*

```python
    def test_should_strike_mean_be_2799(self):
        strike_val = open("Best_strike_value.txt", "r").readlines()
        strike_separado = strike_val[1].split(": ")
        self.assertEqual("2.799714601504851", strike_separado[1])

    def test_should_tc_mean_be_2799(self):
        tc_val = open("Best_tc_value.txt", "r").readlines()
        tc_separado = tc_val[1].split(": ")
        self.assertEqual("3.6450563172892525", tc_separado[1])

    def test_should_sp_mean_be_8276(self):
        sp_val = open("Best_sp_value.txt", "r").readlines()
        sp_separado = sp_val[1].split(": ")
        self.assertEqual("82.7642571471821", sp_separado[1])
```

* Comprobar las medianas de cada variable:

* *Dado que en este caso es el único valor de esos ficheros, podremos acceder directamente mediante [0]*

```python
    def test_should_strike_median_be_288(self):
        strike_val = open("Median_strike_value.txt", "r").readlines()
        self.assertEqual("2.8877640768605", strike_val[0])

    def test_should_tc_median_be_370(self):
        tc_val = open("Median_tc_value.txt", "r").readlines()
        self.assertEqual("3.7037037037037037", tc_val[0])

    def test_should_sp_median_be_829(self):
        sp_val = open("Median_sp_value.txt", "r").readlines()
        self.assertEqual("82.9326923076923", sp_val[0])
```
