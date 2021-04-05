# '''
# views.py file contains 12 views
#     1. post_detail: for view post details
#     2. post_list: for all post on home page
#     3. post_by_category: for view post by category
#     4. post_by_tag: for view post by tags
#     5. post_new:  for create new post
#     6. post_edit: for edit already existing post
#     7. register: for register new user
#     8. logout_request: for logout logged in user
#     9. login_request: for login user
#     10. delete_post: for delete post
#     11. get_user_profile: for user account information
#     12. profile: for edit user profile
# '''


# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import logout, authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
# from django.shortcuts import redirect
# from django.utils import timezone
# from django.contrib import messages
from django.views.generic import TemplateView, ListView
# from .models import Post, Category, Comment
from .models import Country
import numpy as np
import random
# from .forms import PostForm, UserUpdateForm, ProfileUpdateForm
# from .forms import Create_new_user, CommentForm
# from taggit.models import Tag
# # from django.contrib.auth.models import
# from django.contrib.auth import get_user_model
# from django.conf import settings
# User = get_user_model()


# # from .models import Profile_update, Document
# # from .forms import UserUpdateForm, DocumentForm, UserCreation
# # from django.contrib.auth.forms import UserCreationForm


# def sign_up(request):
#     context = {}
#     form = UserCreationForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save()
#             auth.login(request, user)
#             return render(request, 'blog/post_list.html')
#     context['form'] = form
#     return render(request, 'blog/sign_up.html', context)


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return render(request, 'blog/post_list.html')
#     else:
#         return render(request, 'blog/login.html')


# def logout(request):
#     logout(request)
#     return render(request, 'blog/post_list.html')


# @login_required
# def userdetail(request, pk):
#     user = User.objects.get(pk=pk)
#     print(user.image, '1111111111')
#     # userimg=  Userprofile.objects.filter(user= request.user).first()
#     return render(request, 'blog/userdetail.html', {'user': user})


# # ############### post detail view ###############


# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True, parent__isnull=True)
#     new_comment = None
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             parent_obj = None
#             try:
#                 parent_id = int(request.POST.get('parent_id'))
#             except:
#                 parent_id = None
#             if parent_id:
#                 parent_obj = post.comments.get(id=parent_id)
#                 if parent_obj:
#                     replay_comment = comment_form.save(commit=False)
#                     replay_comment.parent = parent_obj
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'blog/post_detail.html',
#                   {'post': post,
#                    'comments': comments,
#                    'new_comment': new_comment,
#                    'comment_form': comment_form})


# # def delete_own_comment(request, slug):
# #     try:
# #         comment = post.comments.get(slug=comment.slug)
# #         comment.delete()
# #         return redirect('post_detail', slug=post.slug)
# #     except TypeError:
# #         return redirect('post_detail', slug=post.slug)
# #     return render(request, 'blog/post_detail.html', {'posts': posts})


# # ############### post list view ###############
# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('-published_date')

#     return render(request, 'blog/post_list.html', {'posts': posts})


# # ############### post list filtered by category ###############
# def post_by_category(request, category_slug):
#     category = Category.objects.get(slug=category_slug)
#     posts = Post.objects.filter(category__slug=category_slug)
#     context = {
#         'category': category,
#         'posts': posts
#     }
#     print(category)
#     return render(request, 'blog/post_by_category.html', context)


# # ############### post list filtered by tags ###############
# def post_by_tag(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     common_tags = Post.tags.most_common()[:4]
#     posts = Post.objects.filter(tags=tag)
#     context = {
#         'tag': tag,
#         'common_tags': common_tags,
#         'posts': posts,
#     }
#     return render(request, 'blog/post_by_tag.html', context)


# # ############### view for new post ###############
# @login_required
# def post_new(request):
#     if request.method == "POST":

#         form = PostForm(request.POST)

#         if form.is_valid():
#             print("Form is valid", 95162)
#             post = form.save(commit=False)
#             print(request.user, 'login userrrr')
#             post.auther = request.user
#             post.published_date = timezone.now()
#             post.save()
#             form.save_m2m()
#             return redirect('post_detail', slug=post.slug)
#     else:
#         form = PostForm(request.POST)
#     return render(request, 'blog/post_edit.html', {'form': form})


# # ############### view for edit post ###############
# def post_edit(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     query_pk_and_slug = True
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             Post.auther = request.user
#             post.published_date = timezone.now()
#             post.save()
#             form.save_m2m()
#             return redirect('post_detail', slug=post.slug)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})


# # ############### view for create new user ###############
# # def register(request):
# #     if request.method == "POST":
# #         form = Create_new_user(request.POST)
# #         if form.is_valid():

# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password1')
# #             user = authenticate(username=username, password=password)
# #             login(request, user)
# #             return redirect("/")
# #         else:
# #             messages.error(request, "Can Not Register.")

# #     else:
# #         form = Create_new_user()
# #     return render(request=request,
# #                   template_name="blog/register.html",
# #                   context={"form": form})


# # ############### view for logout user ###############
# # def logout_request(request):
# #     logout(request)
# #     messages.info(request, "Logged out successfully!")
# #     return redirect("/")


# # ############### view for user login ###############
# # def login_request(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(request=request, data=request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password')
# #             user = authenticate(username=username, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 messages.info(request, f"You are now logged in as {username}")
# #                 return redirect('account')
# #             else:
# #                 messages.error(request, "Invalid username or password.")
# #         else:
# #             messages.error(request, "Invalid username or password.")
# #     form = AuthenticationForm()
# #     return render(request=request,
# #                   template_name="polls/login.html",
# #                   context={"form": form})


# # ############### view for delete post ###############
# @login_required
# def delete_post(request, slug):
#     try:
#         posts = Post.objects.get(slug=slug)
#         query_pk_and_slug = True
#         posts.delete()
#         return redirect('account')
#     except TypeError:
#         return redirect('post_detail', slug=post.slug)
#     return render(request, 'blog/user_profile.html', {'posts': posts})


# # ############### view for get account information ###############
# @ login_required
# def get_user_profile(request):
#     posts = Post.objects.filter(
#         auther=request.user, published_date__lte=timezone.now()).order_by('-published_date')

#     user = User.objects.get(username=request.user)
#     return render(request, 'blog/user_profile.html', {"user": user, 'posts': posts})


# # ############### view for update user profile ###############
# @ login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             profile = p_form.save(commit=False)
#             if 'image' in request.FILES:
#                 profile.image = request.FILES['image']
#             profile.save()

#             messages.success(request, f'Your account has been updated!')
#             return redirect('account')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,

#     }

#     return render(request, 'blog/profile_edit.html', context)


def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class SearchResultsView(ListView):
    model = Country
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Country.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


def rand_lst():
    data = np.random.randint(1, 50, size=87)
    my_list = data.tolist()
    return my_list


def func(lst):
    u_list = list(set(lst))
    return u_list


def main(request):
    r_list = rand_lst()
    u_lst = func(r_list)
    sec_list = list(map(lambda x: x+15, u_lst))
    odd_list = list(filter(lambda x: (x % 2 != 0), sec_list))
    even_list = list(filter(lambda x: (x % 2 == 0), sec_list))
    sum_of_odd = sum(map(lambda x: x, odd_list))
    sum_of_even = sum(map(lambda x: x, even_list))
    sum_of_all = sum(map(lambda x: x, sec_list))
    # print("List after adding 15 to each elements: ", sec_list)
    # print("List of odd numbers: ", odd_list)
    # print("List of even numbers: ", even_list)
    # print("Sum of odd numbers: ", sum_of_odd)
    # print("Sum of even numbers: ", sum_of_even)
    # print("Sum of all numbers: ", sum_of_all)
    return render(request, 'blog/list.html', {'r_list': r_list, 'u_lst': u_lst, 'sec_list': sec_list, 'odd_list': odd_list, 'even_list': even_list, 'sum_of_odd': sum_of_odd, 'sum_of_even': sum_of_even, 'sum_of_all': sum_of_all})
