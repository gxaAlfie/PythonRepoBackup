# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from item_inventory.models import Container, Item

admin.site.register(Container)
admin.site.register(Item)

# Register your models here.
