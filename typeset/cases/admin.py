from django.contrib import admin

# Register your models here.
from .models import Case, Block

class BlockInline(admin.StackedInline):
    model = Block
    extra = 73

class CaseAdmin(admin.ModelAdmin):
    inlines = (BlockInline,)

admin.site.register(Case, CaseAdmin)
