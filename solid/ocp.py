from abc import ABC, abstractmethod

# Definimos uma interface/abstração chamada DiscountStrategy
# Todas as estratégias de desconto seguirão essa interface
class EstrategiaDesconto(ABC):
    # Método abstrato que deverá ser implementado por todas as classes filhas
    @abstractmethod
    def calcular_desconto(self, pedido):
        pass

# Implementação da estratégia de desconto para clientes regulares
class DescontoRegular(EstrategiaDesconto):
    def calcular_desconto(self, pedido):
        # 5% de desconto para clientes regulares
        return pedido.total * 0.05
    
# Implementação da estratégia de desconto para clientes VIP
class DescontoVIP(EstrategiaDesconto):
    def calcular_desconto(self, pedido):
        # 10% de desconto para clientes VIP
        return pedido.total * 0.1

# Implementação da estratégia de desconto para clientes sem desconto
class SemDesconto(EstrategiaDesconto):
    def calcular_desconto(self, pedido):
        # Sem desconto  
        return 0
    
# Classe principal que calcula o desconto
# Recebe a estratégia de desconto a ser utilizada
class CalculadoraDesconto:
    def __init__(self, estrategia):
        # Armazena a estratégia de desconto a ser utilizada
        self.estrategia = estrategia

    # Método que calcula o desconto
    def calcular(self, pedido):
        return self.estrategia.calcular_desconto(pedido)

# Classe que representa um pedido
class Pedido:
    def __init__(self, total):
        # Valor total do pedido
        self.total = total

# Exemplo de uso
pedido = Pedido(100)


# Exemplo para um cliente regular
# Passando a estratégia de desconto para cliente regular
calculadora = CalculadoraDesconto(DescontoRegular())
# Calculando o desconto
desconto = calculadora.calcular(pedido)
print(f'Desconto para cliente regular: {desconto}')


# Exemplo para um cliente VIP
# Passando a estratégia de desconto para cliente VIP

calculadora = CalculadoraDesconto(DescontoVIP())

# Calculando o desconto

desconto = calculadora.calcular(pedido)
print(f'Desconto para cliente VIP: {desconto}')

# Exemplo para um cliente sem desconto
# Passando a estratégia de desconto para cliente sem desconto

calculadora = CalculadoraDesconto(SemDesconto())
print(f'Desconto para cliente sem desconto: {calculadora.calcular(pedido)}')


# class DiscountCalculator:
#     def calculate(self, order, customer_type):
#         if customer_type == 'regular':
#             return order.total * 0.05
#         elif customer_type == 'vip':
#             return order.total * 0.1
#         else:
#             return 0
