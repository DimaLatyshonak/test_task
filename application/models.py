from django.db import models


class CreditApplication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    credit_application = models.OneToOneField(
        CreditApplication, on_delete=models.CASCADE, related_name="contract"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Producer(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    credit_application = models.ForeignKey(
        CreditApplication, on_delete=models.CASCADE, related_name="products"
    )
    manufacturer = models.ForeignKey(
        Producer, on_delete=models.CASCADE, related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True)
