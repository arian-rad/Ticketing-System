from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields"""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username',)


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user
    """
    password = ReadOnlyPasswordHashField(help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


    add_fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'password1', 'password2')}),
    )

