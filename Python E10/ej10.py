print ("----------------------------------------------------------------------------------------------------")
print ("EJERCICIO 10")

import funciones_ej10 as f

nombres =  ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina']


notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


alumnos = f.crearAlumnos(nombres,notas_1,notas_2)
print ("ALUMNOS Y SUS NOTAS: ", alumnos)


print ("------------------------------------------------------------")
promedios = [f.calcularPromedio(elem[1]) for elem in alumnos.items()]
print ("PROMEDIO DE CADA ALUMNO: ", promedios)


print ("------------------------------------------------------------")
print ("PROMEDIO GENERAL : ", f.promedioGeneral(promedios))
print ("PROMEDIO MAXIMO: ", f.promedioMaximo(promedios))
print ("NOTA MINIMA: ", f.promedioMinimo(alumnos.values()))
