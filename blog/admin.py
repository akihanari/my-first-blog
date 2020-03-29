from django.contrib import admin
from .models import Post, Comment

from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
