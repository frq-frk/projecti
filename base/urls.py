from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name = 'home'),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name = 'base/login.html'),name = 'login'),
	re_path(r'^logout/$',auth_views.LogoutView.as_view(),name = 'logout'),
    re_path(r'updatestatus/(?P<pk>\d+)/$',views.updatestatus,name = 'updatestatus'),
    re_path(r'usertaskstatus/(?P<id>\d+)/$',views.usertaskstatus,name = 'usertaskstatus'),
]