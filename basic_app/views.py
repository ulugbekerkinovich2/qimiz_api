from rest_framework import generics

from basic_app import models
from basic_app import serializers


# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset = models.DachaKategory.objects.all()
    serializer_class = serializers.DachaKategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DachaKategory.objects.all()
    serializer_class = serializers.DachaKategorySerializer


class ListQimizDachalari(generics.ListCreateAPIView):
    queryset = models.QimizOlishZonaDachalari.objects.all()
    serializer_class = serializers.QimizOlishZonaDachalariSerializer


class DetailQimizDachalari(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QimizOlishZonaDachalari.objects.all()
    serializer_class = serializers.QimizOlishZonaDachalariSerializer


class ListDachaVideo(generics.ListCreateAPIView):
    queryset = models.DachaVideo.objects.all()
    serializer_class = serializers.DachaVideoSerializer


class DetailDachaVideo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DachaVideo.objects.all()
    serializer_class = serializers.DachaVideoSerializer


class ListMijozlarFikrlariAudio(generics.ListCreateAPIView):
    queryset = models.MijozlarFikrlariAudio.objects.all()
    serializer_class = serializers.MijozlarFikrlariAudioSerializer


class DetailMijozlarFikrlariAudio(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MijozlarFikrlariAudio.objects.all()
    serializer_class = serializers.MijozlarFikrlariAudioSerializer


class ListMijozlarFikrlariImage(generics.ListCreateAPIView):
    queryset = models.MijozlarFikrlariImage.objects.all()
    serializer_class = serializers.MijozlarFikrlariImageSerializer


class DetailMijozlarFikrlariImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MijozlarFikrlariImage.objects.all()
    serializer_class = serializers.MijozlarFikrlariImageSerializer


class ListComments(generics.ListCreateAPIView):
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentsSerializer


class DetailComments(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentsSerializer


class ListForm(generics.ListCreateAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer


class DetailForm(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer


class ListAbout(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class DetailAbout(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class ListQimizDacha(generics.ListCreateAPIView):
    queryset = models.Qimiz_Dacha.objects.all()
    serializer_class = serializers.Qimiz_DachaSerializer


class DetailQimizDacha(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Qimiz_Dacha.objects.all()
    serializer_class = serializers.Qimiz_DachaSerializer
