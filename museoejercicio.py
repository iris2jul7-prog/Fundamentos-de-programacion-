print("Museo de antropologia")
precio = 45
precio_menor = 30
#validar la edad
while True:
    edad = int(input("Ingresa edad: "))
    if edad > 60:
        precio *= .12
        print("Adulto mayor, Tienes un descuento del 12%")
        break
    elif edad < 60 and edad > 17:
        tipo_visitante = int(input("Eres profesor (1) o estudiante (2)"))
        if tipo_visitante == 1:
            precio *= 0.10
            print("Profesor, descuento de 10%")
        elif tipo_visitante == 2:
            precio *= 0.10
            print("Estudiante, descuento de 10%")
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