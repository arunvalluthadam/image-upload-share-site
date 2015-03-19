from django.contrib import admin
from .models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ('image',)
	# search_fields = ['image']

admin.site.register(Item, ItemAdmin)


class CommentsAdmin(admin.ModelAdmin):
	model = Comments
	list_display = ('item','name','email','content')
	# search_fields = ['image']

admin.site.register(Comments, CommentsAdmin)