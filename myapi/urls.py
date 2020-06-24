from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('myapi/', views.userList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('adduser/', views.UserView,name='add'),
    path('adddata/', views.AddView),
    path('alluser/', views.AllUserView),
    path('', views.home, name='home')

]