from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from myapp.serializers import FoodsSerializer, DiseasesClassifySerializer, EatStatisticsSerializer, UserSerializer
from .models import User, EatStatistics, Foods, DiseasesClassify
import json
from myapp import models
from django.http import HttpResponse, JsonResponse


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FoodsSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    lookup_field = 'diseaseVariety'


class EatStatisticsSet(viewsets.ModelViewSet):
    queryset = EatStatistics.objects.all()
    serializer_class = EatStatisticsSerializer


class DiseasesClassifySet(viewsets.ModelViewSet):
    queryset = DiseasesClassify.objects.all()
    serializer_class = DiseasesClassifySerializer


from django.views.decorators.csrf import csrf_exempt


# 注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        account = request.POST.get('account')  # 用户名
        password = request.POST.get('password')  # 密码
        age = request.POST.get('age')  # 年龄

        user = models.User.objects.create(account=account, password=password, age=age)
        user.save()
        resp = {'message': "注册成功"}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': "该用户已存在"}
        return HttpResponse(json.dumps(resp))


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')  # 用户名
        password = request.POST.get('password')  # 密码
        user = User.objects.filter(account=account, password=password)
        if user:
            resp = {'message': "登录成功"}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': "登录失败"}
            return HttpResponse(json.dumps(resp))


# 每日摄入统计
@csrf_exempt
def eatStatistic(request):
    if request.method == 'POST':
        hot = request.POST.get('hot')
        protein = request.POST.get('protein')
        sugar = request.POST.get('sugar')
        time = request.POST.get('time')

        eat = models.EatStatistics.objects.create(eatHot=hot, eatProtein=protein, eatSugar=sugar, eatTime=time)
        eat.save()

        resp = {'message': "存入成功"}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': "存入失败"}
        return HttpResponse(json.dumps(resp))
