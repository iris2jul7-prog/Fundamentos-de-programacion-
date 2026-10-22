print("Museo de antropologia")
precio = 45
precio_menor = 30
#validar la edad
while True:
    edad = int(input("Ingresa edad: "))
    if edad > 60:
        precio *= .12
        print("Adulto mayor, descuento de adulto mayor")
        break
    elif edad < 60 and edad > 17:
        tipo = int(input("Eres profesor (1) o estudiante (2)"))
        if tipo == 1:
            precio *= 0.10
            print("Profesor, descuento de profesor ")
        elif tipo == 2:
            precio *= 0.10
            print("Estudiante, descuento de estudiante")
        break
    elif edad < 18 and edad > 3:
        precio_menor *= 0.10
        print("Estudiante, descuento concedido")
        break
    elif edad <= 3:
        print("No pagas entrada pequeñuelo")
        break
    else:
        print("Ingresa respuesta válida")