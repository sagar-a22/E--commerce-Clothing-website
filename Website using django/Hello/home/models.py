from django.db import models

# makemigration- create changes and store in a file
# migrate- apply the pending changes created by makemigrations

# Create your models here.

class Contact(models.Model):
      name= models.CharField(max_length=100)
      address= models.CharField(max_length=100)
      email= models.TextField()
      phone= models.CharField(max_length=50)

      def __str__(self):
            return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name




