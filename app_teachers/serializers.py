from rest_framework.serializers import ModelSerializer

from .models import BestTeachers

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = BestTeachers
        fields = '__all__'

# class SubjectSerializer(ModelSerializer):
#     model = Subject
#     fields = '__all__'