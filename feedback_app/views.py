from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg, Count
from rest_framework.permissions import IsAuthenticated
from .models import Course, Feedback
from .serializers import CourseSerializer, FeedbackSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to view aggregated analytics data
    @action(detail=False, methods=['get'], url_path='analytics')
    def analytics(self, request):
        data = (
            Feedback.objects
            .values('course__name')
            .annotate(avg_rating=Avg('rating'), total=Count('id'))
            .order_by('course__name')
        )
        return Response(data, status=status.HTTP_200_OK)
