from django.urls import path
from . import views
urlpatterns=[
    path('demo1ab',views.ntrends,name='demo1ab'),
    path('pag1',views.page1,name='pag1'),
    path('pag2',views.page2, name='pag2'),
    path('pag3',views.page3, name='pag3')

]