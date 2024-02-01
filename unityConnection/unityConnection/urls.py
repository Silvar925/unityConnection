from django.contrib import admin
from django.urls import path, include
from Users.urls import urlpatternsUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatternsUsers)),
]
