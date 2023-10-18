from django.contrib import admin
from django.urls import path
from product import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/category/', views.category_list_api_view),
    path('api/v1/category/<int:id>/', views.category_detail_api_view),

    path('api/v1/products/', views.product_list_api_view),
    path('api/v1/products/<int:id>/', views.product_derail_api_view),

    path('api/v1/review/', views.review_list_api_view),
    path('api/v1/review/<int:id/>', views.review_detail_api_view),

]
