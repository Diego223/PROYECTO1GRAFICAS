def puntos (x,y):
    product=0
    for x,y in zip(x,y):
        product = product+x*y
    return product

def cruz(x, y):
    c = [x[1]*y[2] - x[2]*y[1],
         x[2]*y[0] - x[0]*y[2],
         x[0]*y[1] - x[1]*y[0]]

    return c

def zeros_matrix(filas, columnas):
    
    Matrix = []
    while len(Matrix) < filas:
        Matrix.append([])
        while len(Matrix[-1]) < columnas:
            Matrix[-1].append(0.0)
 
    return Matrix

def nul(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def exterminar(r11, r22, color, target=0):
    fac = (r22[color]-target) / r11[color]
    for i in range(len(r22)):
        r22[i] -= fac * r11[i]

def copiar(Matrix):
    
    filas = len(Matrix)
    columnas = len(Matrix[0])
 
    MatrixCopiada = zeros_matrix(filas, columnas)
 
    for i in range(filas):
        for j in range(columnas):
            MatrixCopiada[i][j] = Matrix[i][j]
 
    return MatrixCopiada

#def morn(a):
 #   mb=0
 #   for i in range(len(a)):
 #       mb+=a[i]**2
  #  module= mb**0.5
 #   

  #  return new

#def gauss(a):
 #   for i in range(len(a)):
 #       if a[i][i] == 0:
  #          for j in range(i+1, len(a)):
 #               if a[i][j] != 0:
 #                   a[i], a[j] = a[j], a[i]
 #                   break
 #           else:
 #               raise ValueError("Matrix is not invertible")
 
 #def inverse(a):
 #       tmp = [[] for _ in a]
 #   for i,fila in enumerate(a):
#        assert len(fila) == len(a)
 #       