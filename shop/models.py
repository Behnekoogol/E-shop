from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    shipping_address = models.TextField()

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self) -> str:
        return self.user.username


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    active = models.BooleanField(verbose_name=_("active"), default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('Categories')


# class ProductAttribute(models.Model):
#     product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(verbose_name=_("title"), max_length=64)


#     class Meta:
#         verbose_name = _('Product Attribute')
#         verbose_name_plural = _('Product Attributes')


class Product(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    slug = models.SlugField(verbose_name=_('slug'), allow_unicode=True, null=False)
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.PositiveIntegerField(verbose_name=_("price"))
    in_stock = models.BooleanField(verbose_name=_("in stock"), default=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Product, through='OrderProduct')
    order_date = models.DateTimeField(verbose_name=_("order date"), auto_now_add=True, null=True, blank=True)
    total_amount = models.PositiveIntegerField(verbose_name=_("total amount"))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"Order #{self.id} by {self.customer.user.username}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))

    class Meta:
        verbose_name = _('Ordered Product')
        verbose_name_plural = _('Ordered Products')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
