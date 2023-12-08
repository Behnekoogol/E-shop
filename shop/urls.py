from django.urls import path
from .import views


urlpatterns = [
    path('', views.product_list),
    path('product.html', views.product),
    path('<int:pk>', views.Single.as_view(), name='single'),
    path('about.html', views.About),
    path('contact.html', views.Contact),

]
