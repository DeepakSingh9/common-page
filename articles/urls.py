from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.articles_list,name='articles_list'),
             url(r'^login/$',views.User_login,name='login'),
             url(r'^logout/$',views.User_Logout,name='logout'),
             url(r'^addpost/$',views.AddPost,name='add_post'),
             ]