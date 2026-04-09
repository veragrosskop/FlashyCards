from django.contrib import admin
from .models import Deck, Card, HierarchyItem

admin.site.register(HierarchyItem)
admin.site.register(Deck)
admin.site.register(Card)
