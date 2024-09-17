class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class OrderCalculator:
    @staticmethod    
    def calculate_total(order):
        total = sum(item['price'] for item in order.items)
        return total
    
class OrderPrinter:
    @staticmethod
    def print_order(order):
        print(f"Order ID: {order.order_id}")
        for item in order.items:
            print(f"Item: {item['name']}, Price: {item['price']}")

class OrderSaver:
    @staticmethod
    def save_to_db(order):
        # Simulando a gravação no banco de dados
        print(f"Order {order.order_id} saved to database")


order = Order(1, [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 200}])

# Calcula o total do pedido
total = OrderCalculator.calculate_total(order)
print(f"Total: {total}")

# Imprime o pedido
OrderPrinter.print_order(order)

# Salva o pedido no banco de dados
OrderSaver.save_to_db(order)
