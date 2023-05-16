from django.contrib import admin

# Register your models here.
from .models import post ,Author

class PostAdmin(admin.ModelAdmin):
    list_display=['title' ,'author','publish_date']
    list_filter=['author','tags','publish_date']
    search_fields= ['title','content']


admin.site.register(post)
admin.site.register(Author)