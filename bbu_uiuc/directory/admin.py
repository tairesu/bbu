from django.contrib import admin
from directory.models import (
    Category,
    Business,
    Support
)


admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Support)
