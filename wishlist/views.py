from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from product.models import Product
from .models import Wishlist
from profiles.models import UserProfile


# Create your views here.
@login_required
def view_wishlist(request):
    """A view that renders the wishlist contents page"""

    user = UserProfile.objects.get(user=request.user)
    wishlist_items = Wishlist.objects.filter(user=user)

    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})


@login_required
def add_to_wishlist(request, item_id):
    """Add a quantity of the specified product to the shopping wishlist"""

    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)

    product_exists = Wishlist.objects.filter(
        user=user, product=product
    ).exists()
    if product_exists:
        messages.warning(
            request, f"{product.name} is already in your Wishlist."
        )
    else:
        # create a new wishlist item
        wishlist_item = Wishlist.objects.create(user=user, product=product)
        messages.success(
            request,
            f"{wishlist_item.product.name} added to Wishlist successfully!",
        )

    return redirect(reverse("product_detail", args=[item_id]))


@login_required
def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping wishlist"""

    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(user=user, product=product)

    wishlist_item.delete()
    messages.success(request, f"{product.name} has been successfully removed.")
    return redirect(reverse("view_wishlist"))
