from django.contrib import admin
from MyStreet.models import Street, Comment
from MyStreet.models import UserProfile


class CommentAdmin(admin.ModelAdmin):
    list_display = ('street', 'user', 'comment')


# Add in this class to customized the Admin Interface
class StreetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Street, StreetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)