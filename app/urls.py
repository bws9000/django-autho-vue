from catalog import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private)
]
