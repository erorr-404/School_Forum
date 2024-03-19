from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.PostLike)
admin.site.register(models.PostDisLike)
admin.site.register(models.Comment)