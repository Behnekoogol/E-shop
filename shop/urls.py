from django.urls import path
from .import views


urlpatterns = [
    path('', views.product_list,name='home'),
    path('category/<int:category_id>/', views.Products.as_view(),name='products'),
    path('<int:pk>', views.Single.as_view(), name='single'),
    path('about.html', views.About),
    path('contact.html', views.Contact),

]
