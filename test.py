from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product

keyboard = PhysicalProduct("P001", "Keyboard", 29.99, 50, 0.5)
ebook = DigitalProduct("P002", "E-book", 9.99, 100, 5)

keyboard.display_information()
ebook.display_information()

print(keyboard.get_fulfilment_info())
print(ebook.get_fulfilment_info())

try:
    product = Product("P003", "Generic Product", 19.99, 20)
except TypeError as e:
    print("Error:", e)

print(f"Shipping cost for {keyboard.get_product_name()}: ${keyboard.calculate_shipping_cost():.2f}")