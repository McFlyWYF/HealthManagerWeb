from django.db import models

# Create your models here.

'''
用户表
'''


class User(models.Model):
    account = models.CharField(max_length=100, primary_key=True)  # 账号
    password = models.CharField(max_length=100, null=False)  # 密码
    age = models.CharField(max_length=20, null=False)  # 年龄

    def __str__(self):
        return self.account


'''
疾病表
'''


class DiseasesClassify(models.Model):
    diseaseVariety = models.CharField(max_length=50, primary_key=True)  # 心脏病种类
    diseaseIntroduce = models.TextField(max_length=1000, )  # 介绍

    def __str__(self):
        return self.variety


'''
食谱表
'''


class Foods(models.Model):
    foodId = models.IntegerField(auto_created=True, primary_key=True)  # 食物id
    foodName = models.CharField(max_length=100, null=False)  # 食物名称
    foodMaterial = models.CharField(max_length=200, )  # 食材
    foodHot = models.IntegerField()  # 热量
    foodProtein = models.IntegerField()  # 蛋白质
    foodIntroduce = models.TextField(max_length=200)  # 食物介绍
    foodUrl = models.URLField(max_length=200)  # 食物图片
    diseaseVariety = models.ForeignKey(DiseasesClassify, on_delete=models.CASCADE)  # 疾病名称，一种疾病对应多种食物

    def __str__(self):
        return self.diseaseVariety


'''
每日摄食统计表
'''



class EatStatistics(models.Model):
    eatId = models.IntegerField(auto_created=True, primary_key=True)  # 摄入食物id
    eatHot = models.IntegerField(null=False)  # 摄入热量
    eatProtein = models.IntegerField(null=False)  # 摄入蛋白质
    eatSugar = models.IntegerField(null=False)  # 摄入糖分
    eatTime = models.CharField(max_length=100)  # 摄入时间

    def __str__(self):
        return self.eatTime
