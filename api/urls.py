from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name='apiOverview'),
	path('users/', views.users_list, name='users'),
	path('users/<str:id>/', views.user_detail, name='user-detail'),

]
