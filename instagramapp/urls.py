"""instagramapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth import views as auth_views
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('signup',views.signup,name='signup'),
    path('accounts/profile/',views.myview),
    path('topprofile',views.profile),
    path('myfollowing',views.myfollowing),
    path('myfollowers',views.myfollowers),
    path('accounts/profile/<str:username>',views.reqprofile),
    path('accounts/profile/<str:username>/following',views.following),
    path('accounts/profile/<str:username>/followers',views.followers),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL2,document_root=settings.MEDIA_ROOT)