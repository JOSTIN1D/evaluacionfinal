Alumnos = {"codigo": ["001", "002", "003"],
           "nombre": ["Ricardo", "Jose", "Davi"],
           "curso": ["Matematica", "Comunicacion", " Ingles"]}
nota_ = []
respuesta = "s"
while respuesta == "s":
    codigo = input("Ingrese el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    nota1 = int(input("Ingrese la  nota 1 : "))
    nota2 = int(input("Ingrese la nota 2: "))
    nota3 = int(input("Ingrese la nota 3: "))
    x = 0
    for i in Alumnos["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = Alumnos["nombre"][x]
            promedio = (nota1 + nota2 + nota3) / 3
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Nota 1: " + str(nota1) + " | " + "Nota 2: " + str(nota2) + " | " + "Nota 3: " + str(nota3) + " | " + "Promedio: " + str(promedio)]
            f = open("notas.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
        x += 1
    resp = input("¿Desea continuar? : s/n ")
    f = open("notas.txt")
    print(f.read())
    f.close()