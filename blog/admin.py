from django.contrib import admin
from .models import Post, Category, Comment
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, Country, City
from django.conf import settings


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')


class CustomUserAdmin(UserAdmin):
    ordering = ('-id',)
    list_display_links = ('username', 'mobile')
    list_display = ['username', 'email', 'mobile',
                    'gender', 'first_name', 'last_name', 'role']
    search_fields = ['username', 'email', 'mobile',
                     'gender', 'first_name', 'last_name', 'role']
    # add_fieldsets = (
    # 	(None, {
    # 		'classes': ('wide', 'extrapretty'),
    # 		'fields': ('first_name', 'last_name', 'email', 'mobile', 'username', 'password1', 'password2' ),
    # 	}),
    # )
    fieldsets = [
        (None, {'fields': ('email', 'username', 'mobile',
                           'first_name', 'last_name', 'password',)}),
        ('Personal info', {'fields': ('role', 'gender')})]


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Country)
admin.site.register(City)
