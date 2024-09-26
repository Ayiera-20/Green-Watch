"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from green_watch import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('login/', views.login_page, name='login'),
    path('recycle_center/', views.recycleCenter, name='recycle_center'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact'),
    path('login/submit/', views.sign_in_submit, name='sign_in_submit'),
    path('logout/', views.logout_view, name='logout'),
    path('submit-report/', views.submit_report, name='submit_report')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
