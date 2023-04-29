from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from basic_app import views

urlpatterns = [
    path('category/', views.ListCategory.as_view()),
    path('category/<int:pk>', views.DetailCategory.as_view()),
    path('qimiz_dachalari/', views.ListQimizDachalari.as_view()),
    path('qimiz_dachalari/<int:pk>', views.DetailQimizDachalari.as_view()),
    path('dacha_video/', views.ListDachaVideo.as_view()),
    path('dacha_video/<int:pk>', views.DetailDachaVideo.as_view()),
    path('mijozlar_fikrlari_audio/', views.ListMijozlarFikrlariAudio.as_view()),
    path('mijozlar_fikrlari_audio/<int:pk>', views.DetailMijozlarFikrlariAudio.as_view()),
    path('mijozlar_fikrlari_image/', views.ListMijozlarFikrlariImage.as_view()),
    path('mijozlar_fikrlari_image/<int:pk>', views.DetailMijozlarFikrlariImage.as_view()),
    path('comments/', views.ListComments.as_view()),
    path('comments/<int:pk>', views.DetailComments.as_view()),
    path('form/', views.ListForm.as_view()),
    path('form/<int:pk>', views.DetailForm.as_view()),
    path('about/', views.ListAbout.as_view()),
    path('about/<int:pk>', views.DetailAbout.as_view()),
    path('qimiz_dacha/', views.ListQimizDacha.as_view()),
    path('qimiz_dacha/<int:pk>', views.DetailQimizDacha.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
