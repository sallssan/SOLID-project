from abc import ABC, abstractmethod

# Single Resposipilty  
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Single Resposipilty 
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

# Open Closed   
#  Liskov Substitution : 'DiscountStrategy' subclasses (NoDiscount, PercentageDiscount) can replace the parent class DiscountStrategy
# without breaking functionality, as they apply the same apply_discount method.
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total) :
        return total * (1 - self.percentage / 100)

# Dependancy Inversion
class OrderService:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def process_order(self, order):
        total = order.calculate_total()
        discounted_total = self.discount_strategy.apply_discount(total)
        print("The Order:")
        for item in order.items:
            print(f"- {item.name}: ${item.price:.2f}")
        print(f"Price after discount: ${discounted_total:.2f}")
        


if __name__ == "__main__":
    #items
    pasta = MenuItem("Pasta", 5.00)
    water = MenuItem("Water", 5.00)

    # Create an order 
    order = Order()
    order.add_item(pasta)
    order.add_item(water)

    # discount 
    discount_strategy = PercentageDiscount(10)  # 10% discount

    # Process the order
    order_service = OrderService(discount_strategy)
    order_service.process_order(order)
