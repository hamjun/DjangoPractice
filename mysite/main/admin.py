from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
# put stuff in here to see stuff on the admin site
admin.site.register(ToDoList)
admin.site.register(Item)