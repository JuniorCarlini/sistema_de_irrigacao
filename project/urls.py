from django.contrib import admin
from django.urls import path, include
from users.views import login_view , about_view
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('about/', about_view , name='about'),
    path('', include('dashboard.urls')),
    path('', include('sensors.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)