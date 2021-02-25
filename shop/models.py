from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50, default ="")
    subcategory = models.CharField(max_length = 50 , default = "")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images" , default = "")

    def __str__(self):
        return self.product_name
    

# >>> from shop.models import Product
# >>> Product.objects.all()
# <QuerySet [<Product: watch>, <Product: Wallet>, <Product: python>]>

# >>> from django.utils import timezone
# >>> myprod = Product(product_name = "Mouse" , category = "Computer" , subcategory = "Devices", price =12,desc = "Chuha hai yeh" ,pub_date = timezone.now())


# >>> myprod.save()
# >>> myprod.product_id

# <class 'django.db.models.fields.AutoField'>
# >>> myprod.product_id
# <class 'django.db.models.fields.AutoField'>

# >>> myprod.product_name
# 'Mouse'

# >>> Product.objects.get(product_name = "Mouse")
# <Product: Mouse>

# >>> a = Product.objects.get(product_name = "Mouse")
# >>> a.desc
# 'Chuha hai yeh'