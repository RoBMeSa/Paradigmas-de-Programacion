#=============================
# Clase ClienteBancario
#=============================
class ClienteBancario:
    __nombres:str= None
    __apellidos:str=None
    __edad : int = None
    __balanceDeCuenta : float = 0.0

    def __init__(self, nombres:str, apellidos:str, edad: int = 0, balanceDeCuenta:float=0.0):
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.nombres = nombres
        self.apellidos = apellidos
        self.__edad = edad
        self.balanceDeCuenta = balanceDeCuenta

    def getNombreCompleto(self) ->str:
        return self.nombres + " " + self.apellidos

    def __mandarEmail(self, titulo:str, texto:str)-> None:
        print("mandar email: " + titulo + " con texto: " + texto)

    def __enviarBalanceAlBanco(self, cantidad: float)-> None:
        print("ENviando cantidad: " + str(cantidad) + " al banco...")

#=============================
# Metodo privado con dos guiones bajos
# Si la edad es menor de 18 genera un error
#=============================
        
    def __validarEdad(self, edad: int)-> None:
        if edad < 18:
            raise Exception("Es menor de edad")
    def imprimirInfo(self) -> str: 
        return "Nombre: " + self.getNombreCompleto() + ", Edad: " + str(self.__edad) + ", Balance: " + str(self.__balanceDeCuenta)

#=============================
# Metodo privado que checa si el balance es negativo
# y genera un error
#=============================

    def __validarCantidad(self, balanceDeCuenta: float) -> None:
        if balanceDeCuenta < 0:
            raise Exception("El balance en la cuenta no puede ser negativo")
    
    def guardarDinero(self, cantidad:float) -> None:
        self.__balanceDeCuenta = self.__balanceDeCuenta + cantidad
        self.__mandarEmail("----- guardando deposito ----", " se recibieron " + str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)

    def retirarDinero(self, cantidad:float) -> None:
        cantidadFinal = self.__balanceDeCuenta - cantidad
        self.__validarCantidad(cantidadFinal)
        self.__balanceDeCuenta = cantidadFinal
        self.__mandarEmail("Retirando dinero", "se retiro" + str(cantidad))
        self.__enviarBalanceAlBanco(Cantidad)


    












