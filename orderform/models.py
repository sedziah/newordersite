from django.db import models

# Create your models here.
class NewOrders(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    primary_phone_number = models.CharField(max_length=10)
    alternate_phone_number = models.CharField(max_length=10)
    item_category = models.CharField(max_length=200, choices= [
    ('Mobile Phone', 'Mobile Phones'),
    ('Home, Furniture & Appliances', 'Home, Furniture & Appliances'),
    ('Electronics', 'Electronics'),
    ('Others', 'Others'),
    ])
    purchase_item = models.CharField(max_length=255)
    payment_mode = models.CharField(max_length=255, choices=[
    ('Loan', 'Loan'),
    ('Cash', 'Cash'),
    ])
    email = models.EmailField()
    comments = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name_plural = "New Orders"