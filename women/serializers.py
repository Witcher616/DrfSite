import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):  # Сериализатор для модели Women
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'
    # Ручное создание сериализатора с помощью Serializer
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_created = serializers.DateTimeField(read_only=True)
    # time_updated = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validation_data):
    #     return Women.objects.create(**validation_data)
    #
    # def update(self, instance, validation_data):
    #     instance.title = validation_data.get('title', instance.title)
    #     instance.content = validation_data.get('content', instance.content)
    #     instance.is_published = validation_data.get('is_published', instance.is_published)
    #     instance.cat_id = validation_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance
    #
    # def delete(self):
    #     self.instance.delete()


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data, type(serializer.validated_data), sep='\n')
