from django.contrib.auth import get_user_model
from django.db import models

# from django.utils.translation import gettext_lazy as _
# from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

# import datetime

# CART_ID = 'CART-ID'

# class ItemAlreadyExists(Exception):
#     pass

# class ItemDoesNotExist(Exception):
#     pass

User = get_user_model()

# Create your models here.

class Sword(models.Model):
    image = models.ImageField(null=True, upload_to='swords/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(max_length = 200)

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Sword, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)

#class CartItem(models.Model):
    #item_name = models.CharField(max_length=60)
    #item_price = models.FloatField()

# class Order(models.Model):
#     orderitems  = models.ManyToManyField(Cart)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username



# class Cart(models.Model):
#     creation_date = models.DateTimeField(verbose_name=_('creation date'))
#     checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

#     class Meta:
#         verbose_name = _('cart')
#         verbose_name_plural = _('carts')
#         ordering = ('-creation_date',)

#     def __init__(self, request):
#         cart_id = request.session.get(CART_ID)
#         if cart_id:
#             try:
#                 cart = Cart.objects.get(id=cart_id, checked_out=False)
#             except models.Cart.DoesNotExist:
#                 cart = self.new(request)
#         else:
#             cart = self.new(request)
#         self.cart = cart

#     def __iter__(self):
#         for item in self.cart.item_set.all():
#             yield item

#     def new(self, request):
#         cart = Cart(request)
#         cart.save()
#         request.session[CART_ID] = cart.id
#         return cart

#     def add(self, product, unit_price, quantity=1):
#         try:
#             item = models.Item.objects.get(
#                 cart=self.cart,
#                 product=product,
#             )
#         except models.Item.DoesNotExist:
#             item = models.Item()
#             item.cart = self.cart
#             item.product = product
#             item.unit_price = unit_price
#             item.quantity = quantity
#             item.save()
#         else:
#             raise ItemAlreadyExists

#     def remove(self, product):
#         try:
#             item = models.Item.objects.get(
#                 cart=self.cart,
#                 product=product,
#             )
#         except models.Item.DoesNotExist:
#             raise ItemDoesNotExist
#         else:
#             item.delete()

#     def update(self, product, quantity, unit_price=None):
#         try:
#             item = models.Item.objects.get(
#                 cart=self.cart,
#                 product=product,
#             )
#         except models.Item.DoesNotExist:
#             raise ItemDoesNotExist

#     def clear(self):
#         for item in self.cart.item_set:
#             item.delete()


# class ItemManager(models.Manager):
#     def get(self, *args, **kwargs):
#         if 'product' in kwargs:
#             kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
#             kwargs['object_id'] = kwargs['product'].pk
#             del(kwargs['product'])
#         return super(ItemManager, self).get(*args, **kwargs)

# class Item(models.Model):
#     cart = models.ForeignKey(Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
#     unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
#     # product as generic relation
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()

#     objects = ItemManager()

#     class Meta:
#         verbose_name = _('item')
#         verbose_name_plural = _('items')
#         ordering = ('cart',)

#     def __unicode__(self):
#         return u''

#     def total_price(self):
#         return self.quantity * self.unit_price
#     total_price = property(total_price)

#     # product
#     def get_product(self):
#         return self.content_type.get_object_for_this_type(id=self.object_id)

#     def set_product(self, product):
#         self.content_type = ContentType.objects.get_for_model(type(product))
#         self.object_id = product.pk

#     product = property(get_product, set_product)

