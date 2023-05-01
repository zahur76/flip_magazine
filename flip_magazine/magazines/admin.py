from django.contrib import admin

from .models import Magazines

# Register your models here.


class MagazinesAdmin(admin.ModelAdmin):
    # Admin display
    list_display = ("name",)


# The model followed by class name (model, class name)
admin.site.register(Magazines, MagazinesAdmin)
