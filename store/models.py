from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    Category Table
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    """
    The Product table containing all product items.
    """

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        max_digits=6,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        max_digits=6,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    in_stock = models.BooleanField(
        verbose_name=_("In stock"),
        default=True,
    )
    qty_36 = models.DecimalField(
        verbose_name=_("Amount of size 36"),
        max_digits=6,
        decimal_places=2,
    )
    qty_38 = models.DecimalField(
        verbose_name=_("Amount of size 38"),
        max_digits=6,
        decimal_places=2,
    )
    qty_40 = models.DecimalField(
        verbose_name=_("Amount of size 40"),
        max_digits=6,
        decimal_places=2,
    )
    qty_42 = models.DecimalField(
        verbose_name=_("Amount of size 42"),
        max_digits=6,
        decimal_places=2,
    )
    qty_44 = models.DecimalField(
        verbose_name=_("Amount of size 44"),
        max_digits=6,
        decimal_places=2,
    )
    qty_46 = models.DecimalField(
        verbose_name=_("Amount of size 46"),
        max_digits=6,
        decimal_places=2,
    )
    qty_48 = models.DecimalField(
        verbose_name=_("Amount of size 48"),
        max_digits=6,
        decimal_places=2,
    )
    qty_50 = models.DecimalField(
        verbose_name=_("Amount of size 50"),
        max_digits=6,
        decimal_places=2,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
