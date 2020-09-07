from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home),
    path('song/', views.search),
    path('playlist/', views.playlist),
    path('album/', views.album),
    path('lyrics/', views.lyrics),
    path('result/', views.result),
]