class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class OrderCalculator:    
    def calculate_total(self):
        total = sum(item['price'] for item in self.items)
        return total
    
class OrderPrinter:
    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(f"Item: {item['name']}, Price: {item['price']}")

class OrderSaver:
    def save_to_db(self):
        # Simulando a gravação no banco de dados
        print(f"Order {self.order_id} saved to database")
