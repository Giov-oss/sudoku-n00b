import time

if __name__ == '__main__':
	tablero = []
	for _ in range(9):
		tablero.append([int(i) for i in input().split()])

tablero_incial=tablero

def transponer_tablero():
	global tablero_c
	tablero_c = list(map(list, zip(*tablero)))

def get_celda(l,m):
	global celda
	celda = []
	celdas=([[tablero[i+3*h][j+3*k] for i in range(3) for j in range(3)]for h in range(3) for k in range(3)])
	if l<3:
		if m<3:
			celda = celdas[0]
		elif m>2 and m<6:
			celda = celdas[1]
		else:
			celda = celdas[2]
	elif l>2 and l<6:
		if m<3:
			celda = celdas[3]
		elif m>2 and m<6:
			celda = celdas[4]
		else:
			celda = celdas[5]
	else: 
		if m<3:
			celda = celdas[6]
		elif m>2 and m<6:
			celda = celdas[7]
		else:
			celda = celdas[8]

def possible(i,j,n):
	transponer_tablero()
	get_celda(i,j)
	fila = tablero[i]
	columna = tablero_c[j]
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






