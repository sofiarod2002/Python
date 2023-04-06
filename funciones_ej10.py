def crearAlumnos (nombres,notas_1,notas_2):
    alumnos = dict() 
    for a,n,n2 in zip(nombres,notas_1,notas_2):
        alumnos[a] = n, n2
    return alumnos

def calcularPromedio (alumnos):
    promedioAlumnos = dict ()
    for alu in alumnos:
        promedioAlumnos[alu] = sum(alumnos[alu])/2
    return promedioAlumnos

def promedioGeneral (alumnos):
    return sum(alumnos.values()) / len(alumnos)

def promedioMaximo(alumnos):
    return max(alumnos, key= alumnos.get)

def promedioMinimo (alumnos):
    return min(alumnos, key= alumnos.get)
