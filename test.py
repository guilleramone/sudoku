import sys
sys.path.append('C:/Users/Guille/Documents/Repos/sudoku/')
from sudoku import imprimirSudoku, resolverSudoku, validarSudoku

sudoku =[[-1,-1,-1,6,3,7,-1,-1,-1],
         [-1,2,9,-1,1,-1,-1,-1,-1],
         [8,3,-1,9,2,5,4,1,-1],
         [-1,7,8,2,-1,6,1,-1,-1],
         [9,6,-1,8,7,1,5,-1,3],
         [5,1,2,-1,-1,4,-1,6,-1],
         [4,8,1,5,6,9,-1,-1,-1],
         [-1,-1,-1,-1,8,2,6,-1,4],
         [2,9,6,7,4,-1,-1,-1,-1]]
print(validarSudoku(sudoku))

sudokuValidado = validarSudoku(sudoku)
SudokuResuelto = resolverSudoku(sudoku)
imprimirSudoku(SudokuResuelto)
#print(">>",validarSudoku(sudoku))