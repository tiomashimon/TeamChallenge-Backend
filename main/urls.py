
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import hello_world # temporary
from django.views.generic import TemplateView


schema_view = get_schema_view(
    openapi.Info(
        title="TeamChallenge",
        default_version='v1',
        description="API for TeamChallenge",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/test/hello-world', hello_world), # temporary
    # path('home/', TemplateView.as_view(template_name='tmplt.html'), name ='home')
    path('accounts/', include('allauth.urls')),
]
