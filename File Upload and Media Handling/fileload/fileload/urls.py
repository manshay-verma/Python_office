"""
URL configuration for fileload project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from hostel.views import upload_file, success, search_image, home
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('upload/', upload_file, name='upload'),
    path('success/', success, name='success'),
    path('search/', search_image, name='search_image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)