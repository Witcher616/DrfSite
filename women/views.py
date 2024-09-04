from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

# Работа с классом GenericViewSet

# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         pk = self.kwargs.get('pk')
#         cats = Category.objects.get(id=pk)
#         return Response({'category': cats.name})
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'category': [cat.name for cat in cats]})


class WomenAPIPagination(PageNumberPagination):
    page_size = 2  # Размер страницы
    page_size_query_param = 'page_size'  # Параметр для указания размера страницы со стороны
    # клиента через параметр 'page' http://localhost:8000/api/v1/women/?page=10
    max_page_size = 100  # Максимальное количество объектов в одном запросе


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDelete(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


# Ручная реализация API
# class WomenAPIview(APIView):
#     def get(self, request):
#         w_lst = Women.objects.all()
#         return Response({'posts': WomenSerializer(w_lst, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # post_new = Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     is_published=request.data['is_published'],
#         #     cat_id=request.data['cat_id']
#         # )
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'No Post ID provided.'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Post not found.'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'No Post ID provided.'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Post not found.'})
#         instance.delete()
#         return Response({'post': 'Post deleted.' + str(pk)})

# class WomenAPIview(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
