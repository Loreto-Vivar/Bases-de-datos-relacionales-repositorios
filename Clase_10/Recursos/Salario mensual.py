class Empleado:
    def __init__(self,nombre,salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        return self.salario_mensual * 12
    
    def mostrar_informacion(self):
        print(f"Empleado:{self.nombre}, salario mensual {self.salario_mensual}")
    
    Empleado1 = Empleado("Ana",2000)
    
    Empleado1.mostrar_informacion()
    print(f"salario anual:{Empleado1.calcular_salario_anual()}")
    

      