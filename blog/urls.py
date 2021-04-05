'''
urls.py file create contains all url belong to blog app
'''


from django.urls import path
from . import views


urlpatterns = [
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<str:slug>/', views.post_detail, name='post_detail'),
    # path('category/<category_slug>/',
    #  views.post_by_category, name='post_by_category'),
    # path('tag/<str:slug>', views.post_by_tag, name='post_by_tag'),
    # path('delete/<str:slug>', views.delete_post, name='delete'),
    # path("register/", views.sign_up, name="register"),
    # path("account/", views.userdetail, name="account"),
    # path("profile_update/", views.profile, name="profile_update"),
    # path("logout", views.logout, name="logout"),
    # path("login", views.login, name="login"),
    # path('', views.post_list, name='post_list'),
    path('list/', views.main, name='main'),

]
