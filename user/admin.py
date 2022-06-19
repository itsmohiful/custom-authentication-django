from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserUpdateForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserUpdateForm
    add_form = UserCreationForm


    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    """
        The fields to be used in displaying the User model.
        These override the definitions on the base UserAdmin
        that reference specific fields on auth.User.
    """

    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('permissions', {'fields': ('is_admin',)}),
    )

    """
        add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
        overrides get_fieldsets to use this attribute when creating a user.
    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    search_fields = ('email','username',)
    ordering = ('username','email',)
    filter_horizontal = ()


#register UserAdmin
admin.site.register(User, UserAdmin)
