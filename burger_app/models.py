from django.db import models

# from django.core.validators import RegexValidator

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
         return self.name

class ContactMessage(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=50)
        message = models.CharField(max_length=100)
        submitted_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

class About(models.Model):
        content = models.TextField()

class Cart(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,default='')
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity
 