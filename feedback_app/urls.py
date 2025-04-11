from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]
