def existeValor(array, number):
    existe = False
    for n in array:
        if number == n:
            existe = True
            break
    return existe

def validarSudoku(sudoku):
    #Valida Filas
    for fila in sudoku:
        valoresPosibles = [1,2,3,4,5,6,7,8,9]
        for columna in fila:
            if columna != -1:
                if existeValor(valoresPosibles, columna):
                    valoresPosibles.remove(columna)
        if len(valoresPosibles) != 0:            
            return False
    #Valida Columnas
    for columna in range(9):
        valoresPosibles = [1,2,3,4,5,6,7,8,9]
        for fila in range(9):
            if columna != -1:
                if existeValor(valoresPosibles, sudoku[fila][columna]):
                    valoresPosibles.remove(sudoku[fila][columna])
        if len(valoresPosibles) != 0:
            print(valoresPosibles)
            return False
    #Valida  submatrix
    for n in range(0,9,3):
        valoresPosibles = [1,2,3,4,5,6,7,8,9]
        for fila in range(n, n+3):
            for columna in range(n, n+3):
                if columna != -1:
                    if existeValor(valoresPosibles, sudoku[fila][columna]):
                        valoresPosibles.remove(sudoku[fila][columna])
        if len(valoresPosibles) != 0:
            return False
    return True

        
def traerTodasCeldasVacias(sudoku):
    emptycells = []
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == -1:
                possiblevalues = traerPosiblesValores(sudoku,row,column)
                emptycell = [row, column, possiblevalues]
                emptycells.append(emptycell)
    #Sort empty cells by amount of possible values.
    emptycells = sort(emptycells)
    return emptycells

#
def traerPosiblesValores(sudoku, row, column):
    valoresPosibles = [1,2,3,4,5,6,7,8,9]
    #Busca no posibles valores basado en la fila y remueve desde los valoresPosibles
    for ii in range(9):
        if ii != column and sudoku[row][ii] != -1:
            if existeValor(valoresPosibles, sudoku[row][ii]):
                valoresPosibles.remove(sudoku[row][ii])
    #Busca no posibles valores basados en la columna y remueve desde los valoresPosibles
    for ii in range(9):
        if ii != row and sudoku[ii][column] != -1:
            if existeValor(valoresPosibles, sudoku[ii][column]):
                valoresPosibles.remove(sudoku[ii][column])
    #Search non-possible values based on sub matrix and remove from 
    #possiblevalues.
    #First, calculate row range, that will depende on the row.
    rowrange = []
    columnrange = []
    if row == 0 or row == 3 or row == 6:
        rowrange = [row, row + 1, row + 2]
    elif row == 2 or row == 5 or row == 8:
        rowrange = [row - 2, row - 1, row]
    else:
        rowrange = [row - 1, row, row +1]
    #Calculate column range, that will depende on the row.
    if column == 0 or column == 3 or column == 6:
        columnrange = [column, column + 1, column + 2]
    elif column == 2 or column == 5 or column == 8:
        columnrange = [column - 2, column - 1, column]
    else:
        columnrange = [column - 1, column, column + 1]
    #Iterate through the row and column range to chech the possible values.
    for rowindex in rowrange:
        for columnindex in columnrange:
            if rowindex != row and columnindex != column and sudoku[rowindex][columnindex] != -1:
                if existeValor(valoresPosibles, sudoku[rowindex][columnindex]):
                    valoresPosibles.remove(sudoku[rowindex][columnindex])
    return valoresPosibles


def merge(a, b):
    a_index = 0
    b_index = 0
    z = []
    while a_index<len(a) or b_index<len(b):
        if a_index == len(a):
            z.append(b[b_index])
            b_index = b_index + 1
        elif b_index == len(b):
            z.append(a[a_index])
            a_index = a_index + 1
        elif len(a[a_index][2])<len(b[b_index][2]):
            z.append(a[a_index])
            a_index = a_index + 1
        else:
            z.append(b[b_index])
            b_index = b_index + 1
    return z

def sort(array):
    array_sorted = []
    a = array[0:int(len(array)/2)]
    b = array[int(len(array)/2):len(array)]
    if len(a)>1:
        a = sort(a)
    
    if len(b)>1:
        b = sort(b)
    
    array_sorted = merge(a, b)
    return array_sorted    


#Resuelve el Sudoku.  
def resolverSudoku(sudoku):
    celdasVacias = traerTodasCeldasVacias(sudoku)

    #Si no hay Celdas Vacias valida si el Sudoku es correcto o no 
    if len(celdasVacias) == 0:
        if validarSudoku(sudoku):
            return sudoku
        else:
            return False

    #Si hay celdas vacias pero es la primera al estar ordenadas, 
    #no es posible generar devuelvo False.
    elif len(celdasVacias[0][2]) == 0:
        return False

    #Obtengo iterativamente las celdas vacias
    llenarCeldaVacias = (len(celdasVacias[0][2]) == 1)
    while llenarCeldaVacias:
        for celdaVacia in celdasVacias:
            if len(celdaVacia[2]) == 1:
                row = celdaVacia[0]
                column = celdaVacia[1]
                sudoku[row][column] = celdaVacia[2][0]
                llenarCeldaVacias = True
            else:
                break
        celdasVacias = traerTodasCeldasVacias(sudoku)
        if len(celdasVacias) > 0:
            llenarCeldaVacias = len(celdasVacias[0][2]) == 1
        else:
            break
    if len(celdasVacias) == 0:
        return sudoku

  # Busqueda Recursiva
    i = 0
    while i in range(len(celdasVacias)):
        z = 0
        while z in range(len(celdasVacias[i][2])):            
            nuevoSudoku = list(sudoku)
            nuevoSudoku[celdasVacias[i][0]][celdasVacias[i][1]] = celdasVacias[i][2][z]
            testSudoku = resolverSudoku(nuevoSudoku)
            if testSudoku != False:
                print(testSudoku)
            if testSudoku != False and len(testSudoku) !=0:
                #Esta OK
                return testSudoku
            z += 1
        i += 1
    return False

def imprimirSudoku(sudoku):
    for i in sudoku:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6],
              "\t",i[7],"\t",i[8],"\t")