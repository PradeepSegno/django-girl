from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path('', views.IndexView.as_view(), name='index'),
]
