from django.contrib import admin
from .models import Post, Tag, Activity, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'status', 'created', 'updated',)


class CommentAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class ActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Activity, ActivityAdmin)
