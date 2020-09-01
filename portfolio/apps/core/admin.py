from django.contrib import admin

from .models import Category, Information, Work, Cv

admin.site.register(Category)
admin.site.register(Information)
admin.site.register(Work)
admin.site.register(Cv)
