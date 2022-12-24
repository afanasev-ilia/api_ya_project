from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.apps import ApiConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace=ApiConfig.name)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc',
    ),
]
