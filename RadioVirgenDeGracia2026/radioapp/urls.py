from django.urls import path
from . import views

urlpatterns = [

    path('obtenerCancion/<int:id>', views.get_cancion),
    path('addCancion/', views.add_cancion),
    path('obtenerCanciones/',views.get_canciones)


]