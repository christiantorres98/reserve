from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from jet.views import model_lookup_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Reserve Api",
        default_version="v1",
        description="Reserve Api, desarrollado por Christian Torres",
        contact=openapi.Contact(email="christiantorrescruz5@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('jet/model_lookup/', model_lookup_view, name='model_lookup'),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/users/', include(('users.urls', 'users'), namespace='users')),
    path('api/', include(('drivers.urls', 'drivers'), namespace='drivers')),
    re_path(
        route=r'^swagger(?P<format>\.json|\.yaml)$',
        view=schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        route=r'^swagger/$',
        view=schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        route=r'^redoc/$',
        view=schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

urlpatterns = urlpatterns + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
