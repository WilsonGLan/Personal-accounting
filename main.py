
def valorGasto():
  gasto = input("Por favor ingrese el valor: $")
  return gasto

def nombreProducto():
  producto = input("Por favor ingrese nombre del gasto: ").upper()
  return producto


print("SISTEMA ADMINISTRADOR DE GASTOS PERSONALES")

nombreProducto()
valorGasto()