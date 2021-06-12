from django.contrib import admin

from .models import DocumentType,City, User

admin.site.register(DocumentType)
admin.site.register(City)
admin.site.register(User)