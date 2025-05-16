"""
URL configuration for backend project.

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

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

#sets paths for urls and folders


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/menu/", include("backend.menu.urls")),
    path('api/flight-tracker/', include('backend.flight_tracker.urls')),
    path('api/ticketing/', include('backend.ticketing.urls')),
    path('api/information-hub/', include('backend.information_hub.urls')),
    path('api/check-in/', include('backend.check_in.urls')),
    path('api/profiles/', include('backend.profiles.urls')),
    path('api/benefits/', include('backend.benefits.urls')), 
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]
