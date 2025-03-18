class Product(models.Model):
    price = models.FloatField()
    discount = models.FloatField()

    @property
    def discounted_price(self):
        return self.price * (1 - self.discount/100)
