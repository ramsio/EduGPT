class EduGPT:
    def __init__(self):
        self.name = "EduGPT"
        self.version = "0.0.2"

    def show_information(self):
        print("=" * 45)
        print(f"{self.name} v{self.version}")
        print("=" * 45)
        print("Estado: Activo")

    def train(self):
        print("=" * 45)
        print("ENTRENAMIENTO")
        print("=" * 45)
        print("Esta función estará disponible próximamente")

    def show_menu(self):
        self.show_information()
        print("1. Construir corpus")
        print("2. Entrenar modelo")
        print("3. Información del modelo")
        print("4. Tokenizador Manual")
        print("5. Tokenizador NLTK")
        print("6. Tokenizador TikToken")
        print("0. Salir")
        return input("Seleccione una opción: ")
