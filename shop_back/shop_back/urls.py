from django.contrib import admin
from django.urls import path, include  # Убедись, что здесь есть path и include
from django.http import HttpResponse

# Функция для главной страницы (чтобы не было 404)
def home(request):
    return HttpResponse("<h1>Welcome to the Shop API</h1><p>Use /api/products/ for seeing products.</p>")

urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
