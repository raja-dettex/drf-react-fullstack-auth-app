
from django.contrib import admin
from django.urls import path, include
from .views import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui')
]
