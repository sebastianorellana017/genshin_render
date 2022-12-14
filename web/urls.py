"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from miapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('miapp.urls','miapp'), namespace='miapp')),
    path('nopor/', views.nopor, name='nopor'),
    path('categoria/<int:category_id>', views.category, name="category"),
    path('article/<int:article_id>', views.article, name="article"),
    path('userpage/', views.userpage, name="userpage"),
    path('crear/', views.crear, name="crear"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('borrar/<int:id>', views.borrar, name="borrar"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ruta imagenes
#if settings.DEBUG:
#    from django.conf.urls.static import static
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
