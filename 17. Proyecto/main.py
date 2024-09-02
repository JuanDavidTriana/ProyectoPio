productos = [
  {"nombre": "Anillo de diamante", "precio": 1000, "cantidad": 5},
  {"nombre": "Anillo de cuarzo", "precio": 20, "cantidad": 8},
  {"nombre": "Anillo de plata", "precio": 200, "cantidad": 12},
  {"nombre": "Anillo de oro", "precio": 400, "cantidad": 5}
]
carrito = []

def mostrar_productos():
  print(" -----------------------/Menú de productos-----------------------------------")
  for i, producto in enumerate (productos):
    print(f"{i+1}. {producto["nombre"]} - precio ${producto["precio"]} - cantidad {producto["cantidad"]}")

def agregar_al_carrito():
  mostrar_productos()
  try:
    opcion = int(input("introduce el producto que desees agregar al carrito "))
    if 1 <= opcion <= len (productos):
      cantidad = int(input("Ingrese la cantidad de productos que desees comprar: "))
      producto = productos[opcion - 1]
      if cantidad > producto ["cantidad"]:
        print("No hay suficientes existencias en stock")
      else:
        productos[opcion - 1]['cantidad'] -= cantidad
        carrito.append({"nombre": producto["nombre"], "precio": producto['precio'], "cantidad": cantidad})
        print(f"Felicidades, haz añadido {cantidad} {producto["nombre"]} exitosamente")
  except Exception as e:
    print("Se ha presentado un error", e)

def mostrar_carrito():
  if carrito:
    print("Carrito de compras.")
    for i, item in enumerate(carrito,1):
      print(f"{i}. Producto: {item['nombre']} - ${item['precio']} - cantidad: {item['cantidad']}")
  else:
    print("El carrito esta vacio")

def calcular_total():
  total = sum(item["precio"] * item["cantidad"] for item in carrito)
  print(f"El total de pagar es {total}")

def finalizar_compra():
  mostrar_carrito()
  if carrito:
    calcular_total()
    confirmar = input("Desea finalizar la compra (s/n)")

    if confirmar.lower() == "s":
        carrito.clear()
        print("Compra finalizada exitosamente")
    else:
        print("Compra cancelada")
  else:
      print("No hay productos")

def main():
  while True: 
    print(" -----------------------////-----------------------------------------")
    print("1-Mostrar productos disponibles")
    print("2- Añadir productos al carrito")
    print("3- Mostrar carrito")
    print("4- Finalizar compra, (pagar)")
    print("5- Salir de la compra")
    try:
      selection = int(input("Introduce el número de la opción a la cuál quieres ingresar: "))
      if selection == 1:
        mostrar_productos()
      elif selection == 2:
        agregar_al_carrito()
      elif selection == 3:
        mostrar_carrito()
      elif selection == 4:
        finalizar_compra()
      elif selection == 5:
        break
      else:
        print("Selección no valida, por favor seleccionar del 1 al 5")
    except ValueError:
      print("Entrada invalida, por favor ingrese un número")
    except Exception:
      print("Se ha presentado un error")


main()