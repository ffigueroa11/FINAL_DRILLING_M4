
class Vehiculo:
    def __init__(self, marca, modelo, cant_ruedas ):
        self.marca = marca
        self.modelo = modelo
        self.cant_ruedas = cant_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, cant_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, cant_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (f"Datos del automovil: Marca {self.marca}, Modelo {self.modelo}, "
                f"Ruedas {self.cant_ruedas}, Velocidad {self.velocidad} km/h, "
                f"Cilindrada {self.cilindrada} cc")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vehiculos = []
    cantidad = int(input('Cuantos vehículos desea insertar: '))

    for i in range(cantidad):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))

        auto = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        vehiculos.append(auto)

    print("\nImprimiendo por pantalla los Vehiculos:")
    for vehiculo in vehiculos:
        print(vehiculo)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
