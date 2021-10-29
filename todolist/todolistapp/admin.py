from django.contrib import admin
from .models import Task, Collections, Enrollment

# Register your models here.

admin.site.register(Task)
admin.site.register(Collections)
admin.site.register(Enrollment)
