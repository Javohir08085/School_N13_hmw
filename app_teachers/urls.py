from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet

router = DefaultRouter()

router.register(r'teacher',TeacherViewSet,basename='teacher')
# router.register(r'subject',SubjectViewSet,basename='lesson')

urlpatterns = [

] + router.urls
