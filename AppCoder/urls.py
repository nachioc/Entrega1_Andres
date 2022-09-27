from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
   
    # URLs de Cursos
    path('mascota/', views.mascota, name="mascota"),
    path('crear-mascota/', views.crear_mascota, name="crear_mascota"),
    path('busqueda-mascota-form/', views.busqueda_mascota, name="busqueda_mascota_form"),
    path('busqueda-mascota/', views.buscar_mascota, name="busqueda_mascota"),
    
    # URLs de Profesores
    path('profesion/', views.profesion, name="profesion"),
    path('crear-profesion/', views.crear_profesion, name="crear_profesion"),
    path('editar-profesion/<int:id>/', views.editar_profesion, name="editar_profesion"),
    path('eliminar-profesion/<int:id>/', views.eliminar_profesion, name="eliminar_profesion"),
   
    # URLs de Familiares
    path('familiar/', views.FamiliarListView.as_view(), name="familiar"),
    path('crear-familiar/', views.FamiliarCreateView.as_view(), name="crear_familiar"),
    path('editar-familiar/<int:pk>/', views.FamiliarUpdateView.as_view(), name="editar_familiar"),
]
