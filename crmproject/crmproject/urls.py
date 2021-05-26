from django.contrib import admin
from django.urls import path,include
from crmproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crmapp.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documemt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documemt_root=settings.MEDIA_ROOT)
