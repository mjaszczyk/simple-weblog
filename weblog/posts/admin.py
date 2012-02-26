from __future__ import absolute_import

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title', 'create_time', 'author')
    list_filter = ('create_time', 'update_time')
    search_fields = ('title', 'content')

    def queryset(self, request):
        """ queryset method overwritten to filter posts for current user """
        queryset = super(PostAdmin, self).queryset(request)
        # Superuser can see all users posts
        if not request.user.is_superuser:
            queryset = queryset.filter(author=request.user)
        return queryset

    def save_form(self, request, form, change):
        """ save_form method overwritten to set current user as post author on object creation """
        obj = super(PostAdmin, self).save_form(request, form, change)
        if not change or not obj.author:
            obj.author = request.user
        return obj

admin.site.register(Post, PostAdmin)
