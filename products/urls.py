from django.urls import path
from .views import ( 
    product_detail_view, 
    product_create_view, 
    render_initial_data, 
    product_delete_view,
    product_list_view,
    product_update_view,
    dynamic_lookup_view
    )

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='create'),
    path('<int:id>', dynamic_lookup_view, name='Product-detail'),
    path('<int:id>/update/', product_update_view, name='Product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('product/', product_detail_view, name='Specific Product'),
]