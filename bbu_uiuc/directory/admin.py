from django.contrib import admin
from directory.models import (
    Category,
    Business
)


admin.site.register(Category)
admin.site.register(Business)
