from django.contrib import admin
from django.urls import path, include
from users.views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('', include('dashboard.urls')),
]
