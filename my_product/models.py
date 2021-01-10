from django.db import models

# Create your models here.

import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


# Create your models here.

class ProductsManager(models.Manager):
    def get_active_products(self):

        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):

        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None





class Product(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)

    objects = ProductsManager()

    def __str__(self):
        return self.title


    # ino man ba ye harkate soski terekondam
    # ino ordo khani zade bara raftan az list vio be detail
    # miri jaye href a tameplate mizani{{product.get_absulot_url}}
    # def get_absolute_url(self):
    #     return f"/products/{self.id}/{self.title.replace(' ', '-')}"
