# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
