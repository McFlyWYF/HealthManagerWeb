from django.conf.urls import url, include
from rest_framework import routers
from myapp import views

app_name = '[myapp]'

routers = routers.DefaultRouter()

routers.register(r'user', views.UserSet)  # 用户
routers.register(r'foods', views.FoodsSet)  # 食谱
routers.register(r'disease', views.DiseasesClassifySet)  # 疾病分类
routers.register(r'eat', views.EatStatisticsSet)  # 摄入统计

urlpatterns = [
    url(r'^', include(routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
