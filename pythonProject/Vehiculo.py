class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas ):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

    def to_dict(self):
        return self.__dict__

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (f"Datos del automovil: Marca {self.marca}, Modelo {self.modelo}, "
                f"Ruedas {self.num_ruedas}, Velocidad {self.velocidad} km/h, "
                f"Cilindrada {self.cilindrada} cc")

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo,num_ruedas,velocidad,cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.nro_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo,num_ruedas,velocidad,cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.peso_carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"