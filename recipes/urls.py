from django.urls import path
#from django.http import HttpResponse esto ya lo puedo eliminar porque ahora estar en el archivo views.py de la APP
#eliminé las funciones que antes estaban aquí y ahora le digo que las importe del directorio de la APP y que estan en views.py
from recipes.views import home, contato, sobre


urlpatterns = [
    #siempre acaba con '/', ejemplo, 'admin/' pero nunca '/admin/'
    path('', home),
    path('sobre/', sobre),
    path('contato', contato)
]
