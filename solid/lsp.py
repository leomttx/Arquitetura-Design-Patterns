from abc import ABC, abstractmethod

# Interface abstrata para formas geométricas
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

# Implementação da classe retângulo
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def set_largura(self, largura):
        self.largura = largura

    def set_altura(self, altura):
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Implementação da classe quadrado
class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def set_lado(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# Exemplo de uso
retangulo = Retangulo(4, 5)
print(f'Área do retângulo: {retangulo.area()}')

quadrado = Quadrado(5)
print(f'Área do quadrado: {quadrado.area()}')



# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def set_width(self, width):
#         self.width = width
    
#     def set_height(self, height):
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# class Square(Rectangle):
#     def set_width(self, width):
#         self.width = width
#         self.height = width
    
#     def set_height(self, height):
#         self.height = height
#         self.width = height
