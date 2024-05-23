class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Vector(result_x, result_y)

    def __sub__(self, other):
        result_x = self.x - other.x
        result_y = self.y - other.y
        return Vector(result_x, result_y)


def print_vector_operation(operation, vector1, vector2, result):
    print(f"{operation} vectors:")
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print("Procedure:")
    print(f"  Vector 1: ({vector1.x}, {vector1.y})")
    print(f"+ Vector 2: ({vector2.x}, {vector2.y})")
    print("---------------------")
    print(f"  Result:   ({result.x}, {result.y})")
    print()


# Solicitar al usuario los valores de los vectores
print("Ingrese los valores del primer vector:")
x1 = float(input("Componente x: "))
y1 = float(input("Componente y: "))
vector1 = Vector(x1, y1)

print("\nIngrese los valores del segundo vector:")
x2 = float(input("Componente x: "))
y2 = float(input("Componente y: "))
vector2 = Vector(x2, y2)

# Suma de vectores
suma = vector1 + vector2
print_vector_operation("Suma", vector1, vector2, suma)

# Resta de vectores
resta = vector1 - vector2
print_vector_operation("Resta", vector1, vector2, resta)