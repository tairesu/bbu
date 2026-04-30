from django.contrib import admin
from directory.models import (
    Category,
    Business,
    Support,
    BusinessImage, 
    Featured
)


admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Support)
admin.site.register(BusinessImage)
admin.site.register(Featured)
