from django.conf.urls import url, include 
from django.contrib import admin
from django.urls import path
from dash_app.views import company_article_list, ChartData  


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', company_article_list, name='companies'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-chart-data'),
]
