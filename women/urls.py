from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women import views

# router = routers.DefaultRouter()
# router.register(r'women', views.WomenViewSet, basename='women')

urlpatterns = [
    path('api/v1/women/', views.WomenAPIList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', views.WomenAPIDelete.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # Аутентификация через Djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # Аутентификация через Djoser
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Выдает токен для аутентификации
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновляет токен для аутентификации
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Проверяет токен для аутентификации
    # path('api/v1/women/', views.WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/women/<int:pk>/', views.WomenViewSet.as_view({'put': 'update',
    #                                                            'delete': 'destroy', 'get': 'retrieve'})),
    # path('api/v1/', include(router.urls)),
]
