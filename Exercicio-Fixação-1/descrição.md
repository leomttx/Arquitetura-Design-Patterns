# Exercício Design Pattern - Abstract Factory

## Implementando um Sistema de Gestão de Reservas com Abstract Factory

### Contexto

Você foi contratado para desenvolver um sistema de gestão de reservas para uma rede de hotéis que possui estabelecimentos em diferentes regiões. Cada região tem suas próprias regras e características para reservas, o que implica em diferentes implementações para o processo de reserva, tipos de quartos e pagamentos. Para lidar com essa complexidade e promover a flexibilidade e escalabilidade do sistema, você decidiu usar o padrão de projeto Abstract Factory.

### Descrição do Problema

O sistema deve ser capaz de criar objetos relacionados para diferentes regiões. Especificamente, ele deve:
- Criar tipos de quartos diferentes dependendo da região (e.g., Quartos Luxo e Simples).
- Processar reservas de acordo com as regras específicas de cada região.
- Gerenciar pagamentos seguindo os métodos aceitos em cada região.

### Requisitos

- **Abstract Factory Interface**: Crie uma interface `ReservaFactory` que declare métodos para criar tipos de quartos (`criarQuarto`), processar reservas (`criarProcessoReserva`) e gerenciar pagamentos (`criarPagamento`).
  
- **Concrete Factories**: Implemente classes concretas que herdem de `ReservaFactory` para diferentes regiões (ex., `ReservaFactoryRegiaoA`, `ReservaFactoryRegiaoB`).
  
- **Abstract Products**: Crie interfaces ou classes abstratas para os produtos que serão criados (`Quarto`, `ProcessoReserva`, `Pagamento`). A classe abstrata `Quarto` possui método `definirDescricao`. A classe abstrata `ProcessoReserva` possui o método `reservar`, e a classe abstrata `Pagamento` possui o método `efetuarPagamento`.
  
- **Concrete Products**: Implemente classes concretas que representem os produtos específicos para cada região (e.g., `QuartoLuxoRegiaoA`, `QuartoSimplesRegiaoA`, `ProcessoReservaRegiaoA`, `PagamentoRegiaoA`). Nas classes concretas, implemente os métodos apenas para imprimir mensagens, como por exemplo no método `definirDescricao`, imprimir algo como "Quarto da Região A".
  
- **Cliente**: Implemente uma classe `SistemaReservas` que utiliza a `ReservaFactory` para criar objetos de acordo com a região especificada.

### Instruções

- Implementar as interfaces e classes conforme descrito nos requisitos.
- Escrever um programa principal que demonstre a criação de reservas em diferentes regiões utilizando a `ReservaFactory`.
- Testar o sistema criando reservas para pelo menos duas regiões diferentes, exibindo as informações das reservas e métodos de pagamento usados.
