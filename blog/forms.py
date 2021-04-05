'''
forms.py contains five form
    1. PostForm: for new Post
    2. CommentForm: for comment
    3. Create_new_user: for create new user
    4. UserUpdateForm: for update user's information
    5. ProfileUpdateForm: for update user's image
'''


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Profile, Comment
from .models import User
from django.conf import settings


# from .models import Profile_update, Document
# from .models import NewPost


# ############### form for new post starts here ###############


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tags')


# ############### form for comment starts here ###############


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# ############### form for new user starts here ###############


class Create_new_user(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['mobile', 'gender',
                  'dob', 'image', 'role']

        def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:

            self.fields['city'].queryset = self.instance.country.city_set.order_by(
                'name')


# ############### form for user profile update starts here ###############


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


# ############### form for update user's image and gender ###############


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image',  'gender']
