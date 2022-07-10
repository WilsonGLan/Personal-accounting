import csv

def valorGasto():
  gasto = input("Por favor ingrese el valor: $")
  return gasto

def nombreProducto():
  producto = input("Por favor ingrese nombre del gasto: ").upper()
  return producto

fila = [nombreProducto(), valorGasto()]

nuevoArchivo = open('csv/income.csv', mode='w', encoding='utf-8-sig' )
with nuevoArchivo:
  writer = csv.writer(nuevoArchivo)
  writer.writerow(fila)



print("SISTEMA ADMINISTRADOR DE GASTOS PERSONALES")


