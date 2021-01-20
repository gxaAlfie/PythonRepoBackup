# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# tells admin to display publication date before question text
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# admin.StackedInline => Provides Choice model form below question form. Each field of Choice is a new line
# admin.TabularInline => Provides Choice model form below question form. Each field is a different column in a table format
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# tells admin to separate fields into panels similiar to active admin
# first field indicates panel title if provided
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # by default Django display the str() of each object. To customize that add list_display.
    list_filter = ['pub_date']  # adds a filter at the side for this field
    search_fields = ['question_text']   # adds search function where provided fields is what it searches for

    # tells admin to separate fields into panels similiar to active admin
    # first field indicates panel title if provided
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

    # adds an inline item for the model. Good for items that need this as foreign key
    inlines = [ChoiceInline]

# tells admin that some model (i.e. Choice, Question) has an admin interface
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
