from django.db import models
from django.utils import timezone
import uuid

class AuditCols(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # This model will not create a table in the database 
        # The Fields will be used and this class will treat as abstractclass

class Product(AuditCols):
    pid = models.CharField(primary_key=True,default=f"POK_{uuid.uuid4().hex[:6].upper()}", max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    


Product.objects.all()