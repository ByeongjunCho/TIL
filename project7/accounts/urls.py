from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.userlist, name='userlist'),
    path('<int:account_pk>', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('<int:account_pk>/follow/', views.follow, name='follow'),
]
