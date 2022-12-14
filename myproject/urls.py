"""myproject URL Configuration

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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

from .apps.core.views import frontpage


urlpatterns = i18n_patterns(
    path('',frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path("webpage/", include(("myproject.apps.webpage.urls", "webpage"), namespace="webpage")),
    path("store/", include(("myproject.apps.store.urls", "store"), namespace="store")),
    path("cart/", include(("myproject.apps.cart.urls", "cart"), namespace="cart")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)