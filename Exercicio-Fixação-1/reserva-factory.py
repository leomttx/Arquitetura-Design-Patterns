from abc import ABC, abstractmethod

# Interface Abstract Factory
class ReservaFactory(ABC):
    
    @abstractmethod
    def criar_quarto(self):
        pass

    @abstractmethod
    def criar_processo_reserva(self):
        pass

    @abstractmethod
    def criar_pagamento(self):
        pass


# Interface Produto Abstrato - Quarto
class Quarto(ABC):

    @abstractmethod
    def definir_descricao(self):
        pass

# Interface Produto Abstrato - ProcessoReserva
class ProcessoReserva(ABC):

    @abstractmethod
    def reservar(self):
        pass

# Interface Produto Abstrato - Pagamento
class Pagamento(ABC):

    @abstractmethod
    def efetuar_pagamento(self):
        pass


# Implementação da ReservaFactory para a Região A
class ReservaFactoryRegiaoA(ReservaFactory):

    def criar_quarto(self):
        return QuartoLuxoRegiaoA()

    def criar_processo_reserva(self):
        return ProcessoReservaRegiaoA()

    def criar_pagamento(self):
        return PagamentoRegiaoA()


# Implementação da ReservaFactory para a Região B
class ReservaFactoryRegiaoB(ReservaFactory):

    def criar_quarto(self):
        return QuartoSimplesRegiaoB()

    def criar_processo_reserva(self):
        return ProcessoReservaRegiaoB()

    def criar_pagamento(self):
        return PagamentoRegiaoB()


# Quarto luxo da Região A
class QuartoLuxoRegiaoA(Quarto):

    def definir_descricao(self):
        print("Quarto Luxo da Região A")


# Processo de reserva da Região A
class ProcessoReservaRegiaoA(ProcessoReserva):

    def reservar(self):
        print("Reserva feita na Região A")


# Pagamento na Região A
class PagamentoRegiaoA(Pagamento):

    def efetuar_pagamento(self):
        print("Pagamento efetuado na Região A")


# Quarto simples da Região B
class QuartoSimplesRegiaoB(Quarto):

    def definir_descricao(self):
        print("Quarto Simples da Região B")


# Processo de reserva da Região B
class ProcessoReservaRegiaoB(ProcessoReserva):

    def reservar(self):
        print("Reserva feita na Região B")


# Pagamento na Região B
class PagamentoRegiaoB(Pagamento):

    def efetuar_pagamento(self):
        print("Pagamento efetuado na Região B")


# Classe cliente que usa a Abstract Factory
class SistemaReservas:

    def __init__(self, factory: ReservaFactory):
        self.quarto = factory.criar_quarto()
        self.processo_reserva = factory.criar_processo_reserva()
        self.pagamento = factory.criar_pagamento()

    def realizar_reserva(self):
        self.quarto.definir_descricao()
        self.processo_reserva.reservar()
        self.pagamento.efetuar_pagamento()


# Programa Principal
if __name__ == "__main__":
    # Criando uma reserva para a Região A
    factoryA = ReservaFactoryRegiaoA()
    sistemaA = SistemaReservas(factoryA)
    sistemaA.realizar_reserva()

    # Criando uma reserva para a Região B
    factoryB = ReservaFactoryRegiaoB()
    sistemaB = SistemaReservas(factoryB)
    sistemaB.realizar_reserva()
