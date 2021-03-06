"""
Company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2./topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include

from {{ project_name | lower }}.api.views import \
    {{ project_name | capfirst}}ResourceViewSet, \
    {{ project_name | capfirst }}ResourceSearchViewSet, \
    {{ project_name | capfirst }}ResourceGEOSearchViewSet

from rest_framework import routers

# API v1 Router. Provide an easy way of automatically determining the URL conf.

api_{{ project_name | upper }} = routers.DefaultRouter()

if settings.DSE_SUPPORT:
    api_{{ project_name | upper }}.register(r'{{ project_name | lower }}/search',
                            {{ project_name | capfirst }}ResourceSearchViewSet,
                            base_name="{{ project_name | lower }}-search")

    api_{{ project_name | upper }}.register(r'{{ project_name | lower }}/search/facets',
                            {{ project_name | capfirst }}ResourceSearchViewSet,
                            base_name="{{ project_name | lower }}-search-facets")

    api_{{ project_name | upper }}.register(r'{{ project_name }}/geosearch',
                            {{ project_name | capfirst }}ResourceGEOSearchViewSet,
                            base_name="{{ project_name | lower }}-geosearch")

api_{{ project_name | upper }}.register(r'{{ project_name }}',
                        {{ project_name | capfirst }}ResourceViewSet,
                        base_name="{{ project_name | lower }}")

urlpatterns = [
    # Company API version
    url(r'^', include(api_{{ project_name | upper }}.urls), name="{{ project_name | lower }}-api"),
]
