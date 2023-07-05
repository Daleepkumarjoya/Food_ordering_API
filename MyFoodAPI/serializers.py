from rest_framework import serializers

from .models import HomeModel, AboutModel, MenuModel, contacModel, OrderModel


class HomeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeModel
        fields = "__all__"

        def validate_name(self, value):
            if value > 100:
                raise serializers.ValidationError('Enter Character less than 100')
                return value


class AboutModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'


class MenuModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


class contacModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contacModel
        fields = '__all__'


class OrderModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
