from abc import ABC, abstractmethod

# Interface que define o comportamento de um banco de dados
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# Implementação concreta para o MySQL
class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL database")

# Implementação concreta para outro tipo de banco, como PostgreSQL (opcional)
class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL database")

# Repositório de pedidos, agora desacoplado de uma implementação específica de banco de dados
class OrderRepository:
    # Recebemos o banco de dados como uma abstração (injeção de dependência)
    def __init__(self, db: Database):
        self.db = db
    
    def save(self, order):
        self.db.connect()
        print(f"Order {order} saved to database")

# Exemplo de uso:
mysql_db = MySQLDatabase()
order_repository = OrderRepository(mysql_db)
order_repository.save("12345")

# Se quisermos mudar o banco de dados, é simples:
postgres_db = PostgreSQLDatabase()
order_repository_postgres = OrderRepository(postgres_db)
order_repository_postgres.save("67890")




#  class MySQLDatabase:
#     def connect(self):
#         print("Connected to MySQL database")

# class OrderRepository:
#     def __init__(self):
#         self.db = MySQLDatabase()
    
#     def save(self, order):
#         self.db.connect()
#         print(f"Order {order} saved to database")
