from django.urls import path
from . import views
app_name='shap'

urlpatterns = [
    path('',views.allproductcategory,name='allproductcategory'),
    path('<slug:c_slug>/',views.allproductcategory,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetails,name='productcategory'),
]