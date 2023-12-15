from rest_framework.serializers import ModelSerializer

from .models import (
    News, Anons, Vacancy,
    Image, PhotoGallery,
    VideoGallery, VideoLinks
)


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        read_only_fields = ('news_views_count',)
        fields = '__all__'


class AnonsSerializer(ModelSerializer):
    class Meta:
        model = Anons
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PhotoGallerySerializer(ModelSerializer):
    gallery_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGallery
        read_only_fields = ['gallery_views_count',]
        fields = '__all__'


class VideoLinksSerializer(ModelSerializer):
    class Meta:
        model = VideoLinks
        fields = '__all__'


class VideoGallerySerializer(ModelSerializer):
    gallery_videos = VideoLinksSerializer(many=True, read_only=True)

    class Meta:
        model = VideoGallery
        read_only_fields = ['gallery_views_count',]
        fields = '__all__'
