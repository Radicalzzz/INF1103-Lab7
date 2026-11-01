from physical_product import PhysicalProduct
from digital_product import DigitalProduct

keyboard = PhysicalProduct("P001", "Keyboard", 29.99, 50, 0.5)
ebook = DigitalProduct("P002", "E-book", 9.99, 100, 5)

keyboard.display_information()
ebook.display_information()