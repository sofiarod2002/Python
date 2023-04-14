def crearAlumnos (nombres,notas_1,notas_2):
    alumnos = dict() 
    for a,n,n2 in zip(nombres,notas_1,notas_2):
        alumnos[a] = n, n2
    return alumnos

def calcularPromedio (alumnos):
    return sum(alumnos)/len(alumnos)

def promedioGeneral (promedios):
    return calcularPromedio(promedios)

def promedioMaximo(promedios):
    return max(promedios)

def promedioMinimo (notas):
    return min(min(notas))
