import time

if __name__ == '__main__':
	tablero = []
	for _ in range(9):
		tablero.append([int(i) for i in input().split()])

def get_celda(x,y):
	global celda
	l=(x//3)*3
	m=(y//3)*3
	celda=[tablero[l+i][m+j] for i in range(3) for j in range(3)]

def possible(i,j,n):
	get_celda(i,j)
	fila = tablero[i]
	columna = [tablero[k][j] for k in range(9)]
	if fila.count(n) == 0 and columna.count(n) == 0 and celda.count(n)==0:
		return True

def rastreo():
	for i in range(9):
		for j in range(9):
			if tablero[i][j] == 0:
				for k in range(1,10):
					if possible(i,j,k):
						tablero[i][j] = k
						rastreo()
						tablero[i][j] = 0
				return
	for i in range(9):
		print(tablero[i])

t = time.process_time()
rastreo()
elapsed_time = time.process_time() - t

print(elapsed_time)