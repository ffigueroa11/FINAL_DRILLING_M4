import csv
from Vehiculo import Vehiculo,Automovil,Particular,Carga,Bicicleta,Motocicleta

class GestionVehiculos:
    def __init__(self, vehiculos):
        self.vehiculos = vehiculos

    def guardar_datos_csv(self, nombre_archivo="vehiculos.csv"):
        try:
            with open(nombre_archivo, mode="w", newline='') as archivo:
                archivo_csv = csv.writer(archivo)
                for vehiculo in self.vehiculos:
                    clase = f"<class '{vehiculo.__class__.__module__}.{vehiculo.__class__.__name__}'>"
                    atributos = str(vehiculo.__dict__)
                    archivo_csv.writerow([clase, atributos])
            print(f"Datos guardados exitosamente en {nombre_archivo}.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def leer_datos_csv(self, nombre_archivo="vehiculos.csv"):

        try:
            with open(nombre_archivo, mode="r") as archivo:
                archivo_csv = csv.reader(archivo)
                vehiculos_clasificados = {
                    'Particular': [],
                    'Carga': [],
                    'Bicicleta': [],
                    'Motocicleta': []
                }
                for row in archivo_csv:
                    clase = row[0].split('.')[-1][:-2]
                    atributos = eval(row[1])
                    if clase in vehiculos_clasificados:
                        vehiculos_clasificados[clase].append(atributos)


                for tipo, lista in vehiculos_clasificados.items():
                    print(f"\nLista de Vehículos {tipo}:")
                    for vehiculo in lista:
                        print(vehiculo)

        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer los datos: {e}")

# Press the green button in the gutter to run the script.
vehiculos = []

if __name__ == '__main__':

    generarCSV = GestionVehiculos(vehiculos)

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

    print("\n########## PARTE 2 ##########")

    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos.extend([particular, carga, bicicleta, motocicleta])

    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    print("\n########## Verificación de Instancias ##########")

    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehiculo Particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehiculo Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    generarCSV.guardar_datos_csv()

    # Leer los datos desde vehiculos.csv e imprimirlos por tipo
    generarCSV.leer_datos_csv()
