class Estudiantes:
    def __init__(self, nombre, apellido, id, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.carrera = carrera

    def View(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("ID:", self.id)
        print("Carrera:", self.carrera)

# Subclase Materias que hereda de la superclase Estudiantes
class Materias(Estudiantes):
    def __init__(self, nombre, apellido, id, carrera):
        super().__init__(nombre, apellido, id, carrera)

    def Matricula(self):
        materias = []
        for i in range(3):
            nombre = input("Ingrese el nombre de la materia: ")
            codigo = input("Ingrese el código de la materia: ")
            creditos = input("Ingrese los créditos de la materia: ")
            materias.append([nombre, codigo, creditos])
        return materias

    def View(self):
        super().View()
        print("Materias matriculadas")
        for materia in self.Matricula():
            print("Nombre:", materia[0])
            print("Código:", materia[1])
            print("Créditos:", materia[2])

# Prueba del algoritmo
primiparo = Estudiantes("Pedro", "Perez", 873924, "Biologia")
primiparo.View()
matricula_primiparo = Materias("Carlos", "Giraldo", 837224, "Ingenieria de Sistemas")
print(matricula_primiparo.Matricula())
matricula_primiparo.View()