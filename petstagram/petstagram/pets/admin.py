from django.contrib import admin

from petstagram.pets.models import Pet

#admin.site.register(Pet)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
