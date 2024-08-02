from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uni/', include('app.university.urls')),
    path('auth/', include('app.custom_auth.urls')),
]
