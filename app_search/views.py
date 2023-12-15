from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from app_pages.models import Documents
from app_pages.serializers import DocumentsSerializer

from app_teachers.models import BestTeachers
from app_teachers.serializers import TeacherSerializer

from app_piar.models import News,Anons,Vacancy,PhotoGallery,VideoGallery
from app_piar.serializers import (
    NewsSerializer,AnonsSerializer,
    VacancySerializer,PhotoGallerySerializer,
    VideoGallerySerializer,
)
from app_search.serializers import UniversalSearchSerializer

from collections import namedtuple

UniversalSearch = namedtuple('UniversalSearch',
                             ('news','anons','docs','vacancy','photos','videos','teachers'))
class UniversalSearchView(ListAPIView):
    def get_serializer_class(self):
        return UniversalSearchSerializer

    def list(self,request,*args, **kwargs):
        if 'keyword' in self.request.GET and 'where' in self.request.GET:
            key_model = self.request.GET['where']
            key_word = self.request.GET['keyword']

            if key_model == 'news':
                search_results = UniversalSearch(
                    news=News.objects.filter(news_title_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    docs=Documents.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    videos=VideoGallery.objects.none(),
                    teachers=BestTeachers.objects.none(),
                    # subject=Subject.objects.none(),
                )
            elif key_model == 'anons':
                search_results = UniversalSearch(
                    anons=Anons.objects.filter(anons_title_uz__icontains=key_word),
                    news=News.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    docs=Documents.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    videos=VideoGallery.objects.none(),
                    teachers=BestTeachers.objects.none(),
#                     subject=Subject.objects.none(),
                )
            elif key_model == 'vacancy':
                search_results = UniversalSearch(
                    vacancy=Vacancy.objects.filter(vacancy_name_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    news=News.objects.none(),
                    docs=Documents.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    videos=VideoGallery.objects.none(),
                    teachers=BestTeachers.objects.none(),
#                     subject=Subject.objects.none(),
                )
            elif key_model == 'docs':
                search_results = UniversalSearch(
                    docs=Documents.objects.filter(doc_title_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    news=News.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    videos=VideoGallery.objects.none(),
                    teachers=BestTeachers.objects.none(),
#                     subject=Subject.objects.none(),
                )
            elif key_model == 'photos':
                search_results = UniversalSearch(
                    photos=PhotoGallery.objects.filter(gallery_title_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    docs=Documents.objects.none(),
                    news=News.objects.none(),
                    videos=VideoGallery.objects.none(),
                    teachers=BestTeachers.objects.none(),
#                     subject=Subject.objects.none(),
                )
            elif key_model == 'videos':
                search_results = UniversalSearch(
                    videos=VideoGallery.objects.filter(gellery_title_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    docs=Documents.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    news=News.objects.none(),
                    teachers=BestTeachers.objects.none(),
#                     subject=Subject.objects.none(),
                )
            elif key_model == 'teachers':
                search_results = UniversalSearch(
                    teachers=BestTeachers.objects.filter(teacher_fullname_uz__icontains=key_word),
                    anons=Anons.objects.none(),
                    vacancy=Vacancy.objects.none(),
                    docs=Documents.objects.none(),
                    photos=PhotoGallery.objects.none(),
                    news=News.objects.none(),
                    videos=VideoGallery.objects.none(),
#                     subject=Subject.objects.none(),
                )
#             elif key_model == 'subject':
#                 search_results = UniversalSearch(
#                     subject=Subject.objects.filter(subject_name_uz__icontains=key_word),
#                     anons=Anons.objects.none(),
#                     vacancy=Vacancy.objects.none(),
#                     docs=Documents.objects.none(),
#                     photos=PhotoGallery.objects.none(),
#                     news=News.objects.none(),
#                     teachers=BestTeachers.objects.none(),
#                     videos=VideoGallery.objects.none(),
#                 )
            else:
                search_results = UniversalSearch(
                    news=News.objects.filter(news_title_uz__icontains=key_word),
                    anons=Anons.objects.filter(anons_title_uz__icontains=key_word),
                    vacancy=Vacancy.objects.filter(vacancy_name_uz__icontains=key_word),
                    docs=Documents.objects.filter(doc_title_uz__icontains=key_word),
                    photos=PhotoGallery.objects.filter(gallery_title_uz__icontains=key_word),
                    videos=VideoGallery.objects.filter(gallery_title_uz__icontains=key_word),
                    teachers=BestTeachers.objects.filter(teacher_fullname_uz__icontains=key_word),
                    # subject=Subject.objects.filter(subject_name_uz__icontains=key_word),
                )
            serializer = UniversalSearchSerializer(search_results)
            return Response(serializer.data)
        else:
            return Response(data={'result': 'error',
                                  'description':'search_key doesn\'t exist in your query params'})