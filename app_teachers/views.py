from rest_framework import viewsets

from .serializers import TeacherSerializer
from .models import BestTeachers


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = BestTeachers.objects.all()


# class SubjectViewSet(viewsets.ModelViewSet):
#     serializer_class = SubjectSerializer
#     queryset = Subject.objects.all()
