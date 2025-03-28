class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

def merge_sort(arreglo, clave):
    if len(arreglo) <= 1:
        return arreglo
    
    mitad = len(arreglo) // 2
    izquierda = merge_sort(arreglo[:mitad], clave)
    derecha = merge_sort(arreglo[mitad:], clave)
    
    return merge(izquierda, derecha, clave)

def merge(izquierda, derecha, clave):
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if getattr(izquierda[i], clave) <= getattr(derecha[j], clave):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def heap_sort(arreglo, clave):
    def heapify(arreglo, n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2
        
        if izquierda < n and getattr(arreglo[izquierda], clave) > getattr(arreglo[mayor], clave):
            mayor = izquierda
        
        if derecha < n and getattr(arreglo[derecha], clave) > getattr(arreglo[mayor], clave):
            mayor = derecha
        
        if mayor != i:
            arreglo[i], arreglo[mayor] = arreglo[mayor], arreglo[i]
            heapify(arreglo, n, mayor)
    
    n = len(arreglo)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arreglo, n, i)
    
    for i in range(n - 1, 0, -1):
        arreglo[0], arreglo[i] = arreglo[i], arreglo[0]
        heapify(arreglo, i, 0)
    
    return arreglo

def quick_sort(arreglo, clave):
    if len(arreglo) <= 1:
        return arreglo
    
    pivote = arreglo[len(arreglo) // 2]
    izquierda = [x for x in arreglo if getattr(x, clave) < getattr(pivote, clave)]
    medio = [x for x in arreglo if getattr(x, clave) == getattr(pivote, clave)]
    derecha = [x for x in arreglo if getattr(x, clave) > getattr(pivote, clave)]
    
    return quick_sort(izquierda, clave) + medio + quick_sort(derecha, clave)

def busqueda_binaria(arreglo, clave, valor):
    inicio = 0
    fin = len(arreglo) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = getattr(arreglo[medio], clave)
        
        if valor_medio == valor:
            return arreglo[medio]
        elif valor_medio < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return None

def mostrar_empleados(empleados):
    for empleado in empleados:
        print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Salario: {empleado.salario}")

def menu_principal():
    empleados = [
        Empleado("Carlos", 35, 3000),
        Empleado("María", 28, 2500),
        Empleado("Pedro", 42, 4000),
        Empleado("Ana", 31, 3500),
        Empleado("Luis", 25, 2000)
    ]
    
    while True:
        print("\nBienvenido a la Aplicación Empresarial, ¿Qué quiere hacer?:")
        print("1. Ordenar por edad (Heap Sort)")
        print("2. Ordenar por nombre (Quick Sort)")
        print("3. Ordenar por salario (Merge Sort)")
        print("4. Buscar por edad")
        print("5. Buscar por salario")
        print("6. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            empleados = heap_sort(empleados, "edad")
            mostrar_empleados(empleados)
        
        elif opcion == "2":
            empleados = quick_sort(empleados, "nombre")
            mostrar_empleados(empleados)
        
        elif opcion == "3":
            empleados = merge_sort(empleados, "salario")
            mostrar_empleados(empleados)
        
        elif opcion == "4":
            edad = int(input("Ingrese la edad a buscar: "))
            empleado = busqueda_binaria(sorted(empleados, key=lambda x: x.edad), "edad", edad)
            
            if empleado:
                print(f"Empleado encontrado: Nombre: {empleado.nombre}, Edad: {empleado.edad}, Salario: {empleado.salario}")
            else:
                print("Empleado no encontrado")
        
        elif opcion == "5":
            salario = int(input("Ingrese el salario a buscar: "))
            empleado = busqueda_binaria(sorted(empleados, key=lambda x: x.salario), "salario", salario)
            
            if empleado:
                print(f"Empleado encontrado: Nombre: {empleado.nombre}, Edad: {empleado.edad}, Salario: {empleado.salario}")
            else:
                print("Empleado no encontrado")
        
        elif opcion == "6":
            print("Gracias por usar la aplicación")
            break
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()