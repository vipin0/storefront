from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet, basename='collection')
router.register('carts', views.CartViewSet, basename='cart')
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('orders', views.OrderViewSet, basename='order')

review_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
review_router.register('reviews', views.ReviewViewSet,
                       basename='product-review')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + review_router.urls + carts_router.urls

# urlpatterns = [
#     path('products/',views.product_list),
#     path('products/<int:pk>',views.product_detail),
#     path('collections/',views.collection_list),
#     path('collections/<int:pk>',views.collection_detail),
# ]
