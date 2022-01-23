from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='product')
router.register('collections',views.CollectionViewSet,basename='collection')

review_router = routers.NestedDefaultRouter(router,'products',lookup='product')
review_router.register('reviews',views.ReviewViewSet,basename='product-review')

urlpatterns = router.urls + review_router.urls
# urlpatterns = [
#     path('products/',views.product_list),
#     path('products/<int:pk>',views.product_detail),
#     path('collections/',views.collection_list),
#     path('collections/<int:pk>',views.collection_detail),
# ]
