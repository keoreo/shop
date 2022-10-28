from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField, ModelForm
from PIL import Image


class NotebookAdminForm(ModelForm):

    MIN_RESOLUTION = (400, 400)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображение с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        print(img.width, img.height)
        return image


'''
class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass
'''


class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

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
'''
# регистрация модели (она не обязательна)
admin.site.register(SomeModel)
'''