"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


#app_name = "core"

urlpatterns = [
    path("", include("core.urls", namespace="core") ), 
#   path("", include("users.urls", namespace="users") ), 
#   path("", include("rooms.urls", namespace="rooms") ), 
    path("admin/", admin.site.urls),
]



#장고에게 어떻게 파일을 제공하는지 가르치는 것 (media_url 과 media_root 연결)
#production mode / development mode
url_development = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
      urlpatterns += url_development