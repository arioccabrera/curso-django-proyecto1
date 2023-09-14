"""
URL configuration for CursoDjango2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.http import HttpResponse esto ya lo puedo eliminar porque ahora estar en el archivo views.py de la APP
#eliminé las funciones que antes estaban aquí y ahora le digo que las importe del directorio de la APP y que estan en views.py
#from recipes.views import home, contato, sobre . esto lo puedo eliminar porque voy a usar el recurso include de django.urls para
#llamar a las funciones desde la APP


urlpatterns = [
    #siempre acaba con '/', ejemplo, 'admin/' pero nunca '/admin/'
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
