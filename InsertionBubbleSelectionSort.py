def ordenamiento_insercion(arr):
    N = len(arr)
    for i in range(1, N):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = actual
    return arr

def ordenamiento_burbuja(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

def ordenamiento_seleccion(arr):
    N = len(arr)
    for i in range(N - 1):
        indice_minimo = i
        for j in range(i + 1, N):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        
        if indice_minimo != i:
            temp = arr[i]
            arr[i] = arr[indice_minimo]
            arr[indice_minimo] = temp
    return arr

personas = [
    {"nombre": "Camila", "codigo": 1},
    {"nombre": "Daniel", "codigo": 2},
    {"nombre": "Sofia", "codigo": 3},
    {"nombre": "Juan", "codigo": 4},
    {"nombre": "Valentina", "codigo": 5},
    {"nombre": "Carlos", "codigo": 6},
    {"nombre": "Isabella", "codigo": 7},
    {"nombre": "Andrés", "codigo": 8},
    {"nombre": "Mariana", "codigo": 9},
    {"nombre": "Felipe", "codigo": 10}
]

ordenado_insercion = ordenamiento_insercion(personas.copy())
ordenado_burbuja = ordenamiento_burbuja(personas.copy())
ordenado_seleccion = ordenamiento_seleccion(personas.copy())

print("Ordenamiento por Inserción:")
for persona in ordenado_insercion:
    print(f"{persona['nombre']}: {persona['codigo']}")

print("\nOrdenamiento por Burbuja:")
for persona in ordenado_burbuja:
    print(f"{persona['nombre']}: {persona['codigo']}")

print("\nOrdenamiento por Selección:")
for persona in ordenado_seleccion:
    print(f"{persona['nombre']}: {persona['codigo']}")