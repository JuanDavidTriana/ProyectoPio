import os

productos = [
  {"nombre": "Anillo de diamante", "precio": 1000, "cantidad": 5},
  {"nombre": "Anillo de cuarzo", "precio": 20, "cantidad": 8},
  {"nombre": "Anillo de plata", "precio": 200, "cantidad": 12},
  {"nombre": "Anillo de oro", "precio": 400, "cantidad": 5}
]
carrito = []

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux o Mac
        

def mostrar_productos():
  limpiar_pantalla()
  print(" -----------------------/Menú de productos-----------------------------------")
  for i, producto in enumerate (productos):
    print(f"{i+1}. {producto["nombre"]} - precio ${producto["precio"]} - cantidad {producto["cantidad"]}")
  

def agregar_al_carrito():
  limpiar_pantalla()
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
  limpiar_pantalla()
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
  limpiar_pantalla()
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
    limpiar_pantalla()
    print(" -----------------------Menu Joyeria-----------------------------------------")
    print("1-Mostrar productos disponibles")
    print("2- Añadir productos al carrito")
    print("3- Mostrar carrito")
    print("4- Finalizar compra, (pagar)")
    print("5- Salir de la compra")
    
    try:
      opciones = {
        1: mostrar_productos,
        2: agregar_al_carrito,
        3: mostrar_carrito,
        4: finalizar_compra,
      }

      selecion = int(input("Ingrese opcion:"))

      if selecion in opciones:
        opciones[selecion]()
        input("Enter para continuar.......")
      elif selecion == 5:
        break

    except ValueError:
      print("Entrada invalida, por favor ingrese un número")
      input("Enter para continuar.......")
    except Exception:
      print("Se ha presentado un error")
      input("Enter para continuar.......")


main()