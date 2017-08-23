from django.contrib import admin
from .models import Family_Names, Calamities, Profession, Supplies

# Register your models here.
admin.site.register(Family_Names)
admin.site.register(Calamities)
admin.site.register(Profession)
admin.site.register(Supplies)