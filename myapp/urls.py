from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, StatusViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
