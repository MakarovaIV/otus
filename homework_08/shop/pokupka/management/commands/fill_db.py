from django.core.management.base import BaseCommand, CommandError
from pokupka.models import Category, Item


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Item.objects.all().delete()

        meat_category = Category.objects.create(name='Meat')
        meat_category.save()
        pork = Item.objects.create(name='Pork', category=meat_category, desc='Pork is classified a red meat because it contains more myoglobin than chicken or fish. When fresh pork is cooked, it becomes lighter in color, but it is still a red meat. Pork is classed as "livestock" along with veal, lamb, and beef. All livestock are considered red meat.')
        pork.save()


        fruit_category = Category.objects.create(name='Fruits')
        fruit_category.save()
        apple = Item.objects.create(name='Golden Delicious', category=fruit_category, desc='Golden Delicious is a large, yellowish-green skinned cultivar and very sweet to the taste. It is prone to bruising and shriveling, so it needs careful handling and storage. It is a favorite for salads, apple sauce, and apple butter.')

        apple.save()

        vegetables_category = Category.objects.create(name='Vegetables')
        vegetables_category.save()
        potatoes = Item.objects.create(name='Potatoes', category=vegetables_category, desc='Red potatoes are small to medium in size and are round or oval with a somewhat uniform shape. The thin skin is ruby to deep red and is smooth with some light brown speckling, spots, and indentations. There are also a few medium-set eyes found across the surface of the skin. The flesh is crisp, white, and firm.')
        potatoes.save()

        drink_category = Category.objects.create(name='Drinks')
        drink_category.save()
        lemonade = Item.objects.create(name='Lemonade', category=drink_category, desc='Lemonade is a sweetened beverage made from lemons, sugar, and water. It is popular in the United States during the spring and summer, when it is generally served chilled with ice. In some countries, the word lemonade is also used to describe any clear carbonated drink; in others, it means any fruit-flavored soda.')
        lemonade.save()