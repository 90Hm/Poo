# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca  # Atributo encapsulado
        self.__modelo = modelo  # Atributo encapsulado
        self.anio = anio

    # Métodos getter
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    # Métodos setter
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def descripcion(self):
        return f"{self.get_marca()} {self.get_modelo()} ({self.anio})"


# Clase derivada Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    # Sobrescribiendo el método descripcion
    def descripcion(self):
        return f"Auto: {self.get_marca()} {self.get_modelo()} ({self.anio}), {self.puertas} puertas"

    def conducir(self):
        return f"Conduciendo el auto {self.get_marca()} {self.get_modelo()}."


# Clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    # Sobrescribiendo el método descripcion
    def descripcion(self):
        return f"Motocicleta: {self.get_marca()} {self.get_modelo()} ({self.anio}), Tipo: {self.tipo}"

    def conducir(self):
        return f"Conduciendo la motocicleta {self.get_marca()} {self.get_modelo()}."


# Creación de instancias y demostración
auto1 = Auto("Toyota", "Corolla", 2020, 4)
moto1 = Motocicleta("Yamaha", "MT-07", 2019, "Deportiva")

print(auto1.descripcion())  # Salida: Auto: Toyota Corolla (2020), 4 puertas
print(moto1.descripcion())  # Salida: Motocicleta: Yamaha MT-07 (2019), Tipo: Deportiva

auto1.set_marca("Honda")
print(auto1.descripcion())  # Salida: Auto: Honda Corolla (2020), 4 puertas

print(auto1.conducir())  # Salida: Conduciendo el auto Honda Corolla.
print(moto1.conducir())  # Salida: Conduciendo la motocicleta Yamaha MT-07.
