from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.0

# Only run the following code if this script is executed directly (not imported)
if __name__ == "__main__":
    physical_product1 = PhysicalProduct("P008", "Smartphone", 800.00, 30, 0.2)
    physical_product1.display_information()