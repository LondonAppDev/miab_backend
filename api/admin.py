from django.contrib import admin
# Import our models module.
from . import models

# Register our "Message" model with the Django Admin/
admin.site.register(models.Message)
