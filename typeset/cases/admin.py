from django.contrib import admin
from django.conf.urls import url, include

# Register your models here.
from .models import Case, Block

class BlockInline(admin.StackedInline):
    model = Block
    extra = 73
    class Media:
        js = ['js/charlist.js']

class CaseAdmin(admin.ModelAdmin):
    inlines = (BlockInline,)



admin.site.register(Case, CaseAdmin)

