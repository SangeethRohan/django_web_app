"""
URL configuration for django_web_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from pages.views import home_view, contact_view, social_view, about_view
from products.views import ( 
    product_detail_view, 
    product_create_view, 
    render_initial_data, 
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    product_update_view
    )

urlpatterns = [
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('', home_view, name='Home'),
    path('admin/', admin.site.urls),
    path('home/', home_view, name='Home'),
    path('contact/', contact_view, name='Contact'),
    path('social/', social_view, name='Social'),
    path('about/', about_view, name='About'),
      
]
