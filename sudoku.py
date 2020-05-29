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

def rastreo():
	for i in range(9):
		for j in range(9):
			if tablero[i][j] == 0:
				transponer_tablero()
				get_celda(i,j)
				ops = 0
				for k in range(1,10):
					fila = tablero[i]
					columna = tablero_c[j]
					if fila.count(k) == 0 and columna.count(k) == 0 and celda.count(k)==0:
						ops = ops+1
						if ops == 1:
							num = k
						elif ops >1:
							break
				if ops == 1:
					tablero[i][j] = num
						
n=0
while True:
	rastreo()
	zeros=0
	for i in range(9):
		zeros=zeros+tablero[i].count(0)
	if zeros == n:
		break
	else:
		n = zeros
	print('---------------------')
	for i in range(9):
		print(tablero[i])
	print('---------------------')



print('---------------------')
for i in range(9):
	print(tablero[i])
print('---------------------')




