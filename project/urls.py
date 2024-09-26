from django.contrib import admin
from django.urls import path, include
from users.views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('', include('dashboard.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]
