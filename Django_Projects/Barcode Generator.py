import barcode
from barcode.writer import ImageWriter

ean = barcode.get("ean13", "123456789102", writer=ImageWriter())
ean.save("barcode")
