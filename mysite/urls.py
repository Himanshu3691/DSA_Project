from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings  
from . import views



urlpatterns = [
    path("", views.index, name ="index"),
    path("dsa/", include("dsa.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)