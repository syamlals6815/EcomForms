from django.urls import path
from .views import (home, category_list, edit_category, delete_category, add_product,
                    edit_product,delete_product,sign_out)

app_name = 'adminpanel'
urlpatterns = [
    path('', home, name ='home'),
    path('category_list/', category_list, name ='category_list'),
    path('edit_category/<int:category_id>/', edit_category, name = 'edit_category'),
    path('delete_category/<int:category_id>/', delete_category, name = 'delete_category'),
    path('add_product/<int:category_id>/', add_product, name = 'add_product'),
    path('edit_product/<int:product_id>/', edit_product, name = 'edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name = 'delete_product'),
    path('logout/',sign_out,name='sign_out')

]