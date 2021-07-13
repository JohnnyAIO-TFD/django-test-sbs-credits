from django.urls import path, include
from . import views

urlpatterns = [
    # Urls de la solicitud del credito
    path('crear/', views.creditos_form, name="creditos_insert"),
    path('actualizar/<int:id>', views.creditos_form, name='creditos_update'),
    path('eliminar/<int:id>/', views.creditos_eliminar, name="creditos_eliminar"),
    path('', views.creditos_list, name="creditos_list"),
    # Urls del Cliente
    path('cliente/crear/', views.clientes_form, name="clientes_insert"),
    path('cliente/actualizar/<int:id>',
         views.clientes_form, name='clientes_update'),
    path('cliente/eliminar/<int:id>/',
         views.clientes_delete, name="clientes_delete"),
    path('cliente/', views.clientes_list, name="clientes_list"),

]
