from django.db import models
from django.conf import settings

# Farmer Model
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Processor Model
class Processor(models.Model):
    name = models.CharField(max_length=100)
    process_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Distributor Model
class Distributor(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Product can be associated with a Farmer, Processor, or Distributor
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True, blank=True)
    processor = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Consumer Model
class Consumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Order Model
class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa'),
    ]

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to Product
    quantity = models.PositiveIntegerField(default=1)
    ordered_on = models.DateTimeField(auto_now_add=True)

    # Payment method field
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
    )

    # Track the order status
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order by {self.consumer.name} for {self.quantity} of {self.product.name}"
