from django.db import models

# Create your models here.
from django.db import models
from profiles.models import UserProfile
from product.models import Product


class Wishlist(models.Model):
    """
    A Wishlist model for users to keep track of their favourite products
    """

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_wishlist",
    )

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name
