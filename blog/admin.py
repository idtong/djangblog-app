from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    #list_display = ['id','title']
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']

    def count_text(self,post):
        return '{}글자'.format(len(post.content))

    count_text.short_description = "내용글자수"


# Post 를 admin 사이트에 등록
admin.site.register(Post, PostAdmin)