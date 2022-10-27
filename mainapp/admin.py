from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField


'''
class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass
'''


class NotebookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebook'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


'''
class SmartphoneCategoryChoiceField(forms.ModelChoiceField):
    pass
'''


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CardProduct)
admin.site.register(Cart)
admin.site.register(Castomer)

