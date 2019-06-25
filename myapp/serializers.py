from rest_framework import serializers
from .models import User, Foods, EatStatistics, DiseasesClassify

'''
json格式化model对象
'''

'''
用户
'''


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('account', 'password', 'age')


'''
食谱
'''


class FoodsSerializer(serializers.ModelSerializer):
    diseaseVariety = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = Foods
        fields = ('diseaseVariety','foodId', 'foodName', 'foodUrl','foodMaterial', 'foodHot', 'foodProtein', 'foodIntroduce')


'''
摄入统计
'''


class EatStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatStatistics
        fields = ('eatId', 'eatHot', 'eatProtein', 'eatSugar', 'eatTime')

'''
疾病种类
'''


class DiseasesClassifySerializer(serializers.ModelSerializer):
    foods = FoodsSerializer(source='foods_set', read_only=True, many=True,)  # 一对多关系

    class Meta:
        model = DiseasesClassify
        fields = ('diseaseVariety', 'diseaseIntroduce', 'foods')
