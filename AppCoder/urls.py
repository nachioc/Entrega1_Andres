from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
   
    # URLs de Mascotas
    path('acerca_de_mi/', views.mascota, name="acerca_de_mi"),
    
    # URLs de Profesiones
    path('foro/', views.profesion, name="foro"),
    path('crear-profesion/', views.crear_profesion, name="crear_profesion"),
    path('editar-profesion/<int:id>/', views.editar_profesion, name="editar_profesion"),
    path('eliminar-profesion/<int:id>/', views.eliminar_profesion, name="eliminar_profesion"),
   
    # URLs de BLogs
    path('index/', views.familiar, name="index"),
    path ('',views.insertPost ,name='insertUrl'),
    path('post/<str:pk>/', views.post, name="post"),
    path ('edit/<str:pk>',views.editPost ,name='editUrl'),
    
    #URLs de usuario
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
     path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
    #URLs de login
    path('register', views.register, name = 'register'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
]
