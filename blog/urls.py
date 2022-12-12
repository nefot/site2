
from django.urls import path
from . import views


urlpatterns = [


    path('', views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('edit-page',views.editp, name= "edit_page"),
    path('register',views.register, name= "register"),
    path('login',views.login, name= "login"),

]
