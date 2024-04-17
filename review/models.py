from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User
from product.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField(
        validators=[
            MinLengthValidator(50, "Review must be greater than 50 characters")
        ],
        max_length=400,
    )
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["product", "user"]]
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
