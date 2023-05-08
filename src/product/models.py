from django.db import models


# Create your models here.

def upload_to(instance, filename):
    return '/'.join(['media', str(instance.wording), filename])


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    wording = models.CharField(max_length=255)
    describe = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.wording

    def price_promotion(self):
        if self.promotion:
            percentage_decimal = self.promotion.percentage / 100
            reduce_price = self.price * (1 - percentage_decimal)
            return reduce_price
        else:
            return self.price


class Promotion(models.Model):
    percentage = models.IntegerField(null=False, blank=False)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.percentage
