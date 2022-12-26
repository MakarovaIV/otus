from django.db import models

# Category - vegetables, fruits, meat, drinks
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


# Item - tomatoes, apples, pork, lemonade
class Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
    desc = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class User(models.Model):
    first_name = models.CharField(max_length=64, unique=False)
    last_name = models.CharField(max_length=64, unique=False)
    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

