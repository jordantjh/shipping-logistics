"""logistics_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from . import views as rootViews

### Media settings ###
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

urlpatterns = [
    path('', include('service_providers.urls', namespace='sp')),
    path('login/', rootViews.loginView, name="login"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html',success_url=reverse_lazy('sp:passwordchanged')), name="change_pass"),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='passdone'),
    path('logoff', rootViews.logoffView, name="logoff"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
