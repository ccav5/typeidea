
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target','content','nickname','content','website','created_time')



# Register your models here.
