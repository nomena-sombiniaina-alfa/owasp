from django.contrib import admin
from django.urls import path, include
from idor.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('idor/', include('idor.urls')),
    path('', home, name='home'),
]
